# Documentation
| Note: Each application will be documented in a separated page to maximize versatility

## Table of Contents
1. Home page
    - This page will include links to the tasks and will redirect you towards all the four apps
2. [Data Submission Portal](data_submission.md)
    - This app allows you to submit data submission form, with paginated functionalities on searched result, filtered result and can easily mark the data entries as reviewed
3. Transaction Tracker
4. Transaction Audit Dashboard
5. Scalable Data Pipeline
6. [Dockerfile](dockerimage.md)
    - The base file to generate a docker image

### Project Structure
- Every HTML-related front-end UIs will be placed under /templates with sub-directories representing respective application
    - E.g. Data Submission Portal application will have its frontends under /templates/submission_portal/
- Every backend application will have its own directory created by `python mange.py startapp app_name`
- .env_sample will be provided but it should be configured accordingly
- Dockerfile is used to create Docker Image that's already available publicly at `zettomon/burmeseai-tasks`