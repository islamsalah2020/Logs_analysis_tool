# Logs Analysis Project
## Project Overview
This is an internal reporting tool that produces some Info out in the plain text in the Terminal.
The tool produces answers to the following three questions based on the data in the database:

#### 1- What are the most popular three articles of all time?
#### 2- Who are the most popular articles authors of all time?
#### 3- On which days did more than 1% of requests lead to errors?

This tool is a **Python** program that uses the **psycopg2** module to connect to the database.

## Getting started
you need to install:
#### -VirtualBox
#### -Vagrant

## Running the Project:
#### Navigate to the directory that containing the **vagrantfile**
-Vagrantfile containing:
##### 1-Configuration of the VM.
##### 2-Install Python
##### 3-Install Postgres Database.
##### 4-Creating Database **news**.

#### Run the following command to start the VM ssh into the vagrant box:
`vagrant up`

#### Run the following command to ssh into the VM:
`vagrant ssh`

#### After login to the VM, Extract  newsdata.zip

#### Run the following command to create tables and insert data into news database:
`psql -d news -f newsdata.sql`

#### Connect to the database and create the views where in **Views.txt**

#### Run Python Program **loganalysis.py** and log analysis will be printed
python loganalysis.py


