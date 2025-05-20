import smtplib
from email.message import EmailMessage

# Email content
msg = EmailMessage()
msg['Subject'] = 'Hello from Python'
msg['From'] = 'amiel.padasay004@gmail.com'
msg['To'] = 'amieljohn.padasay@gsfe.tupcavite.edu.ph'
msg.set_content('This is a test email sent from Python!')

# SMTP setup and send
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login('amiel.padasay004@gmail.com', 'uuye ugda doxg vhob')  # Use App Password, NOT your regular Gmail password
    smtp.send_message(msg)

print("Email sent successfully!")