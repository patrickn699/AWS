sudo yum update -y
sudo yum install git -y
git clone https://github.com/patrickn699/AWS.git
cd AWS
cd ec2-sns
sudo chmod u+x semi-auto.sh
sudo ./semi-auto.sh