#!/bin/bash
yum update -y
yum install -y git 
git clone https://github.com/patrickn699/AWS.git
cd AWS
cd ec2-sns
sudo chmod u+x semi-auto.sh
sudo ./semi-auto.sh