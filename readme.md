<!-- PREREQUISITES FOR RUNNING Docker example -->

open cmd prompt in vscode with cd in /sftp-docker-test
npm install paramiko

Docker Desktop must be installed https://docs.docker.com/desktop/setup/install/windows-install/

<!-- Setting up Source file -->

the files in source all need to be .txt or .TXT extensions to be transferred correctly.
Just place the .txt files into source for setup.

open cmd prompt for docker setup.

Docker terminal
cd C:\Users\LukeDurham\Desktop\sftp-docker-test
docker-compose up -d

Python terminal
run python sftp_test_script.py
