# Cloud Data Ingestion and Exposure System

## Overview

This project implements a cloud-based system for ingesting, storing, and exposing data using Infrastructure as Code (IaC) and CI/CD pipelines. The system is designed to ensure data is efficiently processed and made available through an HTTP API.

## Objectives

- **Data Ingestion**: Utilize a Pub/Sub pattern for data ingestion.
- **Data Storage**: Store data in a database optimized for analytics.
- **Data Exposure**: Provide an HTTP endpoint to serve stored data.
- **Infrastructure Deployment**: Deploy infrastructure using Terraform.
- **CI/CD**: Implement CI/CD pipelines for automated deployment.

## Architecture

The system architecture consists of the following components:

1. **Pub/Sub Topic**: Receives messages and triggers data processing.
2. **Cloud Function**: Processes incoming messages and stores data in BigQuery.
3. **BigQuery**: Serves as the data warehouse for analytics.
4. **FastAPI Application**: Provides an HTTP API to retrieve data from BigQuery.
5. **Cloud Run**: Hosts the FastAPI application in a serverless environment.

### Data Flow

1. **Message Ingestion**: Messages are published to a Pub/Sub topic.
2. **Data Processing**: A Cloud Function is triggered to parse and store data in BigQuery.
3. **Data Exposure**: A FastAPI application retrieves and serves data via an HTTP GET request.

## Technologies Used

- **Terraform**: For infrastructure provisioning.
- **Python**: For application logic in Cloud Functions and FastAPI.
- **Docker**: For containerizing the FastAPI application.
- **CI/CD**: Implemented using Cloud Build and YAML configurations.

## Infrastructure Details

### Terraform Resources

- **Pub/Sub Topic**: `google_pubsub_topic` (lines 6-8)
- **Storage Bucket**: `google_storage_bucket` (lines 10-13)
- **BigQuery Dataset**: `google_bigquery_dataset` (lines 15-18)
- **BigQuery Table**: `google_bigquery_table` (lines 20-24)
- **Cloud Function**: `google_cloudfunctions_function` (lines 26-42)
- **Artifact Registry**: `google_artifact_registry_repository` (lines 44-50)
- **Cloud Run Service**: `google_cloud_run_service` (lines 52-65)

## CI/CD Pipeline

The CI/CD pipeline is defined in `cloudbuild.yaml` and includes the following steps:

1. **Build**: Docker image is built for the FastAPI application.
2. **Push**: The Docker image is pushed to the Artifact Registry.
3. **Deploy**: The FastAPI application is deployed to Cloud Run.

## Usage

1. **Deploy Infrastructure**: Use Terraform to deploy the necessary infrastructure.
2. **Publish Messages**: Send messages to the Pub/Sub topic to trigger data ingestion.
3. **Access API**: Use the FastAPI endpoint to retrieve data from BigQuery.

## Diagram

![Architecture Diagram](link_to_diagram.png)

## Conclusion

This project demonstrates a complete end-to-end solution for data ingestion, storage, and exposure using cloud-native technologies and best practices in IaC and CI/CD.

## Proposed Integration Tests

1. **Data Ingestion Test**: Validate that messages published to the Pub/Sub topic are correctly processed and stored in BigQuery.
2. **API Query Parameter Test**: Ensure the API correctly handles various query parameters and returns expected results.
3. **Load Test**: Simulate multiple concurrent requests to the API to assess system performance under load.

## Critical Points and Testing Proposals

1. **Pub/Sub Message Processing Latency**: Measure the time from message publication to data storage in BigQuery.
2. **API Response Time**: Monitor and log response times to identify performance bottlenecks.
3. **BigQuery Query Performance**: Analyze and optimize query execution times.

## System Robustness Improvements

1. **Retries and Backoff**: Implement retries with exponential backoff for Pub/Sub message processing to handle transient errors.
2. **Caching**: Use caching mechanisms to reduce load on BigQuery for frequently accessed data.
3. **Monitoring and Alerting**: Implement monitoring and alerting for critical metrics such as API response time and error rates.

## Monitoring and Metrics

### Proposed Metrics

1. **Pub/Sub Message Processing Latency**: Measure the time taken from message publication to data storage in BigQuery.
2. **API Response Time**: Track the time taken for the FastAPI application to respond to requests.
3. **BigQuery Query Execution Time**: Monitor the time taken to execute queries in BigQuery.

### Visualization Tool

**Tool**: Google Cloud Monitoring

- **Metrics to Display**:
  - Pub/Sub Message Processing Latency
  - API Response Time
  - BigQuery Query Execution Time

- **Strategic Insights**: Visualizing these metrics helps identify performance bottlenecks and optimize system performance.

### Implementation Overview

1. **Setup Google Cloud Monitoring**: Enable and configure it in your GCP project.
2. **Create Dashboards**: Display the proposed metrics.
3. **Alerting**: Set up alerts for critical thresholds.

### Scaling Considerations

- **Visualization Changes**: Use grouping and filtering for multiple systems.
- **Additional Metrics**: Consider inter-system communication latency and error rates.
- **Visualization Techniques**: Use heatmaps or aggregate views.

### Challenges and Limitations

- **Data Overload**: Implement effective filtering and aggregation.
- **Alert Fatigue**: Ensure alerts are meaningful.
- **Scalability of Monitoring Infrastructure**: Ensure it can handle increased load.

--
