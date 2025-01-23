FROM python:3.9.6-slim-buster
WORKDIR /app
COPY . /app


RUN apt update -y && apt install awscli -y
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]

# Use a base image (e.g., Ubuntu)
FROM ubuntu:latest

# Update and clean package lists
RUN apt-get clean && rm -rf /var/lib/apt/lists/* && apt-get update