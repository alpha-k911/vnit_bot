import telebot
import pyjokes
from tabula import read_pdf
from tabula import read_pdf_with_template
from telebot import types
import json
import pymysql as sq




TOKEN = "829593578:AAHlUspWbFlV287wEzXHAr3ZONjyp-EjCsQ"
bot = telebot.TeleBot(TOKEN)

chat_ids = set()

print("\n[+] Working........")

#help
@bot.message_handler(commands=["help"])
def help_command(message):
    # print(chat_ids)
    chat_ids.add(message.chat.id)
    bot.send_message(message.chat.id,"List of Commands:\n/start\n/pun\n/help\n/set_dept\n/BT17CSE030")


#start
@bot.message_handler(commands=["start"])
def start_command(message):
    print("received")
    bot.send_message(message.chat.id,"Greetings! my dear creat0r....")


#pun
@bot.message_handler(commands=["pun"])
def pun_command(message):
    # print()
    print(message.text[-2:])
    bot.send_message(message.chat.id,pyjokes.get_joke())

# pp = "dcn"
#mon_r1
@bot.message_handler(commands=["schedule"])
def scheduler(message):
    markup = telebot.types.InlineKeyboardMarkup()#row_width=2
    mon = telebot.types.InlineKeyboardButton("MON",callback_data=2)
    tue = telebot.types.InlineKeyboardButton("TUE",callback_data=3)
    wed = telebot.types.InlineKeyboardButton('WED',callback_data=4)
    thurs = telebot.types.InlineKeyboardButton('THURS',callback_data=5)
    fri = telebot.types.InlineKeyboardButton('FRI',callback_data=6)
    markup.add(mon,tue)
    markup.add(wed,thurs,fri)
    bot.send_message(message.chat.id, "Choose the day....", reply_markup=markup)
    # bot.callback_query_handler(schedule_callback)

# @bot.answer_callback_query(callback_query_id=ca)

# @bot.callback_query_handler(lambda call: call.data in [2,3,4,5,6])
@bot.callback_query_handler(lambda call: call.data in ["2","3","4","5","6"])
def schedule_callback(call):
    day = call.data
    print(type(call.data))
    print(call.data)
    markup = telebot.types.InlineKeyboardMarkup()  # row_width=2
    r1 = telebot.types.InlineKeyboardButton("R1", callback_data="1"+day)
    r2 = telebot.types.InlineKeyboardButton("R2", callback_data="2"+day)
    r3 = telebot.types.InlineKeyboardButton("R3", callback_data="3"+day)
    r4 = telebot.types.InlineKeyboardButton('R4', callback_data="4"+day)
    # thurs = telebot.types.InlineKeyboardButton('R5', callback_data=5)
    # fri = telebot.types.InlineKeyboardButton('FRI', callback_data=6)
    markup.add(r1,r2)
    markup.add(r3,r4)
    kb = types.InlineKeyboardMarkup()
    cid = call.message.chat.id
    mid = call.message.message_id
    # bot.send_message(call.message.chat.id, "Choose batch....", reply_markup=markup)
    # bot.edit_message_text(call.message.chat.id, "Choose batch....", reply_markup=markup)
    bot.edit_message_text("Choose Batch", cid, mid, reply_markup=markup)

    # if call.data == "CSE":
    # foo(cid,mid,kb,day)


@bot.callback_query_handler(lambda call: len(call.data) == 2)
def foo(call):
    kb = types.InlineKeyboardMarkup()
    cid = call.message.chat.id
    mid = call.message.message_id
    day = call.data[1]
    batch = "R" + call.data[0]
    ll = ""
    db = sq.connect("localhost", "nomad", "nomad", "CSE")
    cursor = db.cursor()
    sql = "select * from "+batch
    try:
        cursor.execute(sql)
        res = cursor.fetchall()
        for row in res:
            id = row[0]
            time = row[1]
            sub = row[int(day)]
            ll = ll + "{time: <7} {sub: <5}\n".format(time=time, sub=sub)
            print(ll, sep=" ")
    except Exception as e:
        print("err")
        print(e)
        ll = "Error"
        # print(message.text[-2:])
    bot.edit_message_text(ll, cid, mid, reply_markup=kb, parse_mode='Markdown')
    # bot.send_message(message.chat.id,ll)


'''
@bot.message_handler(func=lambda message: False) #cause there is no message
def saturday_message():
    now = datetime.now()
    me = bot.get_me()+
    if (now.date().weekday() == 5) and (now.time() == time(8,0)):
        bot.send_message(me.id, 'Wake up!')


#replying same message
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)
'''

