from contestant import Contestant

class Sweepstakes:
        def __init__(self, name):
            self.contestants = {
                "First name": 'First name',
                "Last name": 'Last name',
                "Email Address": '@.com',
                "Registration number": ''
            }
            # self.contestants = {}
            # each item in your dictionary is a key value pair with:
            # unique registration number: Contestant() object


        def register_contestant(self):
            response = input('Would you like to register?')
            self.contestants= response
            print(f'You are now registered! {self.registration_number}')

        def pick_winner(self, contestant):
        # //// should return a contestant object////


        def print_contestant_info(self, contestant):
