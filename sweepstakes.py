class Sweepstakes:
        def __init__(self, name):
            self.dictionary_contestant = {
                "First name": input("Please enter your first name"),
                "Last name": input("Please enter your last name"),
                "Email Address": input("Please enter your email for results"),
                "Registration number": input("Please provide your email")
            }


        def register_contestant(self):
            response = input('Would you like to register?')
            self.dictionary_contestant = response
            print(f'You are now registered! {self.registration_number}')

        def pick_winner(self, contestant):
        # //// should return a contestant object////


        def print_contestant_info(self, contestant):
