
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import os

# Initialize
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Read API key from environment variable
newsapi = os.getenv("NEWS_API_KEY")


# Text-to-speech function
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# Fetch news
def tellNews():
    if not newsapi:
        speak("News API key is missing")
        return

    url = "https://newsapi.org/v2/top-headlines"

    params = {
        "country": "in"
    }

    headers = {
        "X-Api-Key": newsapi
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        if response.status_code == 200:
            articles = response.json().get("articles", [])

            if not articles:
                speak("No news articles found")
                return

            speak("Here are the top five headlines")

            for article in articles[:5]:
                title = article.get("title")

                if title:
                    speak(title)

        else:
            print("News API Error:", response.status_code)
            print(response.text)
            speak("Unable to fetch news")

    except requests.RequestException as e:
        print("News error:", e)
        speak("Please check your internet connection")


# Process commands
def processCommand(c):
    c = c.lower().strip()

    if "open google" in c:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")

    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")

    elif c.startswith("play "):
        song = c.split(" ", 1)[1].strip()

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
            speak("Playing " + song)
        else:
            speak("Sorry, song not found")

    elif "news" in c:
        tellNews()

    elif any(word in c for word in ["stop", "exit", "quit"]):
        speak("Goodbye")
        return False

    else:
        speak("Sorry, I don't understand that command")

    return True


# Main program
if __name__ == "__main__":

    speak("Initializing Jarvis")

    running = True

    while running:
        try:
            # Listen for wake word
            with sr.Microphone() as source:
                print("\nListening for wake word...")

                recognizer.adjust_for_ambient_noise(
                    source,
                    duration=0.5
                )

                audio = recognizer.listen(
                    source,
                    timeout=8,
                    phrase_time_limit=6
                )

            command = recognizer.recognize_google(
                audio,
                language="en-IN"
            )

            print("You said:", command)

            if "jarvis" in command.lower():

                speak("Yes, how can I assist you?")

                # Listen for user command
                with sr.Microphone() as source:
                    print("Listening for command...")

                    recognizer.adjust_for_ambient_noise(
                        source,
                        duration=0.5
                    )

                    audio = recognizer.listen(
                        source,
                        timeout=8,
                        phrase_time_limit=10
                    )

                # Recognize command
                try:
                    command = recognizer.recognize_google(
                        audio,
                        language="en-IN"
                    )

                    print("Command:", command)

                    running = processCommand(command)

                except sr.UnknownValueError:
                    speak("Sorry, please repeat your command")

        except sr.WaitTimeoutError:
            print("No voice detected. Listening again...")
            continue

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Speech recognition error:", e)
            speak("Speech recognition service is unavailable")

        except KeyboardInterrupt:
            print("\nJarvis stopped")
            speak("Jarvis stopped")
            break

        except OSError as e:
            print("Microphone error:", e)
            speak("Please check your microphone")
            break
