import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re
import csv

email_user = 'xyz@gmail.com'
# sender email address

email_password = 'ABC123'
# sender email password for login purpose
# error will be raised if account has 2 factor authentication enabled
# read 'readme.md' file to know how to avoid it


subject = 'Test'
# your subject goes here

msg = MIMEMultipart()
msg['From'] = email_user
msg['Subject'] = subject
body = 'This is a test mail'
#your message goes here

msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

# sending mails to all emails listed in .csv file

email_data = csv.reader(open('emails.csv'))
# add your own .csv file here if you want
# or you can just add your emails in 'emails.csv' file attached.

email_pattern= re.compile("^.+@.+\..+$")
for row in email_data:
  if( email_pattern.search(row[0]) ):
    del msg['To']
    msg['To'] = row[0]
    try:
      server.sendmail(email_user, [row[0]], msg.as_string())
    except smtplib.SMTPException:
      print("An error occured.")
server.quit()