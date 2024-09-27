#!/bin/bash
yum update -y
pip3 install fastapi[all]
pip3 install uvicorn[standard]
yum -y install git
sudo git clone https://gitlab_ci_token:your_access_token@gitlab.com/your_username/awsproject.git
cd awsproject
/usr/local/bin/uvicorn main:app --host 0.0.0.0 --port 8000
