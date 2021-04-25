import speech_recognition as sr
import time as t

# obtain audio from the microphone
def audioController(CONST_requiredKeyword0, CONST_requiredKeyword1):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        tic = t.perf_counter()
        print(f"Say something! --in { tic:0.2f} seconds")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        toc = t.perf_counter()
        # recognize speech
        print(f"Audio captured... --in {toc - tic:0.2f} seconds")
    try:

        tic = t.perf_counter()
        output =  r.recognize_google(audio)
        toc = t.perf_counter()
        print(f"You said -- {output} --in {toc - tic:0.2f} seconds" )
        # CHECKING THE REQUIRED WORD
        if(CONST_requiredKeyword0 in output or CONST_requiredKeyword1 in output):
            return 1
        elif ("stop" in output):
            return 0
        else:
            print(f"Keyword missing in {output}")
    except sr.UnknownValueError:
        print(f"Google could not understand audio")
    except sr.RequestError as e:
        print(f"Google error; {0}".format(e))

# if __name__ == "__main__":