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
from telebot import asyncio_filters
from quiz import QuizBase, genResults
from socials import gen_vk_link
from questions import questions
from notifications import send_email_notification, send_email_feedback
from telebot.states import State, StatesGroup
from telebot.types import ReplyParameters

from telebot.states.asyncio.context import StateContext
from telebot.asyncio_storage import StateMemoryStorage

state_storage = StateMemoryStorage()
quiz = QuizBase("zoo_quiz", questions)
bot = AsyncTeleBot(token=token, state_storage=state_storage)
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
        feedback_info = "Чтобы оставить отзыв, введите команду /feedback"
        formatted_link = hlink("Поделиться Вконткте", vk_link)

        await bot.send_message(
            chat_id=call.message.chat.id,
            text=text + "\n\n" + feedback_info + "\n\n" + formatted_link,
            parse_mode="HTML",
            reply_markup=gen_markup("restart"),
        )

        send_email_notification(
            subject="Рузельтаты викторины",
            message=result.animal,
            user_info=quiz.user,
        )


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


# feedback
class FeedbackState(StatesGroup):
    text = State()


@bot.message_handler(commands=["feedback"])
async def request_feedback(message, state: StateContext):
    await state.set(FeedbackState.text)
    logger.log("info", f"Command /feedback")
    await bot.send_message(
        message.chat.id,
        "Пожалуста, поделитесь своими замечаниями по работе бота",
        reply_parameters=ReplyParameters(message_id=message.message_id),
    )


@bot.message_handler(state=FeedbackState.text)
async def recieve_feedback(message, state: StateContext):
    await bot.send_message(
        message.chat.id,
        "Отзыв получен.",
        reply_parameters=ReplyParameters(message_id=message.message_id),
    )
    logger.log("info", f"User has left feedback")
    await state.add_data(text=message.text)
    send_email_feedback("feedback", message.text)
    await state.delete()


bot.add_custom_filter(asyncio_filters.StateFilter(bot))

from telebot.states.asyncio.middleware import StateMiddleware

bot.setup_middleware(StateMiddleware(bot))

asyncio.run(bot.polling())
