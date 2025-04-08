# factory-machinery-tracker

![image](https://github.com/user-attachments/assets/11ba8bd1-d6d7-4858-a0e1-2a812790007b)

![image](https://github.com/user-attachments/assets/6a3094b8-ba5f-419e-87a2-1be8aa65ad8c)

![image](https://github.com/user-attachments/assets/21db995a-2d06-4064-9a4d-a970583fd534)

![image](https://github.com/user-attachments/assets/df01fee6-2174-4dfb-a237-5a5ce1c5898c)

![image](https://github.com/user-attachments/assets/1e0ab332-56a6-41ed-b354-47cf0668fd99)


Testing Machine Page :
1. You can add new Machine through queries at the moment
INSERT INTO machinery_company (id,name,email,phone,job_title) VALUES ('1','TestComapny','test@test.com','123444','manager')

INSERT INTO machinery_machine (id, name , serial_number, importance, status, company_id) VALUES ('1', 'Test Machinery' , 'SERIAL1123', '1', 'Working','1')
2. Now when you load the machines pages, you should be able to see machine & delete them




How to run a django project

1. git clone https://github.com/rnevin97/factory-machinery-tracker.git

2. Switch to git branch feature/product-website

3. First step is to create Virtual environment to setup django
    3.1  Run following commands to setup virtual environment
         python3 -m venv venv
         source venv/bin/activate (activate virtual environemnt)

4. Install all required packages/libraries
    pip install -r requirements.txt

5. run following command from dir where manage.py file is present
    python manage.py runserver

6. Server will be up running at following address 127.0.0.1:8000
