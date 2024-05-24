
#################################
# Define the input variables    #
#################################

variable "tenant_id" {
  type = string
  sensitive = true
}

variable "github_token" {
  description = "GitHub Personal Access Token."
  type        = string
  sensitive   = true
}

variable "github_owner" {
  description = "GitHub organization or username."
  type        = string
}

variable "github_repository" {
  description = "The name of the GitHub repository."
  type        = string
}