from flask import Blueprint, render_template, flash, redirect, url_for, current_app
from flask_mail import Message
from lotusrpg.main.forms import ContactForm
from flask_security import auth_required
from lotusrpg import mail 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html') 

@main.route('/community')
@auth_required()
def community():
    return render_template('community.html')

@main.route('/charity')
def charity():
    return render_template('charity.html')

@main.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')


@main.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        # Gather form data
        name = form.name.data
        sender_email = form.email.data
        subject = form.subject.data
        message_body = form.message.data

        # Create email message
        msg = Message(
            subject=f"New Contact Form Submission: {subject}",
            sender=current_app.config['MAIL_USERNAME'],
            recipients=[current_app.config['MAIL_USERNAME']]
        )
        msg.body = f"From: {name} <{sender_email}>\n\nMessage:\n{message_body}"
        
        # Attempt to send the email
        try:
            mail.send(msg)
            flash("Thank you for reaching out! Your message has been sent.", "success")
        except Exception as e:
            # Optionally log the error e here
            flash("Sorry, there was an error sending your message. Please try again later.", "danger")
        
        return redirect(url_for("main.contact"))
    
    return render_template("contact.html", form=form)
