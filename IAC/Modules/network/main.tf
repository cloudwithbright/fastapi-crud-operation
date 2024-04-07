## Define VPC

resource "aws_vpc" "appruner-vpc" {
  cidr_block = var.appruner-vpc-cidr
  tags = var.apprunner-vpc-tags
}

## Define Subnets

# resource "aws_subnet" "apprunner-vpc-inbound-igress-subnet" {

#   count = length(var.apprunner-vpc-inbound-igress-subnet-cidr)
#   vpc_id     = aws_vpc.appruner-vpc.id
#   cidr_block = var.apprunner-vpc-inbound-igress-subnet-cidr[count.index]

#   tags = {
#     Name = var.apprunner-vpc-inbound-igress-subnet-name[count.index]
#   }
# }

# resource "aws_subnet" "apprunner-vpc-outbound-egress-subnet" {
    
#   count = length(var.apprunner-vpc-outbound-egress-subnet-cidr)
#   vpc_id     = aws_vpc.appruner-vpc.id
#   cidr_block = var.apprunner-vpc-outbound-egress-subnet-cidr[count.index]

#   tags = {
#     Name = var.apprunner-vpc-outbound-egress-subnet-name[count.index]
#   }
# }