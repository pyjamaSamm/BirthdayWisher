# BirthdayWisher

Project Name : Birthday Wisher

Author : Gulafsha Ahmed

Language : Python

This Birthday Wisher automatically generates a birthday wish for the receiver and sends it via electronic mail using SMTP(Simple Mail Transfer Protocol). This project makes use of datetime, pandas, random and smtplib.

main.py : performs the functionality of the project. It finds the current date and check against the list of receiver's birth date in birthdays.csv for birthday and if it matches, an electronic mail is sent using one of the letters present in letter_templates.

In main.py, MY_EMAIL and MY_PASSWORD must be initialised with sender's email ID and password respectively.

birthdays.csv needs to be updated with possible receiver's name, email ID, birthyear in yyyy,mm,dd format.

letter_templates have various templates which can be modified. More templates can be added too. In the letters, the sender needs to add sender's name in signature.
