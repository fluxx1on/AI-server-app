from django.core.mail.backends.base import BaseEmailBackend
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class SendgridBackend(BaseEmailBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sg = SendGridAPIClient(api_key=settings.SENDGRID_API_KEY)

    def send_messages(self, email_messages):
        for email_message in email_messages:
            message = Mail(
                from_email=email_message.from_email,
                to_emails=email_message.to,
                subject=email_message.subject,
                html_content=email_message.body,
            )
            self.sg.send(message)