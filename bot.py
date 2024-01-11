from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

mental_health_bot = ChatBot("MentalHealthBot")

trainer = ChatterBotCorpusTrainer(mental_health_bot)

trainer.train('chatterbot.corpus.english')

trainer.train([
"Hey there. I've been feeling a bit down lately, and I'm not sure how to handle it."

"I'm really sorry to hear that you're feeling this way. It's important to talk about it. What's been going on?"

 "I don't know, it just feels like everything is overwhelming. I'm stressed about work, and I can't seem to find joy in things I used to enjoy."

"I'm here to listen. It sounds like you're going through a tough time. Have you been able to pinpoint any specific reasons behind your stress at work or the lack of joy in your activities?"

"Work has been piling up, and I feel like I can't keep up with it all. And even when I have free time, I'm just not motivated to do anything."

"That sounds challenging. It's understandable to feel overwhelmed when there's a lot on your plate. Have you considered talking to someone at work about your workload or finding ways to prioritize tasks?"

 "I thought about it, but I don't want to seem incompetent. And it's not just work; it's like a cloud of negativity hanging over everything."

"It's okay to ask for help, and expressing your concerns doesn't make you incompetent. Everyone faces challenges, and seeking support is a sign of strength. Have you thought about talking to friends, family, or even a mental health professional about what you're going through?"

 "I haven't really talked to anyone about it. I guess I'm afraid they won't understand or that they'll judge me."

"It's common to feel that way, but opening up to someone you trust can be a crucial step in getting the support you need. People who care about you often want to help. If you're not comfortable talking to someone close to you, consider reaching out to a mental health professional. They are trained to provide guidance and support without judgment."

"Yeah, maybe that's a good idea. I just don't want to burden anyone with my problems."

"It's important to remember that your feelings are valid, and seeking support is not a burden. Friends, family, and professionals are there to help, and sharing your struggles can actually strengthen your relationships. Taking care of your mental health is an important part of overall well-being."

"You're right. I'll think about reaching out to someone. Thanks for listening."

"You're welcome. Remember, you're not alone, and there are people who care about you. If you ever need to talk or explore more options, don't hesitate to reach out. Taking care of your mental health is a brave and important step."

])    

print("MentalHealthBot: Hello! How can I help you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    else:
       print(f"MentalHealthBot{ mental_health_bot.get_response(user_input)}")  

     