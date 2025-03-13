# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# https://www.docker.com/blog/how-to-dockerize-django-app/  #
# Referred from the above link                              #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

### Builder Stage
FROM python:3.13-slim AS builder
RUN mkdir /app
WORKDIR /app

# ENVs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
# Package Installations
RUN pip install --upgrade pip 
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
 

### Production Stage

FROM python:3.13-slim
 
# For Troubleshooting
#RUN apt-get update && \
    #apt-get install -y --no-install-recommends \
    #curl \
    #net-tools \
    #procps \
    #&& apt-get clean \
    #&& rm -rf /var/lib/apt/lists/*

RUN useradd -m -r app_user && \
   mkdir /app && \
   chown -R app_user /app
 
# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
 
WORKDIR /app
COPY --chown=app_user:app_user . .
 
# ENVs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
 
USER app_user
EXPOSE 8000 

# Start the application using Gunicorn
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "BurmeseAI.wsgi:application"]
