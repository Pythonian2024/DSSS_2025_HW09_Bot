from typing import Final

from telegram import Update

from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import torch
from transformers import pipeline


TOKEN:Final = '7750968307:AAGKCThNmvwqmueqc_zXt9zR16LhbLIi9tI'
BOT_USERNAME:Final ='@Pythonian91Bot'



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello, this is DSSS_2024_HW-09 BOT!, How on earth I can serve you Sir! ')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('For Help Contact the Nearest Police Station ')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Still in Process of Customization ')

pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0", 
torch_dtype=torch.bfloat16, device_map="auto")

def handle_response(text: str) -> str:
    processed: str=text.lower()

    if 'hello' in processed:
        return 'Hooola!'

    if 'how are you' in processed:
        return 'I am preparing for the exam at the moment,so I am bussy'

    print('To LLM....')   
    # prompt = f"User: {processed}\nBot:"
    prompt= f"""below is an instruction that describes a task, 
    write a response that appropriately complete the request "

    ##instruction:
    {processed}

    ## Response:
    """
    outputs = pipe(prompt, max_new_tokens=100, do_sample=True,
     temperature=0.7, top_k=50, top_p=0.95)
    # return 'I do not understand'
    return outputs[0]["generated_text"]


async def handle_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text: str = update.message.text      

    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type =='group':
        if BOT_USERNAME in text:
            new_text: str = text.replace ( BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',start_command))
    app.add_handler(CommandHandler('custom',start_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)


    print('Polling...')
    app.run_polling(poll_interval=3)






    #C:\Users\abalh\AppData\Local\Temp\pip-install-vithiybp\numpy_84499a44225f4d50b07ae6b46348bc2c\.mesonpy-xh3azkxs\meson-private\sanitycheckc.exe