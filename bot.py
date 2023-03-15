from telegram.ext import Updater, MessageHandler, filters
from utils import search_download_youtube_video
from loguru import logger


class Bot:

    def __init__(self, token):
        # create frontend object to the bot programmer
        self.updater = Updater(token, use_context=True)

        # add _message_handler as main internal msg handler
        self.updater.dispatcher.add_handler(MessageHandler(filters.text, self._message_handler))

    def start(self):
        """Start polling msgs from users, this function never returns"""
        self.updater.start_polling()
        logger.info(f'{self.__class__.__name__} is up and listening to new messages....')
        self.updater.idle()

    def _message_handler(self, update, context):
        """Main messages handler"""
        self.send_text(update, f'Your original message: {update.message.text}')

    def send_video(self, update, context, file_path):
        """Sends video to a chat"""
        context.bot.send_video(chat_id=update.message.chat_id, video=open(file_path, 'rb'), supports_streaming=True)

    def send_text(self, update: object, text: object, quote: object = False) -> object:
        """Sends text to a chat"""
        # retry https://github.com/python-telegram-bot/python-telegram-bot/issues/1124
        update.message.reply_text(text, quote=quote)


class QuoteBot(Bot):
    def _message_handler(self, update, context):
        to_quote = True

        if update.message.text == 'Don\'t quote me please':
            to_quote = False

        self.send_text(update, f'Your original message: {update.message.text}', quote=to_quote)


class YoutubeBot(Bot):
    def _message_handler(self, update, context):
        # get the user's message text
        message_text = update.message.text

        # check if the message is a YouTube video link
        if message_text.startswith('https://www.youtube.com/watch?v='):
            # download the video from the link and get the file path
            file_path = search_download_youtube_video(message_text)

        else:
            #if the message is not a YouTube video link, send an error message to the user
            self.send_text(update, 'Please send a valid YouTube video link.')
            if file_path is not None:
            # send the video to the user
                self.send_video(update, context, file_path)
            else:
            # if the download failed, send an error message to the user
                self.send_text(update, 'Sorry, could not download the video.')


    def send_video(self, update, context, file_paths):
        """Sends video to a chat"""
        for file_path in file_paths:
            context.bot.send_video(chat_id=update.message.chat_id, video=open(file_path, 'rb'), supports_streaming=True)


if __name__ == '__main__':
    with open('.telegramToken') as f:
        _token = f.read().strip()

    my_bot = QuoteBot(_token)
    my_bot.start()
