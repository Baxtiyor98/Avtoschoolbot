from telegram.ext import Updater, CommandHandler,ConversationHandler,\
    CallbackQueryHandler,MessageHandler, Filters
from Conversation import *
def main():
    updater = Updater(token='1944886352:AAFo4NFPwKMOPcqR9k73LuuQnaSK7sFjKNs',use_context = True)
    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            'start': [MessageHandler(Filters.text, start)],
            'fname': [MessageHandler(Filters.text, get_fname)],
            'contact': [MessageHandler(Filters.text, get_contact)],
            'main': [MessageHandler(Filters.contact, message)],
            'main_menu': [CallbackQueryHandler(main_menu)],
            'get_menu': [MessageHandler(Filters.text,get_menu)],
            'use': [MessageHandler(Filters.text,use)],
            'exit': [MessageHandler(Filters.text,exit)],
            'about': [MessageHandler(Filters.text,about)],
            'delete': [CallbackQueryHandler(delete)],
            'video': [CallbackQueryHandler(video)],
            'back_query': [CallbackQueryHandler(back_query)],
        },
        fallbacks=[CommandHandler('start',start)]
    )
    dispatcher.add_handler(conv_handler)
    dispatcher.add_handler(CallbackQueryHandler(inline_callback_region))
    dispatcher.add_handler(CallbackQueryHandler(lesson_in))

    updater.start_polling()
    updater.idle()
main()