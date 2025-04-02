from quiz import Question, Animal, Option

arctic_fox = Animal("Песец")
alpaca = Animal("Альпака")
jubngle_cat = Animal("Камышовый кот")
bearded_seal = Animal("Морской заяц")
muskox = Animal("Канадский овцебык")
tamarin = Animal("Краснорукий тамарин")
ratel = Animal("Медоед")


nicobar_pigeon = Animal("Никобарский голубь")
ibis = Animal("Священный ибис")
bittern = Animal("Большая выпь")
galah = Animal("Розовый какаду")
pheasant = Animal("Золотой фазан")

q1_opt1 = Option(pheasant, 3, media="./media/golden_pheasant.JPG")
q1_opt2 = Option("Амурский тигр", is_counted=False, media="./media/tiger.JPG")


question_1 = Question(
    "Какое из животных являлось символом китайской императорской власти?\n\n1) Золотой фазан\n2) Амурский тигр",
    [q1_opt1, q1_opt2],
)
q2_opt1 = Option(alpaca, 3)
q2_opt2 = Option(alpaca, 0)

question_2 = Question(
    "Альпаки знамениты своей шерстью. Но какие альпаки особенно ценятся за качество шерсти?\n\n1) Высокогорные\n2) Равнинные",
    [q2_opt1, q2_opt2],
)

q3_opt1 = Option(nicobar_pigeon, 3)
q3_opt2 = Option(galah, 3)
question_3 = Question(
    "Какие из представителей этих четырех обитателей зоопарка образуют пары на всю жизнь?\n\n1) Никобарский голубь\n2) Обыкновенный павлин\n3) Розовый какаду\n4) Бурый медведь",
    [],
)

questions = [question_1]
