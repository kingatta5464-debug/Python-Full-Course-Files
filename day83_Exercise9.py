import win32com.client

names = ["Atta", "Amna", "Ayesha", "Rubina", "Zainab", "Emaan", "Hashaaam", "Hashim"]
speaker = win32com.client.Dispatch("SAPI.SpVoice")

for name in names:
    print(f"Shoutout to {name}")
    speaker.Speak(f"Shoutout to {name}")


# import pyttsx3


# l = ["Atta", "Amna", "Ayesha", "Rubina", "Zainab", "Emaan", "Hashaam", "Hashim"]

# engine = pyttsx3.init(driverName="sapi5")  # For Windows
# engine.setProperty("rate", 150)  # Speed (default is ~200)
# engine.setProperty("volume", 1.0)  # Volume (0.0 to 1.0)

# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[1].id)  # Choose a female/male voice

# for i in l:
#     engine.say(f"Shoutout to {i}")
#     print(f"Shoutout to {i}")
# engine.runAndWait()
