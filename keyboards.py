from telegram import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
from connectDB import *

def get_contact1():
    con_keyboard = KeyboardButton(text="Nomerni ulashish", request_contact=True)
    custom_keyboard = [[con_keyboard]]
    return ReplyKeyboardMarkup(custom_keyboard, resize_keyboard=True,one_time_keyboard=True)
def inline_callback_region():
    regions = get_region()
    region = []
    t = []
    for x in regions:
        t.append(InlineKeyboardButton(f'{x[1]}', callback_data=f'{x[0]}'))
        if len(t)==2:
            region.append(t)
            t = []
        elif len(regions)-len(region) == 7:
            region.append(t)
            t=[]
    return InlineKeyboardMarkup(region)

def lesson_in():
    link = get_link_lesson()
    l = []
    links=[]
    for x in link:
        l.append(InlineKeyboardButton(f'{x[0]}-dars', callback_data=f'{x[0]}'))
        if len(l)==3:
            links.append(l)
            l=[]
        if len(link)-len(links)*3<3:
            links.append(l)
            l=[]
    return InlineKeyboardMarkup(links)
def menu_keyb():
    main_menu = ReplyKeyboardMarkup([
        [
            'Avtoschool haqida ma\'lumot🚓'
        ],
        [
            'Kerakli dokumentlar📑'
        ],
        [
            'Testlar🧾'
        ],
        [
            'Foydali qo\'llanmalar'
        ],

        [
            'Sozlamalar⚙️'
        ],
    ], resize_keyboard=True,
        # one_time_keyboard=True
    )
    return main_menu
def usefull():
    use = ReplyKeyboardMarkup([
        [
            '️Dasturlar📱'
        ],
        [
            '️Vedio darsliklar📹'
        ],
        [
            '️Ortga⬅'
        ],
    ], resize_keyboard=True,
        # one_time_keyboard=True
    )
    return use

def back():
    back = ReplyKeyboardMarkup([
        [
            '️Ortga⬅'
        ],
    ], resize_keyboard=True,
        # one_time_keyboard=True
    )
    return back

def menu_keyb2():
    main_menu = ReplyKeyboardMarkup([
        [
            'Bizning manzil📍'
        ],
        [
            'Biz bilan aloqa📞'
        ],
        [
            '️Ortga⬅'
        ]
    ], resize_keyboard=True,
        # one_time_keyboard=True
    )
    return main_menu

def setting1():
    setting = ReplyKeyboardMarkup([
        [
            'Akkauntni ko\'rish👁'
        ],
        [
            'Akkauntni o`chirish❌'
        ],
        [
            '️Ortga⬅'
        ]
    ], resize_keyboard=True)
    return setting
def level():
    level = ReplyKeyboardMarkup([
        [
            'A',
            'B',
            'C'
        ],
        [
            'C',
            'D'

        ],
        [
            'BE',
            'CE',
            'DE'
        ],
        [
            '️Ortga⬅'
        ]
    ], resize_keyboard=True,
        # one_time_keyboard=True
    )
    return level
def delete_akk():
    delete_account = [
        [
            InlineKeyboardButton('Ha✅', callback_data='yes'),
            InlineKeyboardButton('Yo`q❌', callback_data='no')
        ]
    ]
    return delete_account



