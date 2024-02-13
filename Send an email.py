import getpass
import smtplib

host = "smtp-gmail.com"
port = 587
from_email = "qorzubek394@gmail.com"
to_email = "orzubek.gamariddinov83@gmail.com"
password = getpass.getpass("Enter Password: ")

message = """ Kamariddinov Orzubek 
Hi 


Sending emails in Python

Thanks."""
smtp = smtplib.SMTP(host, port)
status_code, response = smtp.ehlo()
print(f"[*] Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"[*] Starting TLs connection: {status_code} {response}")

status_code, response = smtp.login(from_email, password)
print(f"[*] Loggin in: {status_code} {response}")

smtp.sendmail(from_email, to_email, message)
smtp.quit()
