class Worker:

    def __init__(self, name, title, hapinessPercent):
        self.name = name
        self.title = title
        self.hapinessPercent = hapinessPercent

    def display_status(self):
        print(
            f'{self.title} {self.name} shows hapiness level of {self.hapinessPercent} percent.')
