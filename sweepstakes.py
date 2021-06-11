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

            def pick_winner(self):
                winner = user_interface.get_random_number(0, len(self.contestants))
                return winner

        def print_contestant_info(self):
            contestant_num = self.pick_winner()
            contestant_info = self.contestants[contestant_num]
            self.name = contestant_info["first_name"]
            print(self.name)

sweepstakes = Sweepstakes()
sweepstakes.register_contestant()
sweepstakes.register_contestant()
sweepstakes.register_contestant()
sweepstakes.print_contestant_info()