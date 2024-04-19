import telebot
import sqlite3
from telebot import types

API_TOKEN=''

db = sqlite3.connect('socio_bot.db')

c = db.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS khortytsa(
    chat_id text,
    answerCnt integer,
    answer0 text,
    answer1 text,
    answer2 text,
    answer3 text,
    answer4 text,
    answer5 text,
    answer6 text,
    answer7 text,
    answer8 text
)""")
db.commit()
db.close()

bot = telebot.TeleBot(API_TOKEN)
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
question_cnt = 0

@bot.message_handler(commands=["start"])
def start(m, res=False):
    db1 = sqlite3.connect('socio_bot.db')
    cur = db1.cursor()
    cur.execute(f"SELECT COUNT(*) FROM khortytsa WHERE chat_id LIKE {m.chat.id}")
    queryCnt = cur.fetchone()[0]
    if queryCnt == 0:
        print("New: ", m.chat.id)
        cur.execute(f"INSERT INTO khortytsa VALUES({m.chat.id}, 0, '', '', '', '', '', '', '', '', '')")
        db1.commit()
    bot.send_message(m.chat.id, 'Привет, я здесь, чтобы исследовать портрет потребителя водки Хортиця')
    cur.execute(f"SELECT answerCnt FROM khortytsa WHERE chat_id LIKE {m.chat.id}")
    question_cnt = cur.fetchone()[0]
    if question_cnt == 0:
        new_buttons(["Мужской", "Женский"])
        bot.send_message(m.chat.id, 'Какой у вас пол?', reply_markup=markup)
        print(1)
    elif question_cnt == 1:
        new_buttons(["Да", "Нет"])
        bot.send_message(m.chat.id, 'Вам больше 45 лет?', reply_markup=markup)
        print(2)
    elif question_cnt == 2:
        new_buttons(["Учусь", "Работаю", "Нет"])
        bot.send_message(m.chat.id, 'Вы учитесь или работаете? ', reply_markup=markup)
        print(3)
    elif question_cnt == 3:
        new_buttons(["Да", "Нет"])
        bot.send_message(m.chat.id, 'Вы женаты?', reply_markup=markup)
    elif question_cnt == 4:
        new_buttons(["Да", "Нет"])
        bot.send_message(m.chat.id, 'У вас есть дети?', reply_markup=markup)
    elif question_cnt == 5:
        new_buttons(["Да", "Нет"])
        bot.send_message(m.chat.id, 'Вы пьете в одиночку?', reply_markup=markup)
    elif question_cnt == 6:
        new_buttons(["Да", "Нет"])
        bot.send_message(m.chat.id, ' Вы пьете чаще 4 раз в месяц?', reply_markup=markup)
    elif question_cnt == 7:
        new_buttons(["Да", "Нет"])
        bot.send_message(m.chat.id, 'Ваш доход выше 40 000 рублей на одного члена семьи?', reply_markup=markup)
    elif question_cnt == 8:
        new_buttons(["Да", "Нет"])
        bot.send_message(m.chat.id, 'Вы религиозны? ', reply_markup=markup)
        print(8)
    elif question_cnt == 9:
        new_buttons(['/start'])
        bot.send_message(m.chat.id, 'Опрос уже пройден', reply_markup=markup)
        print(9)
    db1.close()

@bot.message_handler(content_types=["text"])
def handle_text(message):
    db1 = sqlite3.connect('socio_bot.db')
    cur = db1.cursor()
    cur.execute(f"SELECT answerCnt FROM khortytsa WHERE chat_id LIKE {message.chat.id}")
    question_cnt = cur.fetchone()[0]
    print(question_cnt)
    if question_cnt == 0:
        cur.execute(f"""
        UPDATE khortytsa 
        SET answer0 = '{message.text}',
        answerCnt = 1
        WHERE chat_id LIKE {message.chat.id}
    """)
        db1.commit()
        print(1)
        new_buttons(["Да", "Нет"])
        bot.send_message(message.chat.id, 'Вам больше 45 лет?', reply_markup=markup)
    elif question_cnt == 1:
        cur.execute(f"""
                UPDATE khortytsa 
                SET answer1 = '{message.text}',
                answerCnt = 2
                WHERE chat_id LIKE {message.chat.id}
            """)
        db1.commit()
        print(2)
        new_buttons(["Учусь", "Работаю", "Нет"])
        bot.send_message(message.chat.id, 'Вы учитесь или работаете? ', reply_markup=markup)
    elif question_cnt == 2:
        cur.execute(f"""
                UPDATE khortytsa 
                SET answer2 = '{message.text}',
                answerCnt = 3
                WHERE chat_id LIKE {message.chat.id}
            """)
        db1.commit()
        print(3)
        new_buttons(["Да", "Нет"])
        bot.send_message(message.chat.id, 'Вы женаты?', reply_markup=markup)
    elif question_cnt == 3:
        cur.execute(f"""
                UPDATE khortytsa 
                SET answer3 = '{message.text}',
                answerCnt = 4
                WHERE chat_id LIKE {message.chat.id}
            """)
        db1.commit()
        new_buttons(["Да", "Нет"])
        bot.send_message(message.chat.id, 'У вас есть дети?', reply_markup=markup)
    elif question_cnt == 4:
        cur.execute(f"""
                UPDATE khortytsa 
                SET answer4 = '{message.text}',
                answerCnt = 5
                WHERE chat_id LIKE {message.chat.id}
            """)
        db1.commit()
        new_buttons(["Да", "Нет"])
        bot.send_message(message.chat.id, 'Вы пьете в одиночку?', reply_markup=markup)
    elif question_cnt == 5:
        cur.execute(f"""
                UPDATE khortytsa 
                SET answer5 = '{message.text}',
                answerCnt = 6
                WHERE chat_id LIKE {message.chat.id}
            """)
        db1.commit()
        new_buttons(["Да", "Нет"])
        bot.send_message(message.chat.id, ' Вы пьете чаще 4 раз в месяц?', reply_markup=markup)
    elif question_cnt == 6:
        cur.execute(f"""
                UPDATE khortytsa 
                SET answer6 = '{message.text}',
                answerCnt = 7
                WHERE chat_id LIKE {message.chat.id}
            """)
        db1.commit()
        new_buttons(["Да", "Нет"])
        bot.send_message(message.chat.id, 'Ваш доход выше 40 000 рублей на одного члена семьи?', reply_markup=markup)
    elif question_cnt == 7:
        cur.execute(f"""
                UPDATE khortytsa 
                SET answer7 = '{message.text}',
                answerCnt = 8
                WHERE chat_id LIKE {message.chat.id}
            """)
        db1.commit()
        new_buttons(["Да", "Нет"])
        bot.send_message(message.chat.id, 'Вы религиозны? ', reply_markup=markup)
    elif question_cnt == 8:
        cur.execute(f"""
                UPDATE khortytsa 
                SET answer8 = '{message.text}',
                answerCnt = 9
                WHERE chat_id LIKE {message.chat.id}
            """)
        db1.commit()
        new_buttons(['/start'])
        bot.send_message(message.chat.id, 'Спасибо за прохождение опроса!', reply_markup=markup)
        print(8)
    elif question_cnt == 9:
        new_buttons(['/start'])
        bot.send_message(message.chat.id, 'Опрос уже пройден', reply_markup=markup)
        print(9)
    db1.close()


def new_buttons(buttons_text):
    print(len(buttons_text), markup.keyboard.__len__())
    buttons_diff = len(buttons_text) - markup.keyboard.__len__()
    if buttons_diff > 0:
        for i in range(buttons_diff):
            markup.add(types.KeyboardButton(buttons_text[-i - 1]))
    elif buttons_diff < 0:
        for i in range(buttons_diff * -1):
            print('here')
            markup.keyboard.pop()
    for i in range(len(buttons_text)):
        markup.keyboard[i][0] = buttons_text[i]

bot.infinity_polling(none_stop=True, interval=0)
