import telebot


def send_message(message_id, telegram_id, answer):
    bot = telebot.TeleBot('986722664:AAEx7v_gw8gZvKS7VEZojP2P5JdKfBmoOEQ')
    bot.send_message(telegram_id, answer, reply_to_message_id=message_id)

