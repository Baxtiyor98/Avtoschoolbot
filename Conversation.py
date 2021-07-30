from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ParseMode
from Registratsiya import *
from keyboards import *

def start(update, context):
    if is_logged(update.effective_chat.id):
        print('Main_menu ishladi')
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                                 reply_markup=menu_keyb())
        return 'get_menu'
    else:
        return 'fname'
def get_fname(update, context):
    message = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Assalom alaykum, hurmatli foydalanuvchi, iltimos ro\'yxatdan o\'ting! '
                                              '\nIsm familiyangizni kiriting:')
    return 'contact'
def get_contact(update, context):
    message = update.message.text
    user = Registration(update.effective_chat.id)
    user.update_reg('f_name', message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'{message}! \nIltimos, nomerni ulashish tugmasini bosing' ,
                                 reply_markup = get_contact1())
    return 'main'
def message(update, context):
    user = Registration(update.effective_chat.id)
    contact = update.message.contact
    phone = contact.phone_number
    user.update_reg('phone', phone)
    context.bot.send_message(chat_id=update.effective_chat.id, text='Viloyatingizni tanlang!',
                             reply_markup=inline_callback_region())
    return 'main_menu'

def main_menu(update, context):
    print('Main_menu ishladi')
    query = update.callback_query
    user = Registration(update.effective_chat.id)
    user.update_reg('viloyat', f'{get_region()[int(query.data) - 1][0]}')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Ro\'yxatdan muvaffaqqiyatli o\'tdingiz!')
    context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                             reply_markup=menu_keyb())
    query.message.delete()
    return 'get_menu'
def get_menu(update, context):
    print('Get olindi')
    message = update.message.text
    if message == 'Testlar🧾':
        update.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Level tanlang👇',
                               reply_markup=level())
    if message == 'Kerakli dokumentlar📑':
        update.message.delete()
        context.bot.send_photo(chat_id=update.effective_chat.id,
                               photo=open("C:/Python/Django/Avtoschoolbot/Toifalar.jpg", 'rb'),
                               caption='Haydovchilik guvohnomasi uchun kerak bo\'ladigan hujjatlar👆',
                               reply_markup=back())
    if message == 'Avtoschool haqida ma\'lumot🚓':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Avtoschool haqida ma\'lumot👇',
                                 reply_markup=menu_keyb2())
        return 'about'
    if message == 'Sozlamalar⚙️':
        update.message.delete()
        print('Setting ishladi')
        context.bot.send_message(chat_id=update.effective_chat.id, text='Sozlamalar👇',
                                 reply_markup=setting1())
    if message == 'Foydali qo\'llanmalar':
        update.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id,text='Foydali qo\'llanmalar',
                                 reply_markup=usefull())
        return 'use'

    if message == 'Akkauntni o`chirish❌':
        update.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Akkountingizni o\'chirmoqchimisiz?',
                                 reply_markup=InlineKeyboardMarkup(delete_akk()))
        return 'delete'
    if message == 'Akkauntni ko\'rish👁':
        update.message.delete()
        tg_id = update.effective_chat.id
        print(get_acc())
        for user in get_acc():
            if user[4]==tg_id:
                context.bot.send_message(chat_id=update.effective_chat.id, text='Sizning akkountingiz\n'
                                        f'Foydalanuvchi: {user[1]}\nNomer: {user[2]}\nTelegram id: {user[4]}')
    if message == '️Ortga⬅':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                                 reply_markup=menu_keyb())
        return 'get_menu'
def about(update, context):
    message = update.message.text
    if message == 'Biz bilan aloqa📞':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Bosh mutaxassis: Shohruh Olimjonov\n+99894 333 00 95\n+99833 914 95 95\n'
                                                                        'O\'rgatuvchi mutaxassis: Jahongir Elliyev\n+99893 248 07 70\n'
                                                                        'Bosh mutaxassis yordamchisi: Saidjon Dilmiyev\n+99891 263 95 95\n+99899 010 95 95\n')
    if message == 'Bizning manzil📍':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Manzil: Qashqadaryo viloyati G\'uzor shahri\nTinchlik mahallasi.\n'
                                                                        'Mo\'ljal: Sho\'rtan markaziy stadioni ro\'parasi.')
    if message == '️Ortga⬅':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                                 reply_markup=menu_keyb())
        return 'get_menu'
def use(update, context):
    message = update.message.text
    if message == '️Vedio darsliklar📹':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Darslardan birini tanlang👇:',
                                 reply_markup=lesson_in())
        return 'video'
    if message == '️Dasturlar📱':
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Biz siz haqingizda qayg\'uramiz. Shu bois ba\'zi '
                                                                            f'kitoblarni tavsiya etamiz. Quyidagi linklar orqali yuklab olishingiz mumkin👇:')
        for i in get_link():
            context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f'Tavsiya etiladi:\n{str(i)}')
    if message == 'Vedio darsliklar📹':
        pass
    if message == '️Ortga⬅':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Kerakli bo`limni tanlang👇',
                                 reply_markup=menu_keyb())
        return 'get_menu'

def video(update, context):
    query = update.callback_query
    context.bot.send_message(chat_id=update.effective_chat.id,text=f'{get_link_lesson()[int(query.data)-1][1]}')
    return 'back_query'
def back_query(update, context):
    query = update.callback_query
    query.bot.send_message(chat_id=update.effective_chat.id, text='Ortga⬅',
                                 reply_markup=back())
    return 'use'

def delete(update, context):
    query = update.callback_query
    tg_id = update.effective_chat.id
    if query.data == 'no':
        query.message.delete()
        context.bot.send_message(chat_id=update.effective_chat.id, text='Siz bilan yana birgamiz☺️\n Asosiy menyu',
                                 reply_markup=menu_keyb())
        return 'get_menu'
    if query.data == 'yes':
        delete_acc(tg_id)
        if not is_logged(tg_id):
            query.message.delete()
            query.message.reply_text(text='Siznning akkauntingiz o\'chirildii️!')
            return 'start'
