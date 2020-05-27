# import for the actual sending function
import smtplib

# import for email modules
from email.message import EmailMessage

from string import Template
# similar to the os.path in os library allows us to access the html file
from pathlib import Path

html = Template(Path('index.html').read_text())
# constructing the email
email = EmailMessage()
# print(dir(email))
email['from'] = 'Sirri Glory'
email['to'] = 'sirricelles@gmail.com'
email['subject'] = 'You won One Million dollars'

msg = "Hello this is my first email content. I am testing out my python skills. Python is so cool "

email.set_content(html.substitute(name="Timmy"), 'html')

# sending the email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    # tls is an encryption mechanism to connect securely to the server
    smtp.starttls()
    smtp.login('ztmpython@gmail.com', '3761sirri')
    smtp.send_message(email)
    print('All good Boss!')

# this code could be improved by requesting user name and email.
# carry out validation checks
# catching Exceptions
# write test
