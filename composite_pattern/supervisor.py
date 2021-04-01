class Supervisor:

    def __init__(self, name, title, hapinessPercent):
        self.name = name
        self.title = title
        self.hapinessPercent = hapinessPercent
        self.employees = []

    def display_status(self):
        print(
            f'{self.title} {self.name} shows hapiness level of {self.hapinessPercent} percent.')
        for employee in self.employees:
            employee.display_status()

    def add_employee(self, employee):
        self.employees.append(employee)
