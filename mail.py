from flask import Flask
# import flask_mail
# from flask_mail import Mail, Message
import flask_mail
app =Flask(__name__)
mail=flask_mail.Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'p------e@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = flask_mail.Mail(app)

@app.route("/")
def index():
   msg = flask_mail.Message('Hello Flask', sender = 'pandaskee@gmail.com', recipients = ['sarojpanda63@gmail.com', 'sarojpanda6311@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)