from http import server
import smtplib
import random
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('pshirole2555@gmail.com',"olqvlthbigrwruze")
otp = random.randrange(100000,1000000)
message = "otp to login to your account is" + str(otp)
tosend = input("Enter your email id :")
server.sendmail("pshirole2555@gmail.com",tosend, message)
server.quit()

iscorrectotp = int(input("Enter your otp :"))
if (iscorrectotp ==otp):
    print("OTP Verified")
else :
    print("Invalid OTP")
