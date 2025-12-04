import os 
import shutil
'''
Utility functions for project.
'''

def clean_files():
    '''
    Deletes all built files. Reverts to clean repo.
    '''
    data_dir = "data"
    if not os.path.exists(data_dir):
        print("`data/` directory does not exist.")
        return

    for root, dirs, files in os.walk(data_dir):
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            shutil.rmtree(dir_path)

    print("All files and folders inside `data/` have been deleted.")

def dialogue_dataset_downloaded():
    '''
    Determines if patient-doctor dialogue dataset is downloaded and in correct location.
    '''
    dialogue_fp = os.path.join("data", "MTS-Dialog-TrainingSet.csv")
    return os.path.isfile(dialogue_fp)

def abstract_dataset_downloaded():
    '''
    Determines if PubMed abstract dataset is downloaded and in correct location.
    '''
    abstract_fp = os.path.join("data", "PubMed_abstracts.csv")
    return os.path.isfile(abstract_fp)

def visit_reasons_extracted():
    '''
    Determines if patient visit reasons data has been extracted.
    '''
    visit_reasons_fp = os.path.join("data", "visit_reasons.csv")
    return os.path.isfile(visit_reasons_fp)

def family_illness_extracted():
    '''
    Determines if patient family illness data has been extracted.
    '''
    family_illness_fp = os.path.join("data", "family_illnesses.csv")
    return os.path.isfile(family_illness_fp)

def symptoms_extracted():
    '''
    Determines if patient symptoms data has been extracted.
    '''
    symptoms_fp = os.path.join("data", "symptoms.csv")
    return os.path.isfile(symptoms_fp)

def drug_candidates_extracted():
    '''
    Determines if abstract drug repurposing data has been extracted.
    '''
    drug_candidates_fp = os.path.join("data", "drug_candidates.csv")
    return os.path.isfile(drug_candidates_fp)