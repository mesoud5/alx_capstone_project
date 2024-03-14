from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'mesoudtemam5@gmail.com'
app.config['MAIL_PASSWORD'] = 'ivmu dnaz foos ivue'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


def get_reply_message(name, email, message):
    return f"Hi Mesoud,\n\nYou've received a message from {name} ({email}):\n\n{message}\n\nBest regards,\nYour Flask App"
@app.route('/submit_form', methods=['GET','POST'])
#@app.route('/', methods=['GET', 'POST'])
def submitform():
    if request.method == 'POST':
        # Retrieve data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Create a message object for the user
        user_msg = Message("HEY", sender='mesoudtemam5@gmail.com', recipients=[email])
        user_msg.body = f"Hi {name},\n\nThanks for reaching out! I've received your message and may be i will get back to you. In the meantime, keep calm and code on!\n\nBest regards,\nMesoud"
        
        # Send the email to the user
        mail.send(user_msg)

        # Create a message object for the sender
        sender_msg = Message("New Message Received", sender='mesoudtemam5@gmail.com', recipients=['mesoudtemam5@gmail.com'])
        sender_msg.body = get_reply_message(name, email, message)
        
        # Send the email to the sender
        mail.send(sender_msg)

        return render_template('contact.html')
    return render_template('contact.html')




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/skills')
def skills():
    return render_template('skills.html')
@app.route('/projects')
def projects():
    return render_template('projects.html')


if __name__ == "__main__":
    app.run(debug=True)
