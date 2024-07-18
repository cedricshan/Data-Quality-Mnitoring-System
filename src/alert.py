import smtplib
from email.mime.text import MIMEText
from config.config import ALERT_EMAIL

def send_alert(anomalies):
    msg_content = f"Data Quality Anomalies Detected:\n{anomalies}"
    msg = MIMEText(msg_content)
    msg['Subject'] = 'Data Quality Alert'
    msg['From'] = ALERT_EMAIL
    msg['To'] = ALERT_EMAIL

    # Send the email
    with smtplib.SMTP('localhost') as server:
        server.sendmail(ALERT_EMAIL, [ALERT_EMAIL], msg.as_string())
