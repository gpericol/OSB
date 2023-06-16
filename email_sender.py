import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import config

class EmailSender:
    @staticmethod
    def send_email(subject, message, receiver_emails):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = config.SENDER_EMAIL
        msg['To'] = ', '.join(receiver_emails)

        with open(config.HEADER_IMAGE_PATH, 'rb') as image_file:
            image = MIMEImage(image_file.read())

        image.add_header('Content-ID', '<header_image>')
        msg.attach(image)

        html_message = f'''
            <html>
                <head>
                    <style>
                        .cve_card {{
                            padding: 10px;
                        }}
                        h2 {{
                            text-align: center;
                        }}
                        .cve_id {{
                            font-weight: bold;
                            font-size: 15px;
                        }}
                        .popular {{
                            background-color: #FFCCCC;
                        }}
                        .footer {{
                            background-color: #333333;
                            color: #ffffff;
                            padding: 10px;
                            text-align: center;
                        }}
                    </style>
                </head>
                <body>
                    <img src="cid:header_image" alt="Header Image" style="width:100%;"><br>
                    <div>
                        {message}
                    </div>
                    <div class='footer'>
                        <p>Another beautiful day!</p>
                    </div>
                </body>
            </html>
        '''

        msg.attach(MIMEText(html_message, 'html'))

        with smtplib.SMTP(config.SMTP_SERVER, config.SMTP_PORT) as server:
            server.starttls()
            server.login(config.SMTP_USERNAME, config.SMTP_PASSWORD)
            server.send_message(msg)
