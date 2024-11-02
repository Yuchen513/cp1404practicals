"""
CP5632 Practical 6
Estimate: 30 minutes
Actual:   minutes
"""

class ProgrammingLanguage:
    def __init__(self,name,typing,reflection,year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing}, {self.reflection}, {self.year}"
