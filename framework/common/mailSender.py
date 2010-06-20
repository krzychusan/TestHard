import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def sendMail(task, mail, text):
    msg = MIMEMultipart('holahole')
    msg['From'] = 'dromaderro@gmail.com'
    msg['To'] = mail
    msg['Subject'] = 'Testhard report on task %s.' % task
    msg.attach(MIMEText(text))
    
    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login('dromaderro@gmail.com', 'qweasdzxc')
    mailServer.sendmail('TestHard', mail, msg.as_string())
    mailServer.close()


if __name__ == "__main__":
    print 'Running test'
    sendMail('Tytul', 'midkun@gmail.com', 'Witam, co tam u pana slychac? \n czesc poraz ostatni. \n Papa')
