from twilio.rest import Client
import os


ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
TWILIO_NUMBER = os.environ['TWILIO_NUMBER']
MY_NUMBER = os.environ['MY_NUMBER']



class NotificationManager:


    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)


    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER
        )

        print(message.sid)
