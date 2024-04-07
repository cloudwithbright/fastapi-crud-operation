## Define VPC

variable "appruner-vpc-cidr" {
  type = string
  description = ""
}

## Define Tags

variable "apprunner-vpc-tags" {
  type = map(string)
  description = ""
}

# variable "apprunner-vpc-outbound-egress-subnet-tags" {
#   type = map(string)
#   description = ""
# }

# variable "apprunner-vpc-inbound-igress-subnet-tags" {
#   type = map(string)
#   description = ""
# }

# ## Define Subnets Cidir

# variable "apprunner-vpc-inbound-igress-subnet-cidr" {
#   type = list(string)
#   description = ""
# }

# variable "apprunner-vpc-outbound-egress-subnet-cidr" {
#   type = list(string)
#   description = ""
# }

# ## Define Subnets Names

# variable "apprunner-vpc-inbound-igress-subnet-name" {
#   type = list(string)
#   description = ""
# }

# variable "apprunner-vpc-outbound-egress-subnet-name" {
#   type = list(string)
#   description = ""
# }

# ## Security Group

# variable "appruner-vpc-outbound-egress-security-group" {
#   type = string
#   description = ""
# }

# variable "appruner-vpc-inbound-igress-security-group" {
#   type = string
#   description = ""
# }