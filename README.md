# AI-drug-discovery

This project provides scripts to **download and process patient-doctor dialogue and medical paper abstract datasets** related to drug discovery. The code automatically stores CSV files in the `data/` directory and performs ETL (Extract, Transform, Load) operations on them.  

For data visualizations and findings, see `viz/eda.ipynb`.
---

## Setup

1. **Clone the repository**:  
```bash
git clone https://github.com/suchitbhayani/AI-drug-discovery.git
cd AI_drug_discovery
```

2. **Create and activate a virtual environment**

```bash
# Create a virtual environment named 'env'
python -m venv env

# Activate on Windows Git Bash
source env/Scripts/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Create a .env file at the root of the project containing your API key and email**

```ini
OPENAI_API_KEY=your_openai_api_key_here
EMAIL=your_email_here
```

---

## File organization
`abstract` directory has code and parameter configurations for the research abstract data approach. You can configure parameters in `abstract/abstract_params.json`.

`dialogue` directory has code for the patient-doctor conversation data approach. There are currently no parameters to configure for this approach.

`viz` directory has the data visualizations and analysis in a jupyter notebook.

---

## Usage 

Run the main `run.py` script with **targets** to specify what to download and process.

### Targets

- **`all`** – Runs all targets.
- **`clean`** - Deletes all built files. Reverts to clean repository.

Patient-Doctor Dialogue Analysis:
- **`reasons`** – Extracts visit reasons from dialogue data. Saves csv to `data/visit_reasons.csv`
- **`illnesses`** – Extracts family illnesses from dialogue data. Saves csv to `data/family_illnesses.csv`
- **`symptoms`** – Extracts symptoms from dialogue data. Saves csv to `data/symptoms.csv`
- **`medications`** – Extracts medications the patient is currently taking from dialogue data. Saves csv to `data/medications.csv`

PubMed Abstract Analysis:
- **`repurposing`** – Extracts drug repurposing candidates data. Saves csv to `data/drug_candidates.csv`

Run these by running `python run.py [any combination of targets]`

### Examples

1. **Extracts patient reasons for visits and family illnesses from patient-doctor dialogue data:**
```bash
python run.py reasons illnesses 
```

2. **Extracts drug repurposing candidate data from research paper abstract data:**
```bash
python run.py repurposing
```
