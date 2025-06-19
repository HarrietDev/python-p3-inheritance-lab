#!/usr/bin/env python

from user import User

import random

class Teacher(User):
    def __init__(self, first_name, last_name,knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge else [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request",
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]


    def teach(self,topic = None):
        if not self.knowledge:
            return None
        if topic:
            self.knowledge.append(topic)
            return topic
        return random.choice(self.knowledge)
        
my_teacher = Teacher("Nancy","Johns",knowledge=["pipenv install pipenv shell",
    "pytest -x flag to fail fast"])
print(my_teacher.__dict__)
print(my_teacher.knowledge)
print(my_teacher.teach("JavaScript async web request"))
print(my_teacher.teach())

    
