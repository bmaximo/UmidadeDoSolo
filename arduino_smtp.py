import serial
import time
import smtplib
 
USER_GMAIL = 'your.email@gmail.com'
PASSWORD_GMAIL = 'password'

TO = 'barbara.cmaximo@gmail.com'

arduino = serial.Serial('/dev/ttyACM1', 9600)

SUBJECT  = 'Situacao do solo'


def send_email():
    print("Enviando e-mail")
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(USER_GMAIL, PASSWORD_GMAIL)
    header  = 'To:      ' + TO + '\n'
    header += 'From:    ' + USER_GMAIL + '\n'
    header += 'Subject: ' + SUBJECT + '\n'
    print header
    msg = header + '\n' + TEXT + '\n'
    smtpserver.sendmail(USER_GMAIL, TO, msg)
    smtpserver.close()

while True:
    TEXT = arduino.readline()
    print(TEXT)
    send_email()
    time.sleep(60)

