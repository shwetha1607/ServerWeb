from flask import Flask, render_template, request
from send_mail import SendEmail
from send_sms import SendSMS
from send_whatsapp import SendWhatsApp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
	if request.method=='POST':
		if request.form['sub'] == 'rsub':
			room_num = request.form.get("room")
			min_temp = request.form.get("min")
			max_temp = request.form.get("max")
			print(room_num)

		if request.form['sub'] == 'wsub':
			objW = SendWhatsApp()
			wnum = request.form.get("wnum")
			print(wnum)
			objW.sendText(wnumber, 'This is a test whatsapp message')

		if request.form['sub'] == 'ssub':
			objS = SendSMS()
			sms_num = request.form.get("sms")
			print(sms_num)
			objS.sendSMS(number, 'This is a test sms')

		if request.form['sub'] == 'msub':
			objE = SendEmail()
			email_id = request.form.get("email")
			print(email_id)
			objE.sendMail(email_id, 'Temperature Alert', 'The display reads:', 'static/frame.png')

	return render_template('pagem.html')

if __name__ == '__main__':
	app.run(debug=True, host='localhost', port=5000)