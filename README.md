# Tasks for BurmeseAI
Description: Integration of  [all tasks](https://github.com/Burmese-AI/hiring) from BurmeseAI's hiring sections. The main page will navigate towards the respective page for all the tasks.

<img src="trying_hard.gif" width="250" height="250">

## Table of Contents
* Description
* Installation guide
* Check List
    * Internship Task 1
    * Internship Task 2
    * Junior Task 1
    * Junior Task 2

## Instructions and Information
* All the packages used have been listed in `requirements.txt`
* Mock data can easily be seeded via a script:
    * Internship Task 1: `python manage.py seed_data`
        * Script directory: `submission_portal/management/commands/`


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
| | Implement basic pagination for the data table | 🔜 | 
| | Use HTMX for everything related to the frontend |🔜 |
## Internship Task 2: Financial Transaction Tracker
| Task | Description | Status |
| ---- | ----------- | ------ |
| 1. Transaction Model & Data | Define a Transaction Model | ❌ |
| | Seed 50-200 mock transactions | ❌|
| 2. Frontend Interface | Submission Form | ❌|
| | Transaction Table | ❌|
| | Basic Filter | ❌|
| 3. Financial Reporting | Show Total Income, Total Expenses, Net Balance | ❌|
| | Calculate Average Monthly Expense | ❌|
| 4. Data Validation | Ensure users can't submit $0 or invalid amounts | ❌|
| | Prevent future dates in the `date` field | ❌|

<sub><sup> Author: Zett </sup></sub>