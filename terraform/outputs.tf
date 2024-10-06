output "pubsub_topic" {
  value = google_pubsub_topic.data_topic.name
}

output "cloud_run_url" {
  value = google_cloud_run_service.fastapi_service.status[0].url
}