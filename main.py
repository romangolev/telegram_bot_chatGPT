import openai
import telebot
import os
from dotenv import load_dotenv

load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Set Telegram bot token
bot = telebot.TeleBot(os.getenv("TELEGRAMBOT_API_KEY"))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to ChatGPT! Type anything to get started.")

@bot.message_handler(commands=['hi'])
def send_welcome(message):
    bot.reply_to(message, "Hi there.")

@bot.message_handler(commands=['test'])
def send_welcome(message):
    bot.reply_to(message, "The bot is working now.")

@bot.message_handler(func=lambda message: True)
def chat(message):
    # Send user's message to OpenAI's GPT-3 API
    completion = openai.ChatCompletion.create(
     model="gpt-3.5-turbo", # this is "ChatGPT" $0.002 per 1k tokens
     messages=[{"role": "user", "content": message.text}]
     )

    # Send the AI's response back to the user
    bot.reply_to(message, completion.choices[0].message.content)

bot.polling()