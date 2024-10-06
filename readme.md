# DevSecOps/SRE Challenge

This project demonstrates a cloud-based data ingestion, storage, and exposure system using GCP services, Terraform, FastAPI, and GitHub Actions.

## Components

- **Cloud Pub/Sub**: For receiving messages from various sources.
- **Cloud Function**: Processes incoming messages and stores them in BigQuery.
- **BigQuery**: Stores processed data for analytics.
- **Cloud Run**: Hosts a FastAPI application to expose data via HTTP GET requests.
- **GitHub Actions**: CI/CD pipeline for deploying the FastAPI application.

## Setup

1. Configure your GCP project and enable necessary APIs.
2. Set up Terraform and apply the configuration in the `terraform/` directory.
3. Deploy the Cloud Function by uploading the `cloud-function/` code as a zip to the specified GCS bucket.
4. Use GitHub Actions to build and deploy the FastAPI application to Cloud Run.

## Usage

- Send messages to the Pub/Sub topic to trigger data ingestion.
- Access the FastAPI endpoint to retrieve data from BigQuery.