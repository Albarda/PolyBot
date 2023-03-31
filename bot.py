from telegram.ext import Updater, MessageHandler, filters
from utils import search_download_youtube_video
from loguru import logger


class Bot:
    """Base class for Telegram bots."""

    def __init__(self, token):
        """Initialize a new bot instance."""
        self.updater = Updater(token, use_context=True)
        self.updater.dispatcher.add_handler(
            MessageHandler(filters.Filters.text, self._message_handler)
        )

    def start(self):
        """Start polling messages from users. This function never returns."""
        self.updater.start_polling()
        logger.info(f"{self.__class__.__name__} is up and listening to new messages....")
        self.updater.idle()

    def _message_handler(self, update, context):
        """Main messages handler."""
        self.send_text(update, f"Your original message: {update.message.text}")

    def send_video(self, update, context, file_paths):
        """Sends video to a chat."""
        for file_path in file_paths:
            with open(file_path, "rb") as video:
                context.bot.send_video(
                    chat_id=update.message.chat_id,
                    video=video,
                    supports_streaming=True,
                )

    def send_text(self, update, text, quote=False):
        """Sends text to a chat."""
        update.message.reply_text(text, quote=quote)


class QuoteBot(Bot):
    """Bot that can quote user messages."""

    def _message_handler(self, update, context):
        to_quote = True

        if update.message.text == "Don't quote me please":
            to_quote = False

        self.send_text(update, f"Your original message: {update.message.text}", quote=to_quote)


class YoutubeBot(Bot):
    """Bot that can download and send YouTube videos."""

    def _message_handler(self, update, context):
        message_text = update.message.text

        if message_text.startswith("https://www.youtube.com/watch?v="):
            # Download the video from the link and get the file path.
            file_paths = search_download_youtube_video(message_text)

            if file_paths is not None:
                # Send the video to the user.
                self.send_video(update, context, file_paths)
            else:
                # If the download failed, send an error message to the user.
                self.send_text(update, "Sorry, could not download the video.")
        else:
            # If the message is not a YouTube video link, send an error message to the user.
            self.send_text(update, "Please send a valid YouTube video link.")


if __name__ == "__main__":
    with open(".telegramToken") as f:
        _token = f.read().strip()

    my_bot = QuoteBot(_token)
    my_bot.start()
