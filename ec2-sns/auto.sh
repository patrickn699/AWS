sudo yum update -y
sudo yum install git -y
git clone https://github.com/patrickn699/AWS.git
cd AWS
cd ec2-sns
pip3 install streamlit
pip3 install boto3
streamlit run main.py