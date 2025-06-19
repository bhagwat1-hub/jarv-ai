import openai
from config import OPENAI_API_KEY
from voice import speak, listen

openai.api_key = OPENAI_API_KEY

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    speak("Hello, I am JARVIS. How can I assist you today?")
    while True:
        query = listen()
        if "exit" in query or "stop" in query:
            speak("Goodbye, sir.")
            break
        elif query:
            reply = chat_with_gpt(query)
            speak(reply)
