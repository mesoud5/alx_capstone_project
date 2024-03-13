from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask import render_template_string
import logging

app = Flask(__name__)
app.secret_key = '0944331587'

# Configuration for Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mesoudtemam9@gmail.com'
app.config['MAIL_PASSWORD'] = 'Muaz@123'
app.config['MAIL_DEFAULT_SENDER'] = 'mesoudtemam9@gmail.com'

mail = Mail(app)

# Setup logging
logging.basicConfig(filename='app.log', level=logging.INFO)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    try:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Validate email format
        if not validate_email(email):
            raise ValueError('Invalid email address')

        # Send email to the user
        user_msg = Message(subject='Thank You for Contacting Us!',
                           recipients=[email],
                           body=render_template_string('email_template.txt', name=name))

        # Send email to your inbox
        admin_msg = Message(subject='New Contact Form Submission',
                            recipients=['mesoudtemam9@gmail.com'],
                            body=f'Name: {name}\nEmail: {email}\nMessage: {message}')

        mail.send(user_msg)
        mail.send(admin_msg)
        flash('Your message has been sent successfully!', 'success')
        logging.info(f'Message sent successfully to {email}')
    except Exception as e:
        flash(f'An error occurred while sending the message: {str(e)}', 'error')
        logging.error(f'Error occurred: {str(e)}')

    return redirect(url_for('contact'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

def validate_email(email):
    # Implement email validation logic
    # You can use a library like email-validator or regex
    # For simplicity, you can just check for the presence of '@'
    return '@' in email

if __name__ == "__main__":
    app.run(debug=True)
