# Dockerfile

| Note: This dockerfile is used to create the docker image that's available at `zettomon/burmeseai-tasks`.

[Return to main the documentation](documentation.md)

## Structure
- This dockerfile uses `Builder Stage` and `Production Stage` to maximize efficiency
- Both stages uses `python:3.13-slim`

### Builder Stage
- Installs required packages via `requirements.txt

### Productin stage
- Adds a user called app_user
- Copies necessary packages from builder stage
- Exposes port `8000` from the application side
- Entrypoint will run `gunicorn --bind 0.0.0.0:8000 --workers 3 BurmeseAI.wsgi:application`