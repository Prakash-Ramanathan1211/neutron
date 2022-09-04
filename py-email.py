import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email():
    message = Mail(
        from_email='jetsigma22@gmail.com',
        to_emails='prashprakash1211@gmail.com',
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>easy bro</strong>')
    try:
        sg = SendGridAPIClient('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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))