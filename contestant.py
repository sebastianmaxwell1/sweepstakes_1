import smtplib, ssl


class Contestant:
    def __init__(self, first_name, last_name, email, registration_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email
        self.registration_number = registration_number

    def email_winner(self):
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "maxwellsebas@gmail.com"
        receiver_email = "winnerwinnerchickendinner@gmail.com"  # winner's email
        password = input("Type your password and press enter: ")
        message = """\
        Subject: Congratulations!

        You have won our Grand prize sweepstakes!."""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
