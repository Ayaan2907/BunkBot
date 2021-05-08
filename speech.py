import speech_recognition as sr
from fuzzywuzzy import fuzz # Works on principle of Levenshtein distance
import re #to use split

def checkKeyword(output, keywords):
    print("matching with keywords")
    opList = re.split(' |;|,|\.|\?|\!|\*|\n',output)
    if(opList==0):opList=output
    for i in range(0, len(opList)):
        for j in range(0, len(keywords)):
            score=fuzz.partial_token_set_ratio(opList[i], keywords[j])
            if(score >= 70):
                print(f"keywords matched {opList[i]},{keywords[j]}, with {score} score")
                return 1
            else:
                continue    
    print(f"Keyword missing in {output}")
    return 0

def audioController(keywords):
# OBTAIN AUDIO FROM MICHROPHONE
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print(f"Say something! ")
        audio = r.listen(source, phrase_time_limit=3) #timout=10
        print(f"Audio captured ")
        # FIXME:timeout will wait for input to come and phrase time will select the phrase saied only in that time, use it in try and execute block
    # RECOGNIZE SPEECH
    try:
        # STORING CONVERTED TEXT IN OUTPUT
        output = r.recognize_google(audio).lower()
        print(f"You said --{output}" )
        return(checkKeyword(output, keywords))

    except sr.UnknownValueError:
        print(f"Google could not understand audio")
    except sr.RequestError as e:
        print(f"Network error {0}".format(e))


# if __name__ == "__main__":
