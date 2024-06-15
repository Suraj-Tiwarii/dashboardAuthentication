# Dashboard_authentication
The dashboard authentication project utilizes Flask, ReactJS, and MySQL to manage user registration and login functionalities. The application validates user inputs during registration and securely stores user data in a MySQL database. For authentication, it retrieves stored user credentials from MySQL and verifies login attempts. Upon successful authentication, users are redirected to a dashboard interface where they can access personalized content or features. The project emphasizes data security and user experience, ensuring robust validation mechanisms for input data integrity and secure handling of sensitive user information. Overall, it integrates frontend and backend technologies to create a seamless user authentication and dashboard navigation experience within a web application framework.


## Getting Started

## Starting ReactJS Application

1. **At First Terminal, Navigate to Project Director:**
   ```bash
   cd dashboardAuthentication
   npm install
   npm start

   
## Setting up MySQL
1. **At Second Terminal Follow these Steps:**
  ```bash
   docker pull mysql
   docker run --name my-mysql-container -e MYSQL_ROOT_PASSWORD=india@123 -d -p 3306:3306 mysql
   docker exec -it my-mysql-container mysql -uroot -p
   CREATE DATABASE registration;
   USE registration;
   CREATE TABLE users (
      id INT AUTO_INCREMENT PRIMARY KEY,
      username VARCHAR(50) NOT NULL,
      email VARCHAR(100) NOT NULL UNIQUE,
      password VARCHAR(100) NOT NULL,
      img BLOB);
 ```

## Setting Up MySQL Configuration
1) Open `backend/config.py` using a text editor like Vim and edit the following:
```python
host = ""        # Replace with your MySQL container IP address
user = "root"    # Assuming your MySQL user is root
password = ""    # Replace with your MySQL root password
db = "registration"  # Replace with your MySQL database name
```


## At third terminal, Run Flask Application
python3 main.py

