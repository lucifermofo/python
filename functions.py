import wikipedia

def defination(update,context):
    update.message.reply_text("Finding Defination.. Please Wait")
    print("XXX")
    data = ''
    if len((update.message.text).split(' ')) == 2:
        term = update.message.text.split(' ')[1]
    else:
        term = str(update.message.text).replace('/defination','')
    print(term)
    print("XXX")
    try:
        data = wikipedia.summary(term)
    except wikipedia.exceptions.PageError as e:
        print("Such a Defination Not Found")
        update.message.reply_text("No Such Defination Found ! ")  
    except wikipedia.exceptions.DisambiguationError:
        print("Topic Too Vague, did you mean ?")
        options = wikipedia.search(term)
        msg = " ".join(options)
        to_return = "Topic Too Vague, Did You Mean? "+msg
        update.message.reply_text(to_return)
    update.message.reply_text(data)



