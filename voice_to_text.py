import speech_recognition as sr

def main():
    r = sr.Recognizer()  # Voice recognizer

    with sr.Microphone() as source:
        # Adjust the voice recognizer for ambient noise to enhance voice recognition accuracy
        r.adjust_for_ambient_noise(source)
        print("Please speak for 5 seconds")

        try:
            audio = r.listen(source, timeout=5)  # Listening time is set to 5 seconds
            print("Converting Now...")

            recognized_text = r.recognize_google(audio)
            # Print the captured spoken words
            print("\nCaptured Word/s: " + recognized_text)

            # Print the converted text
            print("Converted Text: " + recognized_text)

        # Display error if the spoken word is not clear
        except sr.UnknownValueError:
            print("Error: Unclear word/s!")

        # Display error if no spoken word is captured
        except sr.WaitTimeoutError:
            print("Error: No spoken words were captured!")

if __name__ == "__main__":
    main()
