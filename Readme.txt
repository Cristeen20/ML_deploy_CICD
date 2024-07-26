# Python-Based Data Analytics Application

## Overview
This project is a Python-based data analytics application that implements a complete CI/CD pipeline using Docker, Minikube, Jenkins, and other tools. The pipeline automates the building, testing, deploying, and monitoring processes. The application performs basic data analysis on a sample dataset.

## Project Structure


## Setup Instructions

### Prerequisites
- Install Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/)
- Install Minikube: [Minikube Installation Guide](https://minikube.sigs.k8s.io/docs/start/)
- Install Jenkins: [Jenkins Installation Guide](https://www.jenkins.io/doc/book/installing/)
- Install Python 3.x and virtualenv

### Clone the Repository
```bash
git clone https://github.com/Cristeen20/ML_deploy_CICD.git
cd ML_deploy_CICD

# Setup Python environment 
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

# Run locally
python src/app.py
