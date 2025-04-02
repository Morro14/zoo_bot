class QuizBase:
    def __init__(self, name: str, questions: list):
        self.name = name
        self.questions = questions
        self.cur_question = 0
        self.results = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur_question < len(self.questions):
            value = self.questions[self.cur_question]
            self.cur_question += 1
            return value
        else:
            raise StopIteration

    def __len__(self):
        return len(self.questions)

    def next_question(self):
        self.cur_question += 1

    def get_cur_question(self):
        return self.questions[self.cur_question]

    def set_answer(self, value):
        question = self.questions[self.cur_question]
        option = question.options[int(value) - 1]
        self.results.append(option)


class Question:
    def __init__(self, question: str, options: list, attachments: list = []):
        self.question = question
        self.options = options
        self.attachments = attachments

    def __str__(self) -> str:
        return self.question


class Option:
    def __init__(self, animal, weight: int = 0, is_counted=True, media=None):
        self.animal = animal
        self.weight = weight
        self.is_counted = is_counted
        self.media = media

    def __str__(self) -> str:
        return f"Animal: {self.animal}, answer wieght: {self.weight}."


class Animal:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str:
        return self.name
