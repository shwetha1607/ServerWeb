from twilio.rest import Client
from config import Twilio

class SendWhatsApp:

	def __init__(self):
		self.waObj = Twilio()
		self.account_sid = self.waObj.account_sid
		self.auth_token = self.waObj.auth_token
		self.client = Client(self.account_sid, self.auth_token)
		self.sandboxNum = self.waObj.sandboxNum

	def sendText(self, numbers, messageBody):

		number = 'whatsapp:+91' + str(numbers)
		print(number)

		message = self.client.messages.create(
			body=messageBody,
			from_= self.sandboxNum,
            to=number
        )

		print(message.sid)
		