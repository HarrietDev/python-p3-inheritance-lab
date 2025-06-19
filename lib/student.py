#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name,knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge else []
    
    def learn(self,new_knowledge):
        if isinstance (new_knowledge,str):
            self.knowledge.append(new_knowledge)
        return new_knowledge
    
s1 = Student("jane","Doe",["pipenv install pipenv shell"])
s1.learn("pytest -x flag to fail fast")
print(s1.knowledge)