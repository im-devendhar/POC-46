POC-46 

 

 

 

Overview 

This PoC is designed to automate the detection and deletion of unused AWS resources to reduce costs and improve cloud hygiene. It uses a Python script that interacts with AWS services via the Boto3 SDK to identify and clean up orphaned or idle resources. 

Implementation Steps 

Step 1: EC2 Instance Setup 

An EC2 instance was created to run and test the AWS cleanup automation project. 

Step 2: Install Python, pip3, and Boto3 

The following commands were used to install Python 3, pip3, and the Boto3 library: 

# Step 1: Update the system 

sudo apt update -y 

sudo apt upgrade -y 

  

# Step 2: Install Python 3 and pip 

sudo apt install python3 -y 

python3 --version 

  

sudo apt install python3-pip -y 

pip3 --version 

  

# Step 3: Install Boto3 (AWS SDK for Python) 

pip3 install boto3 --user 

  

# Step 4: Install AWS CLI 

sudo apt install awscli -y 

aws --version 

  

# Step 5: Configure AWS CLI with your credentials 

aws configure 

# (Enter Access Key, Secret Key, Region, and Output format when prompted) 

  

# Step 6: Set permissions and run your Python script 

chmod 777 cleanupfile.py 

python3 cleanupfile.py 

  

Step 3: Configure AWS CLI 

AWS CLI was configured on the EC2 instance using the following command to enable authenticated access to AWS services: 

aws configure 

 

 

Below are the stopped instances, unattached volumes and Unused Elastic IPs 

 

 

 

 

Step 4: Execute Python Script 

The Python automation script was executed using the following command to delete unused AWS resources: 

python3 cleanupfile.py 

 

 

 

 

 

Expected Output Style 

The script produces clean and concise terminal output indicating the resources being cleaned up.  

Example output: 

 

After executing the cleanupfile.py stopped instances, unattached volumes and Unused Elastic IPs 

 

 

 

 

 

 

 
