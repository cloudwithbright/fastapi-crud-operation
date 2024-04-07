include "root" {
  path = find_in_parent_folders("common.hcl")
}

terraform {
    source = "../../../Modules/network"

    extra_arguments "custom_vars" {
    commands = [
      "apply",
      "plan",
      "import",
      "push",
      "refresh",
      "init",
      "fmt",
      "validate"
    ]
    #required_var_files = ["terraform.tfvars"]
  }
}

inputs = {
  "appruner-vpc-cidr" = "10.0.0.0/16"
  "apprunner-vpc-tags" = {
    "Name"="gtuc-apprunner-vpcconnector"
  }
  # "apprunner-vpc-outbound-egress-subnet-tags"={
  #   "Name" = ""
  # }
}