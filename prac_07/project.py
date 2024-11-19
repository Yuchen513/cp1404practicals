"""
CP5632 Practical 7
"""

import datetime

class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost}, "
                f"completion: {self.percentage}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def is_complete(self):
        return self.completion_percentage == 100