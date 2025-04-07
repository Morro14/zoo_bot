import urllib.parse
import requests
import urllib

title = urllib.parse.quote("Программа опеки от Московского зоопарка")
comment = urllib.parse.quote(
    "Узнайте больше о программе опеки, а также поучаствуйте в викторине, чтобы узнать свое тотемное животное!"
)

img = urllib.parse.quote(
    "https://storage.moscowzoo.ru/storage/647edc2a70bb5462366280fc/images/animals/3d4b82db-4161-421c-8f50-902b0f3b0240.jpg"
)
bot_link = urllib.parse.quote("https://web.telegram.org/k/#@my_zoo_quiz_bot")


vk_link = f"https://vk.com/share.php?url={bot_link}&image={img}&title={title}&comment={comment}"


def gen_vk_link(bot_link=bot_link, img=img, title=title, comment=comment):
    vk_link = f"https://vk.com/share.php?url={bot_link}&image={img}&title={title}&comment={comment}"
    return vk_link
