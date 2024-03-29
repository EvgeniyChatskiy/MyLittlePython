import smtplib
import yaml
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

with open('./testdata.yaml') as f:
    testdata = yaml.safe_load(f)

from_email = testdata['from_email']
to_email = testdata['to_email']
pass_email = testdata['pass_email']
filename = 'log.txt'
subject = f"report {filename}"
message_body = 'Here is the text with test report'

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

msg.attach(MIMEText(message_body, _subtype='plain'))

with open(filename, 'rb') as f:
    attach = MIMEApplication(f.read(), Name=basename(filename))
    attach['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
    msg.attach(attach)

try:
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    server.login(from_email, pass_email)

    server.sendmail(from_email, to_email, msg.as_string())

    print('The message was sent')
    server.quit()
except Exception as e:
    print(f'Error {str(e)}')
