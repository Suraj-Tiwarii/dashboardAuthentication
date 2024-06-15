# Project Name

Brief description of your project.

## Getting Started

### Starting ReactJS Application

1. **At First Terminal, Navigate to Project Director:**
   ```bash
   cd dashboardAuthentication
   npm install
   npm start

   
### Setting up MySQL Configuration
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


### Backend Configuration
### Edit MySQL Configuration:
### Open backend/config.py using a text editor like Vim.
host = ""  # Replace with your MySQL container IP address
user = "root"       # Assuming your MySQL user is root
password = ""  # Replace with your MySQL root password
db = "registration"  # Replace with your MySQL database name


## Run Flask Application
python3 main.py

