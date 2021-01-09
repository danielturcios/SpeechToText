import speech_recognition as sr
import time

r = sr.Recognizer()

keywords = [("google", 1), ("hey google", 1)]

source = sr.Microphone()


def callback(recognizer, audio):
    # this is called from the background thread

    try:
        print("Say \"Hey Google!\" to begin...")
        speech_as_text = recognizer.recognize_sphinx(audio)
        print(speech_as_text)

        if "google" in speech_as_text or "hey google":
            recognize_main()

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}.".format(e))


def recognize_main():
    print("Listening for audio...")
    r.adjust_for_ambient_noise(source)
    audio_data = r.listen(source)
    print("you said: " + r.recognize_google(audio_data))


def start_recognizer():
    r.listen_in_background(source, callback)
    time.sleep(100)


start_recognizer()