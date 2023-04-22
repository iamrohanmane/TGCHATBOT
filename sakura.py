import asyncio
from setup import chatgpt
import openai
from pyrogram import filters, Client
from textblob import TextBlob

Rohan = Client(name="OpenaiBot",api_id=chatgpt.api_id,api_hash=chatgpt.api_hash)

async def ai(query):
    openai.api_key = chatgpt.openai_api_key
    completion = openai.Completion.create(engine=chatgpt.model, prompt=query, max_tokens=chatgpt.mxtoken, n=1, stop=None,temperature=0.7)
    result = completion.choices[0].text
    return result

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

@Rohan.on_message(filters.command("start") & ~filters.group)
async def main(bot,msg):
    newbie = msg.from_user.id
    await bot.send_message(newbie, "" '👋 Hello ''!\n\n'
                    'My name is sakura. \n'
                    'And I am a telegram AI based chat-bot \n\n'
                    'Belongs to OpenAIs GPT-3 family \n'
                    'Im here to help answer any questions you may have about a variety of topics.\n'
                    'Feel free to ask me anything! ☺️\n\n'
                    'MADE BY : Rohan Mane \n'
                    'Git-Hub Profile : https://github.com/iamrohanmane\n'
                    'Git-Hub Reposotory :https://github.com/iamrohanmane/TGCHATBOT.git\n'
                    'Please leave your feedback @sakura_feedback_bot')
    DEL = await msg.reply(f"Typing🤔.......")
    await asyncio.sleep(3)
    await DEL.delete(10)

@Rohan.on_message(filters.text & ~filters.group)
async def main(bot, msg):
    newbie = msg.from_user.id
    ques = msg.text
    sentiment_score = get_sentiment(ques)
    if sentiment_score < -0.5:
        expression = "😔"
    elif sentiment_score < 0:
        expression = "😕"
    elif sentiment_score == 0:
        expression = "😐"
    elif sentiment_score < 0.5:
        expression = "🙂"
    else:
        expression = "😄"
    chatgpt = await ai(ques)
    await asyncio.sleep(3)
    test = f"`{expression} {guu}`"
    await asyncio.sleep(1)
    await bot.send_message(newbie,test)


Rohan.run()
