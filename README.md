## Flask CRUD MySQL

### Step to run the application

1. Clone the application

```
  git clone
```

2. Create a virtual environment

```
  python -m virtualenv venv
```

4. Activate the virtual environment

```
  .\venv\Scripts\activate
```

3. Install the ```.whl``` extension package

```
  pip install mysqlclient-1.4.6-cp38-cp38-win32.whl
```

4. Install the other libraries

```
  pip install -r requirements.txt
```

5. Create a ```.env``` file and set:

```MYSQL_USER``` ```MYSQL_HOST``` ```MYSQL_PORT``` ```MYSQL_PASSWORD```

6. Initialize MySQL Service

  6.1. Create the database

  ```SQL
    CREATE DATABASE <NAME>
  ```
  
  6.2. Create the table *contacts*

  ```SQL
    CREATE TABLE contacts (
      _id INT AUTO_INCREMENT,
      fullname VARCHAR(255)
      phone VARCHAR(255)
      email VARCHAR(255)
      PRIMARY KEY (_id)
    );
  ```