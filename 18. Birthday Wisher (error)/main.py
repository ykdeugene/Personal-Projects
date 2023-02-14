import smtplib
import email_data

gmail = email_data.my_gmail
yahoo = email_data.my_yahoo
pw = email_data.my_password

connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
connection.starttls()
connection.login(user=yahoo, password=pw)
connection.sendmail(from_addr=yahoo, to_addrs=gmail, msg="Hello")
connection.close()
