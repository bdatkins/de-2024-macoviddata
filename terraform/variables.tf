variable "credentials" {
  description = "Path to the credentials file"
  default     = "../keys/gcp-creds.json"
}

variable "project_id" {
  type        = string
  description = "The name of the project"
  default     = "dtc-de-ma-covid-data"
}

variable "region" {
  description = "Region Name"
  default     = "us-east1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "zone" {
  type        = string
  description = "The default compute zone"
  default     = "us-east1-b"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "covid_data"
}

variable "gcs_bucket_name" {
  description = "Google Cloud Bucket Name"
  default     = "de-project-coviddata"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "app_name" {
  type        = string
  description = "Application Name"
  default     = "de-macovid-data"
}

variable "container_cpu" {
  description = "Container cpu"
  default     = "2000m"
}

variable "container_memory" {
  description = "Container memory"
  default     = "2G"
}

variable "repository" {
  type        = string
  description = "The name of the Artifact Registry repository to be created"
  default     = "de-covid-data-prep"
}

variable "docker_image" {
  type        = string
  description = "The docker image to deploy to Cloud Run."
  # default     = "docker.io/bdatkinsdev/de_project_coviddata:latest"
  default     = "us-east1-docker.pkg.dev/dtc-de-ma-covid-data/de-ma-covid-data-repo/de_project_coviddata"  
}

variable "domain" {
  description = "Domain name to run the load balancer on. Used if `ssl` is `true`."
  type        = string
  default     = ""
}

variable "ssl" {
  description = "Run load balancer on HTTPS and provision managed certificate with provided `domain`."
  type        = bool
  default     = false
}