import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("email-id", "password")
# message to be sent
message = "message sent using python"
# sending the mail
s.sendmail("senders_email_id", "recievers_email_id", message)
# terminating the session
s.quit()