import csv
import requests
from Bio import Entrez
from semlib import Session
import os
from collections import Counter
import asyncio
import pandas as pd
'''
dialogue_etl.py contains for extracting, transforming, and loading the data from the patient-doctor conversations.
'''

MAX_CONCURRENCY = 3
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
session = Session(model="openai/gpt-4.1-mini", max_concurrency=MAX_CONCURRENCY)

def download_dialogue():
    '''
    Downloads the dialogue. Saves data in data/MTS-Dialog-TrainingSet.csv
    '''
    url = "https://raw.githubusercontent.com/abachaa/MTS-Dialog/main/Main-Dataset/MTS-Dialog-TrainingSet.csv"
    
    save_path = os.path.join("data", "MTS-Dialog-TrainingSet.csv")
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"File downloaded and saved to {save_path}")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")

def preprocess_dialogue():
    '''
    Returns structured list of conversations.
    Must have data/MTS-Dialog-TrainingSet.csv first. Run `python run.py download_dialogue` if you don't.
    '''
    path = "data/MTS-Dialog-TrainingSet.csv"
    if not os.path.exists(path):
        raise FileNotFoundError(
            "Must have data/MTS-Dialog-TrainingSet.csv first. Run `python run.py download_dialogue`"
        )
    
    with open("data/MTS-Dialog-TrainingSet.csv", encoding="latin-1") as f_in:
        csv_file = csv.reader(f_in)
        header = next(csv_file)
        convos = [dict(zip(header, row, strict=False)) for row in csv_file]

    print(f"Loaded {len(convos)} conversations\n")
    return convos


async def extract_reasons(convos):
    '''
    Returns dataframe of extracted reasons for each patient visit.
    Saves csv to data/visit_reasons.csv
    '''
    extracted_reasons = await session.map(
        convos,
        template=lambda r: f"""
        Extract the patient's chief complaint or reason for coming to the doctor. 1-2 word response only. No capitalization. If patient has no reasons, respond with none.
        {r['dialogue']}
        """.strip(),
    )
    print(f'Example reason: {extracted_reasons[0]}')
    df = pd.DataFrame(extracted_reasons)
    df.to_csv("data/visit_reasons.csv", index=False)
    return df

async def extract_family_illnesses(convos):
    '''
    Returns dataframe of family illnesses for each patient visit.
    Saves csv to data/family_illnesses.csv
    '''
    extracted_family_illnesses = await session.map(
        convos,
        template=lambda r: f"""
        Extract the any illness(es) that the patient and doctor are concerned about. Respond with only the illness(es) separated by commas. No capitalization. If patient has no family illness, respond with none.
        {r['section_text']}
        """.strip(),
    )
    print(f'Example family illness: {extracted_family_illnesses[0]}')
    df = pd.DataFrame(extracted_family_illnesses)
    df.to_csv("data/family_illnesses.csv", index=False)
    return extracted_family_illnesses

async def extract_symptoms(convos):
    '''
    Returns dataframe of extracted symptoms for each patient visit.
    Saves csv to data/symptoms.csv
    '''
    extracted_symptoms = await session.map(
        convos,
        template=lambda r: f"""
        Extract the patient's symptom(s). Respond with only the symptom(s) separated by commas. 1-2 words for each symptom. If patient has no symptons, respond with none.
        {r['section_text']}
        """.strip(),
    )
    print(f'Example symptom: {extracted_symptoms[0]}')
    df = pd.DataFrame(extracted_symptoms)
    df.to_csv("data/symptoms.csv", index=False)
    return extracted_symptoms

async def extract_medications(convos):
    '''
    Returns dataframe of extracted medications currently taking for each patient visit.
    Saves csv to data/medications.csv
    '''
    extracted_medications = await session.map(
        convos,
        template=lambda r: f"""
        Extract the medications the patient is currently taking. Respond with only the medication(s) separated by commas. 1-2 words for each medication. If patient is taking no medication, respond with none.
        {r['section_text']}
        """.strip(),
    )
    print(f'Example medication: {extracted_medications[0]}')
    df = pd.DataFrame(extracted_medications)
    df.to_csv("data/medications.csv", index=False)
    return extracted_medications