import urllib.request
import urllib.parse
from config import TextLocal

class SendSMS:
	def __init__(self):
		self.smsObj = TextLocal()
		self.apiKey = self.smsObj.apiKey
		
	def sendSMS(self, numbers, message):
		print(type(numbers))
		print(numbers)
		data = urllib.parse.urlencode({
	    	'apikey': self.apiKey, 
	    	'numbers': numbers,
	    	'message': message, 
	    	'test': True
	    })
		data = data.encode('utf-8')
		print('Attempt to send')
		print(data)
		request = urllib.request.Request("https://api.textlocal.in/send/?")
		f = urllib.request.urlopen(request, data)
		fr = f.read()
		print(fr)
