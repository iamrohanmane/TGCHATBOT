# Importing necessary modules
import asyncio
from setup import keys
import openai
from pyrogram import filters, Client

# Creating a Pyrogram client instance
Rohan = Client(name="OpenaiBot",api_id=keys.api_id,api_hash=keys.api_hash)

# An async function to interact with OpenAI API and get response for the user's input
async def ai(query):
    # Setting OpenAI API key
    openai.api_key = keys.openai_api_key
    # Creating a completion object by passing the user input as prompt to OpenAI API
    completion = openai.Completion.create(engine=keys.model, prompt=query, max_tokens=keys.mxtoken, n=1, stop=None,temperature=0.7)
    # Extracting the response from the completion object
    result = completion.choices[0].text
    return result

# Pyrogram event handler to greet the user when they start a private chat with the bot
@Rohan.on_message(filters.command("start") & ~filters.group)
async def main(bot,msg):
    newbie = msg.from_user.id
    # Sending a welcome message to the user
    await bot.send_message(newbie, "" '👋 Hello ''!\n\n'
                    'My name is Sakura Yamuchan. \n'
                    'And I am a telegram AI based chat-bot \n\n'
                    'Belongs to OpenAIs GPT-3 family \n'
                    'Im here to help answer any questions you may have about a variety of topics.\n'
                    'Feel free to ask me anything! ☺️\n\n'
                    'MADE BY : Rohan\n'
                    'Git-Hub Profile : https://github.com/iamrohanmane\n'
                    'Git-Hub Reposotory : https://github.com/iamrohanmane/TGCHATBOT\n'
                    'Please leave your feedback @cosmic_89_bot')
    DEL = await msg.reply(f"Typing🤔.......")
    await asyncio.sleep(3)
    await DEL.delete(10)

# Pyrogram event handler to process the user's message and send back the response from OpenAI API
@Rohan.on_message(filters.text & ~filters.group)
async def main(bot, msg):
    newbie = msg.from_user.id
    # Extracting the user's message
    ques = msg.text
    print(ques)
    # Calling the ai() function to get response from OpenAI API
    keys = await ai(ques)
    await asyncio.sleep(3)
    print(keys)
    # Wrapping the response inside backticks for better visual clarity
    test = f"{keys}"
    await asyncio.sleep(1)
    # Sending the response back to the user
    await bot.send_message(newbie,test)

# Starting the Pyrogram client
Rohan.run()
