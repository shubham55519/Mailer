import os
import smtplib
#import imghdr
from email.message import EmailMessage
import csv

# Create the Environment Variables Named as EMAIL_ADDRESS and EMAIL_PASSWORD having your Email ID and Password .
# For the 2 step Authentication purpose create secured password on :
# https://accounts.google.com/signin/v2/challenge/az?continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&service=accountsettings&osid=1&rart=ANgoxccc1_Or9PHwdTPEMRIshSh15VI38w7-NrjmtEkF9KOGrlVWDpIFGdiK14iUh4xX7UiIY_s42v15GPmTVApTbxIn6EcLrA&TL=AM3QAYYjx-ROHJaL2r61UqYu1toklNCtgjlZ2Cw0gzl2ix-bc62fk9JKY0BZZXMl&flowName=GlifWebSignIn&cid=5&flowEntry=ServiceLogin

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# Path of the CSV File

f = open('C:/Users/ADMIN/Desktop/py/email.csv')
csv_f = csv.reader(f)
next(csv_f)
contacts = []

for row in csv_f:
    key = row[1]
    if key not in contacts:
        contacts.append(row[1])

print (contacts)
msg = EmailMessage()
msg['Subject'] = 'Test Email'
msg['From'] = EMAIL_ADDRESS
msg['To'] = ', '.join(contacts)

msg.set_content('This is a plain text email')

msg.add_alternative("""\
   
<html>
    <head>

    </head>
    <body> <img src="https://pbs.twimg.com/profile_images/1226346039210209280/FptpYmpd_400x400.jpg" height="100" width="100"><br><br>
       
        <hr>
        Hey,<br>
        Hope you are doing well!<br>
        Thank you for showing interest in <b>Automation using Web-Scraping in Python.</b><br>
        We highly recommend you to keep a pen and notebook with wou during the session.The link for the session is given below.<br>
        <b>Please try to join 10 minutes prior to event</b><br><br>
        We hope to see you at:<br>
        Webinar link:<a href="https://meet.google.com/mgs-crdv-tqc"> Join Meeting </a><br>
        Date:<b> 27 June 2020 / Saturday
    </body>
</html>
""", subtype='html')

#with open('C:/Users/ADMIN/Desktop/py/WebScraping.png', 'rb') as f:
    #file_data = f.read()
   # msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='WebScraping.png')    

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)