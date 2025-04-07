import asyncio
from telebot.async_telebot import AsyncTeleBot
from env import token
from logging_ import BotLogger
from telebot.formatting import hlink
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InputMediaPhoto,
    InputFile,
)
from quiz import QuizBase, genResults
from socials import gen_vk_link
from questions_main import questions
from notifications import send_email_notification


quiz = QuizBase("zoo_quiz", questions)
# bot = telebot.TeleBot(token=token)
bot = AsyncTeleBot(token=token)
logger = BotLogger("bot.log")


def gen_markup(options):
    markup = InlineKeyboardMarkup()
    if options == "intro":
        markup.row_width = 1
        markup.add(InlineKeyboardButton("Начать викторину", callback_data="start_quiz"))
    if options == "restart":
        markup.row_width = 1
        markup.add(
            InlineKeyboardButton("Повторить викторину", callback_data="quiz_start")
        )
    if options == 4:

        markup.row_width = 2
        markup.add(
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("4", callback_data="4"),
        )
    if options == 2:
        markup.row_width = 2
        markup.add(
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
        )

    return markup


@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):

    if call.data == "1":
        quiz.set_answer("1")
        quiz.next_question()
        bot.answer_callback_query(call.id, "Your answer is 1")
    if call.data == "2":
        quiz.set_answer("2")
        quiz.next_question()
        bot.answer_callback_query(call.id, "Your answer is 2")
    if call.data == "3":
        quiz.set_answer("3")
        quiz.next_question()
        bot.answer_callback_query(call.id, "Your answer is 3")
    if call.data == "4":
        quiz.set_answer("4")
        quiz.next_question()
        bot.answer_callback_query(call.id, "Your answer is 4")
    if call.data == "quiz_start":
        quiz.reset()
        print("quiz start")

    # if quiz.cur_question < 11:
    #     quiz.cur_question = 11
    if quiz.cur_question < len(quiz):

        cur_question = quiz.get_cur_question()
        media_list = []
        for opt in cur_question.options:
            if opt.media:
                media_list.append(opt.media)
        await bot.send_media_group(
            call.message.chat.id,
            [InputMediaPhoto(InputFile(n)) for n in media_list],
        )
        await bot.send_message(
            call.message.chat.id,
            cur_question,
            reply_markup=gen_markup(len(cur_question.options)),
        )

    else:

        result = genResults(quiz)
        quiz.set_user(
            call.from_user.id,
            call.from_user.first_name,
            call.from_user.username,
            call.from_user.last_name,
            call.from_user.language_code,
        )
        logger.log("info", f"Quiz completed by user {quiz.user['id_']}")
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=InputFile(result.media),
            caption=f"Правильных ответов: {quiz.stats}/{len(quiz)}.\n\nИтак, ваше тотемное животное -- {result.animal}!",
        )
        zoo_link = hlink("ссылке", "https://moscowzoo.ru/about/guardianship")
        vk_link = gen_vk_link(img=result.animal.image_url)
        text = f"Вы можете взять этого обитателя зоопарка под свою опеку! Участие в программе «Клуб друзей зоопарка» — это помощь в содержании наших обитателей, а также ваш личный вклад в дело сохранения биоразнообразия Земли и развитие нашего зоопарка. Узнайте больше по {zoo_link}."
        formatted_link = hlink("Поделиться Вконткте", vk_link)

        await bot.send_message(
            chat_id=call.message.chat.id,
            text=text + "\n\n" + formatted_link,
            parse_mode="HTML",
            reply_markup=gen_markup("restart"),
        )
        # try:
        #     await send_email_notification(
        #         subject="Рузельтаты викторины",
        #         message=result.animal,
        #         user_info=quiz.user,
        #     )
        # except Exception as e:
        #     print(e)


@bot.message_handler(commands=["start", "help"])
async def send_welcome(message):
    logger.log("info", f"Command /start")
    intro_caption = "Приймите участие в викторине об обитателях московского зоопарка и узнайте свое тотемное животное! Цель этой небольшой игры - рассказать о программе опеки животных от Московского Зоопарка. Подробности - в конце викторины."
    await bot.send_photo(
        chat_id=message.chat.id,
        photo=InputFile("./media/logo.jpg"),
        caption=intro_caption,
        reply_markup=gen_markup("intro"),
    )


asyncio.run(bot.polling())
