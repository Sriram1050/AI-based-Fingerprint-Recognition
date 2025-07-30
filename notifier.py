from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, RECEIVER_NUMBER

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_success_message():
    message = client.messages.create(
        body="✅ Access Granted: Fingerprint matched.",
        from_=TWILIO_NUMBER,
        to=RECEIVER_NUMBER
    )
    print("Success message sent:", message.sid)

def send_alert_message():
    message = client.messages.create(
        body="❌ ALERT: Unauthorized fingerprint access detected!",
        from_=TWILIO_NUMBER,
        to=RECEIVER_NUMBER
    )
    print("Alert message sent:", message.sid)
