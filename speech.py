import speech_recognition as sr
import notifications

# obtain audio from the microphone
r = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        print('listening...')
        audio = r.listen(source)
    # recognize speech
        print("audio sent...")
    try:
        # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
        output =  r.recognize_google(audio)
        print(f" you said {output}" )
        CONST_requiredKeyword = "interesting"
        if(CONST_requiredKeyword in output):
            print("sending the mail...")
            # FIXME: run the whole script
            notifications.main()
        else:
            print(f"failed to send... {output}")
    except sr.UnknownValueError:
        print("Google could not understand audio")
    except sr.RequestError as e:
        print("Google error; {0}".format(e))
