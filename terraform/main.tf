resource "google_storage_bucket" "scada_data_lake" {
  name                        = var.bucket_name
  location                    = "NORTHAMERICA-NORTHEAST1"
  force_destroy               = false
  uniform_bucket_level_access = true
}

resource "google_bigquery_dataset" "wind_farm_dataset" {
  dataset_id = var.bq_dataset_id
  location   = "northamerica-northeast1"
}