

#  POC-46
<img width="359" height="247" alt="{653D5263-96A9-4A6A-9F13-1CD153F82741}" src="https://github.com/user-attachments/assets/08a29d60-9acf-4b9f-88c9-c76a14601f09" />

##  Overview

This PoC automates the detection and deletion of unused AWS resources to reduce cloud costs and improve infrastructure hygiene. It uses a Python script powered by the **Boto3 SDK** to identify and clean up orphaned or idle resources such as:

- Stopped EC2 instances  
- Unattached EBS volumes  
- Unused Elastic IPs  

---

##  Implementation Steps

### Step 1: EC2 Instance Setup

Launch an **Ubuntu-based EC2 instance** to host and execute the cleanup automation script.

---

### Step 2: Install Required Tools

Run the following commands to install Python, pip3, Boto3, and AWS CLI:

```bash
# Update the system
sudo apt update -y
sudo apt upgrade -y

# Install Python 3 and pip
sudo apt install python3 -y
python3 --version

sudo apt install python3-pip -y
pip3 --version

# Install Boto3 (AWS SDK for Python)
pip3 install boto3 --user

# Install AWS CLI
sudo apt install awscli -y
aws --version
```

---

### Step 3: Configure AWS CLI

Configure AWS CLI with your credentials to allow authenticated access to AWS services:

```bash
aws configure
```

You will be prompted to enter:

- Access Key ID  
- Secret Access Key  
- Default region name  
- Default output format  

---

### Step 4: Execute Python Script

Ensure your cleanup script (`cleanupfile.py`) has the correct permissions and execute it:

```bash
chmod 777 cleanupfile.py
python3 cleanupfile.py
```

---

##  Expected Output

The script will produce clean and concise terminal output indicating the resources being cleaned up. Example:

```
Stopped EC2 Instances:
- i-0abcd1234efgh5678 (Terminated)

Unattached EBS Volumes:
- vol-0123456789abcdef0 (Deleted)

Unused Elastic IPs:
- 54.123.45.67 (Released)
```

---

---

