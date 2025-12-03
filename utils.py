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
