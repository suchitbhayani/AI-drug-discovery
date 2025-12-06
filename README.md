# AI-drug-discovery

## Project Overview

This is a capstone project for **UCSD Data Science (DSC 180A)** in Domain B23, mentored by Murali Krishnam from Solix Technologies. The project focuses on **AI-driven drug discovery using natural language processing (NLP)** techniques to analyze medical literature and patient-doctor conversations.

**Goal:** Combine patient dialogue analysis with medical literature mining to identify potential drug repurposing candidates and extract meaningful clinical insights for drug discovery research, with a specific focus on Alzheimer's disease treatment.

**Approach:** The project uses neuro-symbolic AI techniques, semantic analysis, and large language models to:
- Extract clinical information from patient-doctor dialogues
- Mine PubMed abstracts for drug repurposing opportunities
- Identify relationships between symptoms, medications, and potential treatments

---

This project provides scripts to **download and process patient-doctor dialogue and medical paper abstract datasets** related to drug discovery. The code automatically stores CSV files in the `data/` directory and performs ETL (Extract, Transform, Load) operations on them.  

For data visualizations and findings, see `viz/eda.ipynb`.

---

## Data Sources

### Patient-Doctor Dialogue Data
- **Source:** Medical dialogue datasets accessed via automated API calls
- **Content:** Conversations between patients and doctors including visit reasons, symptoms, family medical history, and current medications
- **Access Method:** Automatically downloaded and processed via the scripts in the `dialogue/` directory
- **Storage:** Processed data stored as CSV files in the `data/` directory

### PubMed Abstract Data
- **Source:** PubMed Central API (National Center for Biotechnology Information)
- **Content:** Medical research paper abstracts related to drug discovery and Alzheimer's disease
- **Access Method:** Queries via PubMed E-utilities API using semantic search
- **Configuration:** Search parameters configurable in `abstract/abstract_params.json`
- **Storage:** Processed drug candidates and analysis results stored in `data/drug_candidates.csv`

**Note:** Raw data files are not included in this repository. The scripts download and process data automatically when targets are run. All processed outputs are saved to the `data/` directory, which is gitignored to avoid committing large datasets.

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

## Troubleshooting

### Common Issues

**Issue: ModuleNotFoundError**
- Solution: Ensure you've activated the virtual environment and installed all dependencies with `pip install -r requirements.txt`

**Issue: OpenAI API errors**
- Solution: Verify your API key is correctly set in the `.env` file and has sufficient credits

**Issue: PubMed API rate limiting**
- Solution: The script includes built-in delays. If you still encounter issues, try running smaller batches or contact PubMed about rate limits

**Issue: Empty CSV files**
- Solution: Check your internet connection and API credentials. Ensure the target datasets are available

---

## Contributing

This is a capstone project for UCSD Data Science (DSC 180A). Contributions are welcome from project team members.

---

## License

This project is for educational purposes as part of UCSD coursework.