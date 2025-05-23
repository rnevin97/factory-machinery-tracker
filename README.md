# factory-machinery-tracker

![Dashboard](https://github.com/user-attachments/assets/121e4194-9811-46d8-b41a-630195331178)

![image](https://github.com/user-attachments/assets/11ba8bd1-d6d7-4858-a0e1-2a812790007b)

![image](https://github.com/user-attachments/assets/6a3094b8-ba5f-419e-87a2-1be8aa65ad8c)

![image](https://github.com/user-attachments/assets/21db995a-2d06-4064-9a4d-a970583fd534)

![image](https://github.com/user-attachments/assets/df01fee6-2174-4dfb-a237-5a5ce1c5898c)

![AddMachine](https://github.com/user-attachments/assets/cd07ec14-2806-4cfb-9bdf-57236dd1bca3)


![image](https://github.com/user-attachments/assets/5d600740-eef5-4506-88e1-b21f1cbcf462)




![alt text](IssueScreen.PNG) 

![alt text](<add_modify issue.PNG>)



# Overview of functionality
Registration:
•	User can register as a Manager or Technician
•	During registration, a new company record will be created based on user input
•	Manager of the company will be able to see all registered technicians under the same company
Navigation Menu:
•	Dashboard: in progress
•	Machines: list all machines under the same company
•	Repair Request: list of all the repair requests raised against the machines in the company
•	Technicians: Only managers can see this option, which will list all technicians registered in the company
Machines Page:
•	Manager:
o	New Machine Button: Only visible to managers, so only they can add machines.
o	Managers can modify and delete the machines.
o	When a machine is deleted, all corresponding issues against it will be deleted too.
•	Technician:
o	Technicians can only see the available machine, but they cannot add/modify/delete any
Technician Page:
•	Only visible to manager, list all technician and their details under the company
Repair Requests Page:
•	Manager:
o	Manager can see all the issues raised against the machines in the company.
o	They can only modify, change the request status , and delete it
•	Technician:
o	They can do all the task as Manager and also can raise new requests


Testing Machine Page :
1. You can add new Machine through queries at the moment
INSERT INTO machinery_company (id,name,email,phone,job_title) VALUES ('1','TestComapny','test@test.com','123444','manager')

INSERT INTO machinery_machine (id, name , serial_number, importance, status, company_id) VALUES ('1', 'Test Machinery' , 'SERIAL1123', '1', 'Working','1')
2. Now when you load the machines pages, you should be able to see machine & delete them



# How to run a django project

1. git clone https://github.com/rnevin97/factory-machinery-tracker.git

2. Switch to git branch feature/product-website

3. First step is to create Virtual environment to setup django
    3.1  Run following commands to setup virtual environment
         python3 -m venv venv
         source venv/bin/activate (activate virtual environemnt)

4. Install all required packages/libraries
    pip install -r requirements.txt

5. run following command from dir where manage.py file is present
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

6. Server will be up running at following address 127.0.0.1:8000

# How to run using docker

open your terminal 
docker-compose up


# Notes

Errors encountered
Locally:
If running locally and experiencing login issues, try opening an new icognito window. It's because Django uses cookies to store session information. 
If your login view and the admin are using the same session cookie, there could be some weird behavior.

Docker:
If you see errors like:

> `sqlite3.OperationalError: duplicate column name: raised_by_id`

You might have stale migrations or an old database file.

To reset:
In terminal
# Stop Docker
docker-compose down

# Remove SQLite DB file
rm db.sqlite3

# Delete old migration files (optional but clean)
rm machinery/migrations/0*.py

# Recreate migrations
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
/////
# How to Run Using Docker

Open your terminal and run:
docker-compose up

# Notes

## Errors Encountered

### Locally

If running locally and experiencing login issues, try opening a new incognito window.  
This happens because Django uses cookies to store session information.  
If your login view and the admin are using the same session cookie, there may be unexpected behavior.

### Docker

If you see errors like:

sqlite3.OperationalError: duplicate column name: raised_by_id

You might have stale migrations or an old database file.

#### To Reset:

1. **Stop Docker**  
   docker-compose down
  
2. **Remove SQLite DB file**  
   rm db.sqlite3

3. **Delete old migration files (optional but clean)**  
   rm machinery/migrations/0*.py

4. **Recreate migrations**  
   docker-compose run web python manage.py makemigrations
   docker-compose run web python manage.py migrate
