import wikipediaapi
import pyttsx3

wiki = wikipediaapi.Wikipedia(language='en', user_agent='VoiceAssistantProject/1.0 (contact: youremail@example.com)')
voice = pyttsx3.init()

topic = input("Enter a topic: ")
page = wiki.page(topic)

if page.exists():
    summary = page.summary[:500]
    print(summary)
    voice.say(summary)
    voice.runAndWait()
else:
    print("Sorry, no page found for that topic.")
