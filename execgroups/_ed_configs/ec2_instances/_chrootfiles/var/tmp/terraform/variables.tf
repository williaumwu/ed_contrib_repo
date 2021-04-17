variable "ami_search" {
  type    = list
  default = ["amzn2-ami-hvm-*-x86_64-ebs"]
}

variable "owners" {
  default     = ["amazon"]
}

variable "security_group_ids" {
  type        = string
}

variable "subnet_id" {
  type        = string
}

variable "server_name_base" {
  type        = string
}

variable "key_name" {
  type        = string
}

variable "volume_size" {
  default     = 80
}

variable "instance_type" {
  type        = string
  default     = "t3.micro"
}

variable "server_count" {
  default     = 1
}

