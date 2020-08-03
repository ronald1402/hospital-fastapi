import mysql.connector
import datetime

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Zicare_dev",
  database="zicareDB"
)

cursor = db.cursor()
sql = """
CREATE TABLE `patient` (
  `patient_id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `username` varchar(20) NOT NULL ,
  `password` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `dob` date DEFAULT NULL,
  `gmt_created` date NOT NULL,
  `gmt_updated` date NOT NULL,
  UNIQUE(username)
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
"""
cursor.execute(sql)

print("Table patient successfully created")

cursor = db.cursor()
sql = "INSERT INTO patient (username, password, name, email, dob, gmt_created, gmt_updated) VALUES (%s, %s, %s, %s, " \
      "%s, %s, %s) "
current_time = datetime.datetime.now()

val = ("Zicaredev", "hashpassword", "developer", "developer@zicare.id", current_time, current_time, current_time)
cursor.execute(sql, val)

db.commit()

print("{} data successfully added".format(cursor.rowcount))
