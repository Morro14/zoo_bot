import random


class QuizBase:
    def __init__(self, name: str, questions: list):
        self.name = name
        self.questions = questions
        self.cur_question = 0
        self.results = []
        self.user = {}
        self.stats = 0

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

    # TODO questions length check

    def next_question(self):
        self.cur_question += 1

    def get_cur_question(self):
        return self.questions[self.cur_question]

    def set_answer(self, value):
        try:

            question = self.questions[self.cur_question]
            option = question.options[int(value) - 1]

            self.results.append(option)

        except IndexError:
            print("Exception: No more questions in the quiz.")

    def reset(self):
        self.results = []
        self.cur_question = 0
        self.stats = 0

    def set_user(self, id_, first_name, username, last_name, language_code):
        self.user = {
            "id_": id_,
            "first_name": first_name,
            "username": username,
            "last_name": last_name,
            "language_code": language_code,
        }


class Question:
    def __init__(self, question: str, options: list):
        self.question = question
        self.options = options

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

    def __repr__(self):
        return f"{self}"


class Animal:
    def __init__(self, name: str, image_url: str = ""):
        self.name = name
        self.image_url = image_url

    def __str__(self) -> str:
        return self.name


def genResults(quiz):

    # all valid options
    all_options = []
    for q in quiz.questions:
        for opt in q.options:
            if opt.is_counted:
                all_options.append(opt)

    # options connected to correct answers
    correct_options = []
    for opt in quiz.results:
        if opt.is_counted:
            correct_options.append(opt)

    weights = []
    for opt in all_options:
        if opt not in correct_options:
            weights.append(0)
        else:
            weights.append(opt.weight)

    # if there are correct answers
    if len(correct_options) != 0:
        result_weighted = random.choices(
            population=[opt for opt in correct_options],
            weights=[opt.weight for opt in correct_options],
            k=1,
        )
    # if there are no correct answers
    else:
        result_weighted = random.choices(
            population=[opt for opt in all_options],
            k=1,
        )
    # correct answers count
    quiz.stats = len(correct_options)
    return result_weighted[0]
