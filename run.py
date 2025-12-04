#!/usr/bin/env python
from utils import *
from dialogue.dialogue_etl import *
from abstract.abstract_etl import *
import asyncio
import sys
import json

async def dialogue_pipeline(targets, run_all):
    '''
    Main logic to handle patient-doctor conversation dialogue approach.
    '''
    # Download data
    if not dialogue_dataset_downloaded():
        download_dialogue()

    # Preprocess data, required step for analysis
    convos = preprocess_dialogue()

    # Data analysis
    if not visit_reasons_extracted() and (run_all or 'reasons' in targets):
        visit_reasons_df = await extract_reasons(convos)
    if not family_illness_extracted() and (run_all or 'illnesses' in targets):
        family_illnesses_df = await extract_family_illnesses(convos)
    if not symptoms_extracted() and (run_all or 'symptoms' in targets):
        symptoms_df = await extract_symptoms(convos)

async def abstracts_pipeline(targets, run_all):
    '''
    Main logic to handle research abstract searching for drug repurposing approach.
    '''
    # Load params
    with open('abstract/abstract_params.json') as fh:
        data_params = json.load(fh)
        
    # Download data
    if not abstract_dataset_downloaded():
        download_abstracts(**data_params)

    # Preprocess data, required step for analysis
    abstracts = preprocess_abstracts(**data_params)

    # Data analysis
    if not drug_candidates_extracted() and (run_all or 'repurposing' in targets):
        repurposing_candidates_df = await extract_candidates(abstracts)

async def main(targets):
    if 'clean' in targets:
        clean_files()

    run_all = 'all' in targets
    all_dialogue_subargs = ['reasons', 'illnesses', 'symptoms']
    run_dialogue_pipeline = any(arg in targets for arg in all_dialogue_subargs)
    all_abstract_subargs = ['repurposing']
    run_abstract_pipeline = any(arg in targets for arg in all_abstract_subargs)
    
    if run_all or run_dialogue_pipeline:
        await dialogue_pipeline(targets, run_all)
    if run_all or run_abstract_pipeline:
        await abstracts_pipeline(targets, run_all)

if __name__ == '__main__':
    targets = sys.argv[1:]
    asyncio.run(main(targets))
