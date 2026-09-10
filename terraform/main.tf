terraform {
  required_version = ">= 1.16.0, < 2.0.0"
}

variable "environment" {
  type        = string
  description = "Deployment environment."
}

output "example" {
  description = "Training-only Terraform output."
  value       = "devops-${var.environment}"
}
