# Create your classes here

class Student:

    def __init__(self, first_name, last_name, address):
        self.first_name = self
        self.last_name = last_name
        self.address = address


class Question:

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer


class Exam:

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(new_question):
        self.questions.append(new_question)


    def ask_and_evaluate(self):

        for ask in self.questions:
            response = input("{} > ".format(ask.question))
            if response == ask.correct_answer:
                return True
            return False

    def administer():





