variable "project_id" {
  description = "GCP project ID"
  type        = string
  default     = "wind-farm-analytics-janio"
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "northamerica-northeast1"
}

variable "bucket_name" {
  description = "GCS bucket name"
  type        = string
  default     = "wind-farm-analytics-janio-scada-data"
}

variable "bq_dataset_id" {
  description = "BigQuery dataset ID"
  type        = string
  default     = "wind_farm"
}