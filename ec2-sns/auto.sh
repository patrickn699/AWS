sudo yum update
sudo yum install git
git clone https://github.com/patrickn699/AWS.git
cd AWS
cd ec2-sns
pip3 install streamlit
pip3 install boto3
streamlit run main.py