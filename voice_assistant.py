import speech_recognition as Jc
import datetime
import wikipedia
import webbrowser
import requests
import playsound
import json
import wolframalpha

def talk():
    input = Jc.Recognizer()
    with Jc.Microphone() as source:
        audio = input.listen(source)
        data = ""
        try:
            data = input.recognize_google(audio)
            print("Jc "+data)
        except Jc.unkownvalueError:
            print("sorry i did not hear your question,please repet again")
    return data  
    def respond (output):
        Num = 0
        print(output)
        num += 1
        response = gTTS(text = output, lang='en')
        file = str(num)+".mp3"
        response.save(file)
        playsound.playsound(file,true)
        os.remove(file)
    if __name__=='__main_':
        respond("hi,i am Jc your personal assistant")
        while(1):
            respond("how can i help you bro?")
            text = talk().lower()
            if text == 0:
                continue
            if "stop" in str(text) or "exit" in str(text) or "bye" in str(text):
                respond('searching wikipiedia')
                text = text.replace("wikipedia","")
                result=wikipedia.summary(text,sentences=3)
                respond("according to wikipedia")
                print(result)
                respond(result)
            elif  'time' in text:
                strTime=datetime.datetimenow().strftime("%H:%M:%S")
                respond(f"the time is {strTime}")
            elif 'search' in text:
                text=text.replace("search","")
                webbrowser.open_new_tab(text)
                time.sleep(5)
            elif "calculate " or "what is" in text:
                question=talk()
                app_id="mention your API key"
                client=wolframalpha.Client(app_id)  
                res=client.query(QUESTION)
                answer =next(res.result).txt 
                respond("the answer is"+answer)
            elif 'open google' in text:
                webbrowser.open_new_tab("http://www.google.com")
                respond("google is open")
                time.sleep(5)
            elif 'youtube' in text:
                driver=webdriver.chrome(r"mention your webdriver location")
                driver.implicitly_wait(1)
                driver.maximize_window()
                respond("opening in youtube")
                indx = text.split() .index('youtube')
                query = text.split()[indx +1]
                driver.get("http://http://www.youtube.com/results?search_query="+'+'.join(query))
            elif "open word" in text:
                respond("opening microsoft word")
                os.startfile('mention location of word in your system')
            else:
                respond("application not 