import smtplib


from_name = 'Testrun'
from_addr = 'youremailhere@gmail.com'
to_name = 'Testresult'
to_addr = 'someemail@email.com'
subject = 'Test Email'
msg = 'Hello World'
message = """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""

message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg)
# Credentials (if needed)
username = 'youremailhere@gmail.com'
password = 'somepassword'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 