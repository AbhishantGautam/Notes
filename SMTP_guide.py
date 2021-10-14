'''
-- SMTP : simple mail transfer protocol
-- sender------------------------------->post-office 1----------->post-office 2--------------->mailbox of reciever
   (abhishantgautam10@gmail.com)        (gmail server)           (yahoo server)               (hello@yahoo.com)
-- smtp is the postman that takes the mail/letter from sender goes through all processes in post offices and deliver to reciever.
-- location of email provider smtp server: gmail: "smtp.gmail.com"
-- TLS : transport layer security : way of securing our connection to the email server(mail is encrypted when transfering it)
'''

import smtplib
connection = smtplib.SMTP("smtp.gmail.com")#to skip "connection.close()" write : "with smtplib.SMTP("smtp.gmail.com") as connection:"
connection.starttls()
connection.login(user="abhishantgautam10@gmail.com", password="your_password")
message = "subject : Hello \n \n this is a mail sent by smtplib module in python"
connection.sendmail(
    from_addr="abhishantgautam10@gmail.com",
    to_addrs="hello@yahoo.com",
    msg=message
)
connection.close()

#if there is an error, check your email privacy settings
