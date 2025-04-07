from quiz import Question, Animal, Option

arctic_fox = Animal(
    "Песец",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/c41d53da-8b31-4c2b-9011-01cccc81a899.jpg",
)
alpaca = Animal(
    "Альпака",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/7ee94b22-86c4-4ae6-a583-00d4e61ea90d.jpeg",
)
jubngle_cat = Animal(
    "Камышовый кот",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/6d771474-82f9-4f55-b6c5-1034e026fdd4.jpeg",
)
bearded_seal = Animal(
    "Морской заяц",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/0f7ee967-f9a1-4a09-9843-8ad97914139f.jpeg",
)
muskox = Animal(
    "Канадский овцебык",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/5a4c4c52-71f9-475e-8ba9-ed5863e8e6d3.jpeg",
)
tamarin = Animal(
    "Краснорукий тамарин",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/81ba700d-4d46-4c6b-9c5a-a2bd4f76e323.webp",
)
ratel = Animal(
    "Медоед",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/16cb2d06-ecce-4e44-a01c-f6d7ba40be5f.jpeg",
)


nicobar_pigeon = Animal(
    "Никобарский голубь",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/0631b2a3-b94a-447d-a9c3-2b6cc1e2438e.jpeg",
)
ibis = Animal(
    "Священный ибис",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/e6ef3180-8afd-41e2-ae02-a1652edf877b.jpg",
)
bittern = Animal(
    "Большая выпь",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/a9111a05-1d93-4871-989d-c8bbcf1061c7.jpeg",
)
galah = Animal(
    "Розовый какаду",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/47eb38a5-b36f-49c0-bbaa-4b26d4cc7e92.jpeg",
)
pheasant = Animal(
    "Золотой фазан",
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/e5d25474-591c-46ea-96bc-c99cf6d32b78.JPG",
)

q1_opt1 = Option(pheasant, 3, media="./media/golden_pheasant.JPG")
q1_opt2 = Option("Амурский тигр", is_counted=False, media="./media/tiger.JPG")
question_1 = Question(
    "Какое из животных являлось символом китайской императорской власти?\n\n1) Золотой фазан\n2) Амурский тигр",
    [q1_opt1, q1_opt2],
)

q2_opt1 = Option(None, is_counted=False)
q2_opt2 = Option(muskox, 3, media="./media/muskox.JPG")
question_2 = Question(
    "Канадские овцебыки - обладатели самой длинной шерсти (до 90см в области шеи). Как в зоопарке эти огромные животные расчесывают столь обильный шерстяной покров?\n\n1) Это работа смотрителей, овцебыки - дружелюбные животные и позволяют себя расчесывать.\n2) Установлены специальные чесалки, чтобы быки расчесывались самостоятельно.",
    [q2_opt1, q2_opt2],
)

q3_opt1 = Option(nicobar_pigeon, 3, media="./media/nicobar_pigeon.JPG")
q3_opt2 = Option("Викунья", is_counted=False, media="./media/vicugna.JPG")
question_3 = Question(
    "Какие из представителей этих четырех обитателей зоопарка образуют пары на всю жизнь?\n\n1) Никобарский голубь\n2) Викунья",
    [q3_opt1, q3_opt2],
)

q4_opt1 = Option(
    "Кенгуру Беннета", is_counted=False, media="./media/bennet's_wallaby.JPG"
)
q4_opt2 = Option(galah, 3, media="./media/galah.JPG")
question_4 = Question(
    'В Австралии имя этого животного (Galah) значит "дурак" или "клоун" и может относиться к человеку. Какое из этих двух животных носит это имя?\n\n1) Кенгуру Беннета\n2) Розовый Какаду',
    [q4_opt1, q4_opt2],
)
q5_opt1 = Option(ratel, 3, media="./media/ratel.JPG")
q5_opt2 = Option(None, is_counted=False)
question_5 = Question(
    "Медоед известен своим бесстрашием - он не избегает схватки даже со смертельно ядовитыми змеями. Каким образом медоед одерживает победу над ними?\n\n1) Игнорирует укусы, впадает в кому после ядовитого укуса и “оживает” через час.\n2) Полагается на свою ловкость избегая укусов змеи.",
    [q5_opt1, q5_opt2],
)
q6_opt1 = Option(tamarin, 3, media="./media/tamarin.JPG")
q6_opt2 = Option(tamarin, 3)
q6_opt3 = Option(None, is_counted=False)
q6_opt4 = Option(None, is_counted=False)
question_6 = Question(
    "Воспитанием детенышей красноруких тамаринов занимаются самцы группы. В их обязанности входит:\n\n1) Ношение детенышей \n2) Расчесывание \n3) Воспитание \n4) Развлечение",
    [q6_opt1, q6_opt2, q6_opt3, q6_opt4],
)
q7_opt1 = Option(ibis, 3, media="./media/ibis.JPG")
q7_opt2 = Option(None, is_counted=False, media="./media/white_stork.JPG")
question_7 = Question(
    "Какая из этих двух птиц считалась символом египетского бога мудрости?\n\n1) Священный ибис\n2) Белый аист",
    [q7_opt1, q7_opt2],
)
q8_opt1 = Option(None, is_counted=False)
q8_opt2 = Option(alpaca, 3, media="./media/alpaca.JPG")
question_8 = Question(
    "Альпак разводят для стрижки шерсти. Но какие альпаки особенно ценятся за качество своей шерсти?\n\n1) Равнинные\n2) Высокогорные",
    [q8_opt1, q8_opt2],
)
q9_opt1 = Option(arctic_fox, 3, media="./media/arctic_fox.JPG")
q9_opt2 = Option(None, is_counted=False)
question_9 = Question(
    "Песцы иногда организуются в группы с довольно сложным устройством. Например, они могут здороваться друг с другом, но при этом:\n\n1) Воровать друг у друга еду из тайников\n2) Создавать коалиции внутри группы",
    [q9_opt1, q9_opt2],
)
q10_opt1 = Option(None, is_counted=False)
q10_opt2 = Option(bearded_seal, 3, media="./media/bearded_seal.JPG")
question_10 = Question(
    "Свою имя морской заяц получил за:\n\n1) Пугливый характер\n2) Вибрисы, напоминающие заячьи",
    [q10_opt1, q10_opt2],
)

q11_opt1 = Option(None, is_counted=False)
q11_opt2 = Option(bittern, 3, media="./media/bittern.JPG")
question_11 = Question(
    "Как большая выпь издает свой известный низкий “крик”, похожий на далекий гудок парохода?\n\n1) Опускает клюв в воду при крике\n2) Поднимает клюв и раздувает пищевод для большего резонанса",
    [q11_opt1, q11_opt2],
)

q12_opt1 = Option(jubngle_cat, 3, media="./media/jungle_cat.JPG")
q12_opt2 = Option(None, is_counted=False)
question_12 = Question(
    "Камышовый кот, как и другие кошачьи, ночное животное. Как сотрудники зоопарка мотивируют кота выйти днем к посетителям?\n\n1) Показательное дневное кормление\n2) Развлекают кота играми с веревкой",
    [q12_opt1, q12_opt2],
)


questions = [
    question_1,
    question_2,
    question_3,
    question_4,
    question_5,
    question_6,
    question_7,
    question_8,
    question_9,
    question_10,
    question_11,
    question_12,
]