@bot.message_handler(commands=["set_dept"])
def setdept(message):
    markup = telebot.types.ReplyKeyboardMarkup()#row_width=2
    itembtn2 = telebot.types.KeyboardButton('ECE')
    itembtn1 = telebot.types.KeyboardButton("CSE")
    itembtn3 = telebot.types.KeyboardButton('EEE')
    itembtn4 = telebot.types.KeyboardButton('CIVIL')
    itembtn5 = telebot.types.KeyboardButton('MME')
    itembtn6 = telebot.types.KeyboardButton('MINING')
    itembtn7 = telebot.types.KeyboardButton('ARCHI')
    markup.add(itembtn1)
    markup.add( itembtn2, itembtn3)
    markup.add(itembtn4, itembtn5, itembtn6,itembtn7)
    bot.send_message(message.chat.id, "Select your Dept.", reply_markup=markup)

'''
@bot.message_handler(commands=["set_dept"])
def set_dept(message):
    markup = telebot.types.InlineKeyboardMarkup()#row_width=2
    itembtn2 = telebot.types.InlineKeyboardButton("ECE",callback_data="ECE")
    itembtn1 = telebot.types.InlineKeyboardButton("CSE",callback_data="CSE")
    itembtn3 = telebot.types.InlineKeyboardButton('EEE',callback_data="EEE")
    itembtn4 = telebot.types.InlineKeyboardButton('CIVIL',callback_data="CIVIL")
    itembtn5 = telebot.types.InlineKeyboardButton('MME',callback_data="MME")
    itembtn6 = telebot.types.InlineKeyboardButton('MINING',callback_data="MINING")
    itembtn7 = telebot.types.InlineKeyboardButton('ARCHI',callback_data="ARCHI")
    markup.add(itembtn1)
    markup.add( itembtn2, itembtn3)
    markup.add(itembtn4, itembtn5, itembtn6,itembtn7)
    # bot.send_message(message.chat.id, "Select your Dept.", reply_markup=markup)
    # markup = types.ReplyKeyboardRemove(selective=True)
    bot.send_message(message.chat.id, "Setting your Department.......", reply_markup=markup)
    # bot.send_message(message.chat.id,a)
#
@bot.callback_query_handler(func=lambda call: True)
def set_dept_callback(call):
    kb = types.InlineKeyboardMarkup()
    cid = call.message.chat.id
    mid = call.message.message_id
    # if call.data == "CSE":
    bot.edit_message_text("Setting up your Dept. as **"+call.data+"** in database", cid, mid, reply_markup=kb, parse_mode='Markdown')
'''

@bot.message_handler(regexp="BT17CSE0[0-9][0-9]")
def cse(message):
    with open('../data/cse226.template_777.json', 'r') as fp:
        obj = json.load(fp)
    a = []
    for i in range(len(obj)):
        p = []
        p.append(obj[i]["y1"])
        p.append(obj[i]["x1"])
        p.append(obj[i]["y2"])
        p.append(obj[i]["x2"])
        a.append(p)
    z = message.text[-2:]
    k = int(z) + 146
    print(k)
    df = read_pdf('../data/cse.pdf', pages=k, area=a, multiple_tables=True, guess=False)
    name = df[6][2][0]
    enroll = df[6][5][0]
    bot.send_message(message.chat.id,name + "\n" + enroll + '\n')
    df = read_pdf('../data/cse.pdf', pages=k, area=a[3], guess=False,
                  pandas_options={'names': ['Code', 'Course', 'Credits', 'Grade']})
    for i in range(len(df)):
        d = "Code: " + df['Code'][i] + "\n" + "Course: " + df['Course'][i] + '\n' + "Credits: " + str(
            df['Credits'][i].item()) + "\n" + "Grade: " + df['Grade'][i]
        bot.send_message(message.chat.id,d + '\n')
    df = read_pdf('../data/cse.pdf', pages=k, area=a[0], guess=False, pandas_options={'header': None})
    cg = df[6][1]
    sg = df[3][1]
    c_cre = df[7][3]
    s_cre = df[3][3]
    s_cre = s_cre[5:]
    c_cre = c_cre[5:]
    print(s_cre + c_cre + sg + cg)
    bot.send_message(message.chat.id,"Semester Credits: " + s_cre + "\nTotal Credits: " + c_cre)
    bot.send_message(message.chat.id,'SGPA: ' + sg + '\nCGPA: ' + cg)


#replying same message

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    # js = message
    bot.reply_to(message, "I didn't get....")
    bot.send_message(message.chat.id,"List of Commands:\n/start\n/pun\n/help\n/set_dept\n/BT17CSE030")




# bot.polling()
#abc
bot.polling(none_stop=True)
