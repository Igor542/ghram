from TOKEN import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

import gh_utils

def start(update, context):
    update.message.reply_text('Hi! Use /help to get a list of commands')

def status(update, context):
    branch = ''
    nargs = len(context.args)
    if nargs == 0:
        branch = 'master'
    elif nargs > 1:
        return help(update, context)
    else:
        branch = context.args[0]

    try:
        s = gh_utils.get_status(branch)
        update.message.reply_text('branch: %s status: %s'%(branch, s))
    except (IndexError, ValueError):
        return help(update, context)


def help(update, context):
    update.message.reply_text('/status [branch]')

def main():

    """Run the bot."""
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    help_handler = CommandHandler('help', help)
    dispatcher.add_handler(help_handler)

    status_handler = CommandHandler('status', status)
    dispatcher.add_handler(status_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
