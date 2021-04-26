# Presenting OCassistant (Online Classes Assistant) the helper/proxy maker  of our online classes

## AIM
Automating the replies on calling our name in meetings and notifying us about the call

## Steps
1. First understanding how to send notifications ***EMAIL/MESSAGE*** (push notifications are not helpfull)
2. Then understanding voice recognition techniques
3. Learn web automations to automute/unmute
4. Finally integrate everything


## Requirements
- For email `python smtplib` will be required.
- Now for speech recognition and related stuff you need
    1. `speechRecognition`
    2. `pyttsx3`
    3. `pyAudio`
- For counts `time` is required
> Note: for automation step is a TODO
## Done/Todo
### Done
- Recognizing voice and chechking for desired Keyword
- On keyword detection sending email using the passed parameters.
### Todo
- Using web automation controlling the mute/unmute actions
- On keword detections perform mute
- In unmute status play a recorded reply
- Mute back

## Installation 
- Clone the repo
- `pip3 install requirements.txt`
- Enter the directory ` cd OCassistant`

***CHANGE SENDER_EMAIL PASSWORD AND RECIPIENT_EMAIL TO YOURS THEN ONLY RUN IT***
> Note: The password is not the gmail password it should be [gmailAppPassword](https://support.google.com/accounts/answer/185833?hl=en). 
- Run `python3 index.py`

## Refrences
