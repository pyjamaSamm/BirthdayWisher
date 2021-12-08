from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = # Sender's email here
MY_PASSWORD = # Sender's email password here

today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]):data_row for(index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    # pick a random letter
    file_path = f"./letter_templates/letter_{random.randint(1,3)}.txt"

    # replace the name
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg = f"Subject: Happy Birthday!\n\n{contents}"
        )
