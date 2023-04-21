from datetime import datetime


class Project:
    def __init__(self, name, start_date, priority, estimate, completion):
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __repr__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        return self.priority < other.priority


