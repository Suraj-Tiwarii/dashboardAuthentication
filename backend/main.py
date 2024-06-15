from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
from flask_bcrypt import Bcrypt
from flask_mysqldb import MySQL
import MySQLdb
from config import host,user,password,db

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.secret_key = "xyzsdfg"
# MySQL configurations
app.config["MYSQL_HOST"] = host  
app.config["MYSQL_USER"] = user  
app.config["MYSQL_PASSWORD"] = password  
app.config["MYSQL_DB"] = db  
mysql = MySQL(app)


@app.route("/api/register", methods=["POST"])
# Maintaing single Responsiblity Principle
def register_user():
    try:
        mesage = ""
        if (
            request.method == "POST"
            and "username" in request.form
            and "password" in request.form
            and "email" in request.form
        ):
            userName = request.form["username"]
            password = request.form["password"]
            email = request.form["email"]
            img_data = None
            if "img" in request.files:
                img = request.files["img"]
                img_data = img.read()

            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute("SELECT * FROM users WHERE email = % s", (email,))

            account = cursor.fetchone()
            if account:
                mesage = "Account already exists !"
            else:
                cursor.execute(
                    "INSERT INTO users VALUES (NULL, %s, %s, %s,%s)",
                    (userName, email, hashed_password, img_data),
                )

                mysql.connection.commit()

                mesage = "You have successfully registered !"
        elif request.method == "POST":
            mesage = "Please fill out the form !"
        return jsonify(mesage=mesage)
    except Exception as e:
        return jsonify({"error": "Failed to register user", "details": str(e)}), 500


@app.route("/api/login", methods=["POST"])
def login_user():
    try:
        message = ""
        if (
            request.method == "POST"
            and "email" in request.json
            and "password" in request.json
        ):
            email = request.json["email"]
            password = request.json["password"]
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

            # Fetch user data from database
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            user_data = {}

            if user and bcrypt.check_password_hash(user["password"], password):

                user_data = {
                    "id": user["id"],
                    "email": user["email"],
                    "username": user["username"],
                    "img": base64.b64encode(user["img"]).decode("utf-8"),
                }

                message = "Login successful!"
                # Send the JSON response to the React frontend
                response = {"message": message, "user": user_data}
                return jsonify(response)
            else:
                # User doesn't exist or incorrect credentials
                message = "Login failed. Please check your email and password."
                return jsonify({"error": message}), 401
        else:
            message = "Please fill out the form!"
            return jsonify({"error": message}), 400
    except Exception as e:
        # Handle exceptions
        return jsonify({"error": "Failed to process request", "details": str(e)}), 500


if __name__ == "__main__":
    app.run("127.0.0.1", 8900, debug=True)
