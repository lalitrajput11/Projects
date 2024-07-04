import telebot
from datetime import datetime
import logging

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = "7161330441:AAHniFjfs3hmOYVnsCaG6_1mcKaNPsM0MOA"
bot = telebot.TeleBot(TOKEN)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Handler for the /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Path to your local GIF file
    gif_path = '/home/lalitrajput/python_programs/Pandas/Bots/Pkp.gif'
    
    try:
        # Open the GIF file
        with open(gif_path, 'rb') as gif_file:
            # Send the welcome message with media
            bot.send_chat_action(message.chat.id, 'upload_photo')  # Action to indicate bot is uploading photo
            bot.send_document(message.chat.id, gif_file, caption="Welcome to dark_cheveyoBot! Use /help to see available commands.")
            logging.info(f"Sent welcome message to {message.chat.id}")
    except Exception as e:
        logging.error(f"Error sending welcome message: {e}")

# Handler for the /help command
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "/start - Start dark_cheveyoBot\n"
        "/help - Show help\n"
        "/info - Get information\n"
        "/status - Get status update\n"
        "/time - Get current time\n"
        "/datascience - Get data science resources"
    )
    bot.reply_to(message, help_text)
    logging.info(f"Handled /help command from {message.chat.id}")

# Handler for the /info command
@bot.message_handler(commands=['info'])
def send_info(message):
    bot.reply_to(message, "This is a simple Telegram bot created for demonstration purposes.")
    logging.info(f"Handled /info command from {message.chat.id}")

# Handler for the /status command
@bot.message_handler(commands=['status'])
def send_status(message):
    bot.reply_to(message, "All systems are operational!")
    logging.info(f"Handled /status command from {message.chat.id}")

# Handler for the /time command
@bot.message_handler(commands=['time'])
def send_time(message):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bot.reply_to(message, f"The current time is: {now}")
    logging.info(f"Handled /time command from {message.chat.id}")

# Handler for the /datascience command
@bot.message_handler(commands=['datascience'])
def send_data_science_resources(message):
    resources = (
        "Here are some useful data science resources:\n"
        "1. [Data Science Portfolio-KaggleDataset](https://t.me/DataPortfolio)\n"
        "2. [Programming for Data Science_365](https://t.me/data_science_365)\n"
        "3. [Machine Learning books and papers](https://t.me/Machine_learn)\n"
        "4. [Next-Gen Data Scientists](https://t.me/nextgendatascientists)\n"
        "5. [Data Science AI Project](https://t.me/pythonspecialist)\n"
    )
    bot.reply_to(message, resources, parse_mode='Markdown')
    logging.info(f"Handled /datascience command from {message.chat.id}")

# Handler for unrecognized commands
@bot.message_handler(func=lambda message: True)
def handle_invalid_command(message):
    bot.reply_to(message, "Invalid command. Use /help to see the list of available commands.")
    logging.info(f"Handled invalid command from {message.chat.id}")

# Start the bot
try:
    logging.info("Bot is polling...")
    bot.polling()
except Exception as e:
    logging.error(f"Error in bot polling: {e}")

