import smtplib
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
#must be here

smtp_object.ehlo()
print(smtp_object.starttls())
#password = input('what is your password?:')
#import getpass
email = input('email: ')
password = 'iklrbgoxajnjbyej'
smtp_object.login(email,password)

from_address = email
to_address = input('recieving email address')
subject = input('enter the subject line:')
message = input('enter the body of the message:')
msg = "subject: "+subject+'\n'+message
smtp_object.sendmail(from_address, to_address, msg)
