import smtplib
import os
import email
import schedule
import datetime

def script():
    server = smtplib.SMTP('smtp.test.com')
    server.login('username@test.com', 'password')
    msg = email.message.EmailMessage()
    recipients = ['recipient1@test.com', 'recipient2@test.com']
    for recipient in recipients:
        msg['To'] = recipient
        msg['Subject'] = 'Daily Report'
        msg.set_content('This is a daily report from Brainnest.')
        report_files = os.listdir('ReportsPath')
        for file in report_files:
            with open('ReportsPath/' + file, 'rb') as f:
                file_data = f.read()
                file_name = f.name
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
        # Send the message
        server.send_message(msg)
    server.quit()
  
schedule.every().day.at("08:00").do(script)
logfile = open("log.txt", "w")
while True:
    schedule.run_pending()
    logfile.write("Daily report sent at: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    logfile.close()
