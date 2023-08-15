from twilio.rest import Client



ACCOUNT_SID = "ACaed4637585721f659c4cca7ee60244e7"
AUTH_TOKEN = "122175a71e04cd6d072f5a3225625320"
TWILIO_NUMBER = "+13148977440"
MY_NUMBER = "+40722733096"



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
