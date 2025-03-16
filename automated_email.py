import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Load credentials from environment variables 
sender_email = os.getenv("EMAIL_SENDER")  
receiver_email = os.getenv("EMAIL_RECEIVER") 
smtp_password = os.getenv("EMAIL_PASSWORD")  

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587

# Create the email
msg = MIMEMultipart()
msg['Subject'] = 'Automated Compliance Report'
msg['From'] = sender_email
msg['To'] = receiver_email

# Email body
body = "Please find the attached compliance report."
msg.attach(MIMEText(body, 'plain'))

# Attach the compliance report
report_file = "/home/ubuntu/compliance_report.json"
try:
    with open(report_file, "rb") as f:
        attachment = MIMEApplication(f.read(), _subtype="json")
        attachment.add_header('Content-Disposition', 'attachment', filename="compliance_report.json")
        msg.attach(attachment)
except FileNotFoundError:
    print(f"Error: {report_file} not found.")
    exit(1)

# Send the email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS
        server.login(sender_email, smtp_password)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")
