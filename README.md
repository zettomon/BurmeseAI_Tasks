# Tasks for BurmeseAI
Description: Integration of  [all tasks](https://github.com/Burmese-AI/hiring) from BurmeseAI's hiring sections. The main page will navigate towards the respective page for all the tasks.

| For detailed documentation, [visit documentation.md](docs/documentation.md)

<img src="trying_hard.gif" width="250" height="250">

## Table of Contents
* Description
* Installation and quick start
* Check List
    * Internship Task 1
    * Internship Task 2
    * Junior Task 1
    * Junior Task 2

# Installation and quick start
### Prerequisites
Before you begin, ensure you have met the following requirements:
- **Python** (3.8 or higher)
- **pip**
- **Git**

### Installation
1. **Clone the repository**:
```bash
git https://github.com/zettomon/BurmeseAI_Tasks
cd BurmeseAI
```
2. **Set up a virtual environment**:
```bash
# Unix-based systems
virtualenv .venv
source .venv/bin/activate
```
```bash
# Windows 
python -m virtualenv .venv
.venv\Scripts\activate
```
3. **Install Dependencies**
```bash
pip install -r requirements.txt
```
4. **Prepare a `.env` File**:
Create a `.env` file in the root directory or rename the `.env-sample` to `.env` and modify it as needed
5. **Run migrations**:
```bash
python manage.py makemigrations
python manage.py migrate 
```
### Running the application
To start the development server, run:
```bash
python manage.py runserver
```
You can now access the appilcation at 
- http://127.0.0.1:8000/
- http://localhost:8000/
- http://your_ip_address:8000/

## Check List
## Internship Task 1: Data Submission Portal
| Task | Description | Status | 
| ---- | ----------- | ------ | 
| 1. Data Model and Mock Data| Define a DataEntry Model with fields | ✅ | 
| | Seed 50-100 entries |✅ | 
| 2. Frontend Interface | A form to submit new DataEntry | ✅ | 
| | Display entries in a table with columns | ✅ | 
| | Add a filter to show entries by category | ✅ | 
| 3. Basic Review Workflow | Add a button to toggle `is_reviewed` |✅|
| 4. Simple reporting | Show total entries per category |✅|
| Bonus | Search bar to filter entries by keywords in `content` | ✅|
| | Implement basic pagination for the data table | ✅ | 
| | Use HTMX for everything related to the frontend |✅|
## Internship Task 2: Financial Transaction Tracker
| Task | Description | Status |
| ---- | ----------- | ------ |
| 1. Transaction Model & Data | Define a Transaction Model | ✅ |
| | Seed 50-200 mock transactions | ❌ |
| 2. Frontend Interface | Submission Form | ❌|
| | Transaction Table | ❌|
| | Basic Filter | ❌|
| 3. Financial Reporting | Show Total Income, Total Expenses, Net Balance | ❌|
| | Calculate Average Monthly Expense | ❌|
| 4. Data Validation | Ensure users can't submit $0 or invalid amounts | ❌|
| | Prevent future dates in the `date` field | ❌|

<sub><sup> Author: Zett </sup></sub>