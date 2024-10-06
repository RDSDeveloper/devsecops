provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_pubsub_topic" "data_topic" {
  name = "data-topic"
}

resource "google_storage_bucket" "function_bucket" {
  name     = "${var.project_id}-function-bucket"
  location = var.region
}

resource "google_bigquery_dataset" "analytics_dataset" {
  dataset_id = "analytics_dataset"
  location   = var.region
}

resource "google_bigquery_table" "data_table" {
  dataset_id = google_bigquery_dataset.analytics_dataset.dataset_id
  table_id   = "data_table"
  schema     = file("schema.json")
}

resource "google_cloudfunctions_function" "data_processor" {
  name        = "data-processor"
  runtime     = "python310"
  entry_point = "process_data"
  source_archive_bucket = google_storage_bucket.function_bucket.name
  source_archive_object = "cloud-function.zip"
  trigger_http = false
  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource   = google_pubsub_topic.data_topic.id
  }
}

resource "google_artifact_registry_repository" "docker_repo" {
  provider = google-beta
  location = var.region
  repository_id = "fastapi-repo"
  format = "DOCKER"
  project = var.project_id  
}

resource "google_cloud_run_service" "fastapi_service" {
  name     = "fastapi-service"
  location = var.region
  template {
    spec {
      containers {
        image = "REGION-docker.pkg.dev/${var.project_id}/fastapi-repo/fastapi-app:latest"
      }
    }
  }
}