import telebot
from env import token
from logging_ import BotLogger
from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InputMediaPhoto,
    InputFile,
)
from quiz import QuizBase
from questions_main import questions


quiz = QuizBase("zoo_quiz", questions)
bot = telebot.TeleBot(token=token)
logger = BotLogger("bot.log")


def gen_markup(button_num):
    markup = InlineKeyboardMarkup()
    if button_num == 4:

        markup.row_width = 2
        markup.add(
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
            InlineKeyboardButton("3", callback_data="3"),
            InlineKeyboardButton("4", callback_data="4"),
        )
    if button_num == 2:
        markup.row_width = 2
        markup.add(
            InlineKeyboardButton("1", callback_data="1"),
            InlineKeyboardButton("2", callback_data="2"),
        )
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "1":
        quiz.set_answer("1")
        bot.answer_callback_query(call.id, f"Your answer is 1")
    if call.data == "2":
        quiz.set_answer("2")
        bot.answer_callback_query(call.id, "Your answer is 2")
    if call.data == "3":
        quiz.set_answer("3")
        bot.answer_callback_query(call.id, "Your answer is 3")
    if call.data == "4":
        quiz.set_answer("4")
        bot.answer_callback_query(call.id, "Your answer is 4")

    if quiz.cur_question != len(quiz):
        quiz.next_question()
        cur_question = quiz.get_cur_question()
        bot.send_message(
            call.message.chat.id,
            cur_question,
            reply_markup=gen_markup(len(cur_question.options)),
        )
        bot.send_media_group(
            call.message.chat.id,
            [InputMediaPhoto(InputFile("./media/golden_pheasant.JPG"))],
        )


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    logger.log("info", f"Команда /start")
    cur_question = quiz.get_cur_question()
    bot.reply_to(message, "Quiz start!")
    bot.send_message(
        message.chat.id,
        quiz.get_cur_question(),
        reply_markup=gen_markup(len(cur_question.options)),
    )
    media_list = []
    for opt in cur_question.options:
        media_list.append(InputMediaPhoto(InputFile(opt.media)))
    bot.send_media_group(message.chat.id, media_list)


# @bot.message_handler(func=lambda message: True)
# def message_handler

bot.infinity_polling()
