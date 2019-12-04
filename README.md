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
#### -Python3
Download Python2 from [here](https://www.python.org/downloads/).
#### -VirtualBox
Download VirtualBox from [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).
#### -Vagrant
download Vagrant from [here](https://www.vagrantup.com/).
#### Get news sql script 
Download news database script from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

## Running the Project:
#### Navigate to the directory that containing the **vagrantfile**
-Vagrantfile containing:
##### 1-Configuration of the VM.
##### 2-Install Python
##### 3-Install Postgres Database.
##### 4-Creating Database **news**.

### Steps:
#### 1-Run the following command to start the VM ssh into the vagrant box:
`vagrant up`

#### 2-Run the following command to ssh into the VM:
`vagrant ssh`

#### 3-After login to the VM, Extract  newsdata.zip

#### 4-Run the following command to create tables and insert data into news database:
`psql -d news -f newsdata.sql`

#### 5-Connect to the database and create the views where in **Views.txt**
`psql news`
Run Views creation , run them with the same sequnce.

#### 6-Run Python Program **loganalysis.py** and log analysis will be printed
`python2 loganalysis.py`


