> THE README IS NOT UP TO DATE
# Presenting OCassistant (Online Classes Assistant) the helper/proxy maker  of our online classes
## AIM
Automating the replies on calling our name in meetings and notifying us about the call

## Steps/Learning Outcomes
1. First understanding how to send notifications ***EMAIL/MESSAGE*** (push notifications are not helpfull)
2. Then understanding voice recognition techniques
3. Learn web automations to automute/unmute
4. Finally integrate everything

## Requirements
- Any version of `python` and `pip`
- For email `python smtplib` will be required.
- Now for speech recognition and related stuff you need
    1. `speechRecognition`
    3. `pyAudio`
- For counts `time` is required
## Timeline  
- [x] Basic step of recognizing voice and notifying over email on using terminal
- [ ] Enhancing the functionality using `radis queue` and `google cloud api` and allowing to send notification over different handelers
- [ ] Converting into a full stack web-app deploying using Heroku/Aws
- [ ]  Introducing automation to join attend and leave meetings.
- [ ] During a meeting detecting the `keyword` and auto unmute then play an audio file then mute back 
- [ ] Front-end using `React` and enhancing the UI.
### Done
- Recognizing voice and chechking for desired Keyword
- On keyword detection sending email using the passed parameters.

## Installation 
1. Clone the repo
2. Enter the directory ` cd OCassistant`
3. `pip3 install -r requirements.txt`
> If this command not wirking then perform following steps manually
4. `pip3 install speechRecongition`
5. `pip3 install pyaudio`
> If pyaudio giving err then first try below command then install pyaudio `sudo apt install libasound-dev portaudio19-dev libportaudiocpp0`
***CHANGE SENDER_EMAIL PASSWORD AND RECIPIENT_EMAIL TO YOURS THEN ONLY RUN IT***
6. Run `python3 index.py`
> NOTE : > 1. The password is not the gmail password it should be [gmailAppPassword](https://support.google.com/accounts/answer/185833?hl=en). 
>  2. These installation steps are for Mac/Linux. For please windows try yourself 

## Fixes
- Passing `keyword_to_match_with` needs optimization
- Allowing multiple processes to run simultaneously using `radis queue` mainly `Queuing` 
## Refrences
https://askubuntu.com/questions/1235957/how-to-add-chromedriver-to-path-in-ubuntu
