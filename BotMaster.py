#https://groosha.gitbooks.io/telegram-bot-lessons/content/chapter1.h



import config
from telebot import TeleBot
import Bot

id_counter=0
id_list=[]
bots={}

print('start')
bot = TeleBot(config.token)
print('sucsess start')

#




@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    if message.chat.id not in id_list:
        id_list.append(message.chat.id)
        tmp_bot=Bot(bot,message.chat.id,len(id_list))

        bots[message.chat.id]=tmp_bot
        tmp_bot=None

    bots[message.chat.id].get_answer(message.text)



    #if(message.text!='Привет'):
    #    bot.send_message(message.chat.id,'и тебе привет')
    #else:
    #    bot.send_message(message.chat.id, 'start')
    #    bot.send_photo(message.chat.id,open('fl2.jpeg', 'rb'))
    #    bot.send_message(message.chat.id, 'stop')



if __name__ == '__main__':
     bot.polling(none_stop=True)