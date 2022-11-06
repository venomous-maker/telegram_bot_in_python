from flask import Flask
from flask import request
from flask import Response
import os
import requests
import json
import conn

TOKEN = "5335*****:AAFd6gr4ClCTNJGHOshSoF*******"#bot token here
app = Flask(__name__)
def tel_parse_message(message, key):
    print("message-->",message)
    try:
        chat_id = message[key]['chat']['id']
        txt = message[key]['text']
        username = message[key]['from']['username'] if 'username' in message[key]['from'] else message[key]['from']['first_name'] + " " + message[key]['from']['last_name']
        print("chat_id-->", chat_id)
        print("txt-->", txt)
        return chat_id,txt,username
    except:
        try:
            g_chat_id = message[key]['chat']['id']
            g_file_id = message[key]['photo'][0]['file_id']
            print("g_chat_id-->", g_chat_id)
            print("g_image_id-->", g_file_id)
 
            return g_file_id
        except:
            try:
                g_chat_id = message[key]['chat']['id']
                g_file_id = message[key]['video']['file_id']
                print("g_chat_id-->", g_chat_id)
                print("g_video_id-->", g_file_id)
 
                return g_file_id
            except:
                try:
                    g_chat_id = message[key]['chat']['id']
                    g_file_id = message[key]['audio']['file_id']
                    print("g_chat_id-->", g_chat_id)
                    print("g_audio_id-->", g_file_id)
 
                    return g_file_id
                except:
                    try:
                        g_chat_id = message[key]['chat']['id']
                        g_file_id = message[key]['document']['file_id']
                        print("g_chat_id-->", g_chat_id)
                        print("g_file_id-->", g_file_id)
 
                        return g_file_id
                    except:
                        print("NO file found found-->>")
#text message function
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text,
                'reply_to_message_id': reply_to_message_id
                
                }
   
    r = requests.post(url,json=payload)
    return r

# images function
def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': open("~/Pictures/svc.png", 'r'),
        'caption': "This is a sample image"
    }
 
    r = requests.post(url, json=payload)
    return r

#audio function
def tel_send_audio(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
 
    payload = {
        'chat_id': chat_id,
        "audio": "http://www.largesound.com/ashborytour/sound/brobob.mp3",
 
    }
 
    r = requests.post(url, json=payload)
 
    return r

#video function
def tel_send_video(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'
 
    payload = {
        'chat_id': chat_id,
        "video": "https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4",
 
    }
 
    r = requests.post(url, json=payload)
 
    return r

# document function
def tel_send_document(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
 
    payload = {
        'chat_id': chat_id,
        "document": "http://www.africau.edu/images/default/sample.pdf",
 
    }
 
    r = requests.post(url, json=payload)
 
    return r

#pols function
def tel_send_poll(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    payload = {
        'chat_id': chat_id,
        "question": "In which direction does the sun rise?",
        "options": json.dumps(["North", "South", "East", "West"]),
        "is_anonymous": False,
        "type": "quiz",
        "correct_option_id": 2
    }
 
    r = requests.post(url, json=payload)
 
    return r

#button function
def tel_send_button(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "What is this?",
                'reply_markup': {'keyboard': [[{'text': 'supa'}, {'text': 'mario'}]]}
    }
 
    r = requests.post(url, json=payload)
 
    return r

# inline button
def tel_send_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "What is this?",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "A",
                    "callback_data": "ic_A"
                },
                {
                    "text": "B",
                    "callback_data": "ic_B"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r

#inline url
def tel_send_inlineurl(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "Which link would you like to visit?",
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "google", "url": "http://www.google.com/"},
                    {"text": "youtube", "url": "http://www.youtube.com/"}
                ]
            ]
        }
    }
 
    r = requests.post(url, json=payload)
 
    return r

def chat_handler(msg, key):
    global reply_to_message_id
    if 'reply_to_message' in msg[key]:
        reply_to_message_id = msg[key]['reply_to_message']['message_id']
    if 'message_id' in msg[key]:
        reply_to_message_id = msg[key]['message_id']
    else:
        reply_to_message_id = None
    if True:
        chat_id, txt, username = tel_parse_message(msg, key)
        TXT = txt
        txt = txt.lower()
        if txt == "audio":
            tel_send_audio(chat_id)
        elif "nmap: " in txt:
            inex_ = TXT[TXT.index('nmap: ') + 6 : ]
            print(inex_)
            tel_send_message(chat_id, f"Hello {username}, please hold on as we scan nmap -T4 {inex_}!")
            results = pentest(inex_).nmap()
            tel_send_message(chat_id, f"NMAP Results\n {results}")
        elif txt == "hi" or txt == "hello" or txt == "mambo":
            tel_send_message(chat_id, f"Hello, {username}!")
        elif "how are you" in txt:
            tel_send_message(chat_id, f"I am fine {username}. What about you?")
        elif "i am fine" in txt:
            tel_send_message(chat_id, f"Great {username}!")
        elif "wish me a happy birthday" in txt:
            tel_send_message(chat_id, f"Happy Birthday @{username}, Enjoy your GROWTH!")
        elif "thank you" in txt:
            tel_send_message(chat_id, f"Welcome @{username}!")
        elif txt == "file":
            tel_send_document(chat_id)
        elif txt == "video":
            tel_send_video(chat_id)
        elif txt == "image":
            tel_send_image(chat_id)
        elif txt == "inlineurl":
            tel_send_inlineurl(chat_id)
        elif txt == "poll":
            tel_send_poll(chat_id)
        elif txt == "button":
            tel_send_button(chat_id)
        elif txt == "inline":
            tel_send_inlinebutton(chat_id)
        else:
            tel_send_message(chat_id, f'Unknown message: {TXT}')

#send media
def tel_upload_file(file_id):
    url = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}'
    a = requests.post(url)
    json_resp = json.loads(a.content)
    print("a-->",a)
    print("json_resp-->",json_resp)
    file_pathh = json_resp['result']['file_path']
    print("file_path-->", file_pathh)
   
    url_1 = f'https://api.telegram.org/file/bot{TOKEN}/{file_pathh}'
    b = requests.get(url_1)
    file_content = b.content
    with open(file_pathh, "wb") as f:
        f.write(file_content)

# new member added
def tel_add_member(message, key):
    chat_id = message[key]['chat']['id']
    group_name = message[key]['chat']['title']
    if 'username' in message[key]['from']:
        add_member = message[key]['from']['username']
    else:
        add_member = message[key]['from']['first_name'] + " " + message[key]['from']['last_name']
    for user in message[key]['new_chat_members']:
        if 'username' in user:
            username = user['username']
        else:
            username = user['first_name'] + " " + user['last_name']
        url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
        payload = {
                'chat_id': chat_id,
                'text': f"Hello {username}, welcome to {group_name} your membership was awarded to you by {add_member}"
            }
        print('New Member--> ', username)
        print("Added By--> ", add_member)
    r = requests.post(url, json=payload)
    return r

class pentest:
    def __init__(self, ip):
        self.ip = ip
    def nmap(self):
        results = os.popen(f'nmap -T5 {self.ip}').read()
        return results

def media_handler(msg, key):
    if True:
        file_id = tel_parse_message(msg, key)
        tel_upload_file(file_id)
def webhook_new():
    URL = input("Input new url for webhook to capture: ")
    return URL
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
        print(msg)
        if 'edited_message' in msg:
            key = 'edited_message'
            if 'text' in msg['edited_message']:
                chat_handler(msg, key)
            else:
                media_handler(msg, key)
        elif 'poll_answer' in msg:
            key = 'poll_answer'
            chat_id = msg[key]['user']['id']
            txt = msg[key]['poll_id']
            username = msg[key]['user']['username']
            print("user_id-->", chat_id)
            print("poll id-->", txt)
            print("Username-->", username)
        elif  'message' in msg:
            key = 'message'
            chat_id = msg[key]['chat']['id']
            username = msg[key]['from']['username'] if 'username' in msg[key]['from'] else msg[key]['from']['first_name'] + " " + msg[key]['from']['last_name']
            firstName = msg[key]['from']['first_name'] if 'first_name' in msg[key]['from'] else 'null'
            lastName = msg[key]['from']['last_name'] if 'last_name' in msg[key]['from'] else 'null'
            conn.DataBase.func(conn.DataBase.insert_user(chat_id, firstName, lastName, username))
            if 'new_chat_members' in msg['message']:
                tel_add_member(msg,key)
            elif 'text' in msg['message']:
                chat_handler(msg, key)
            elif 'audio' in msg['message'] or 'video' in msg['message'] or 'photo' in msg['message'] or 'document' in msg['message']:
                media_handler(msg, key)
            else:
                return 0
        elif 'my_chat_member' in msg:
            key = 'my_chat_member'
            if 'old_chat_member' and 'new_chat_member' in msg[key]:
                chat_id = msg[key]['chat']['id']
                demoter = msg[key]['from']['username']
                demoted = msg[key]['old_chat_member']['user']['username']
                url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                if msg[key]['old_chat_member']['status'] == 'administrator' and msg[key]['new_chat_member']['status'] == 'member':
                    payload = {
                               'chat_id': chat_id,
                               'text': f"{demoted} was demoted by {demoter} from {msg[key]['old_chat_member']['status']} to {msg[key]['new_chat_member']['status']}",
                            }
                    r = requests.post(url,json=payload)
                    print(r)
                if msg[key]['old_chat_member']['status'] == 'member' and msg[key]['new_chat_member']['status'] == 'administrator':
                    payload = {
                               'chat_id': chat_id,
                               'text': f"{demoted} was promoted by {demoter} from {msg[key]['old_chat_member']['status']} to {msg[key]['new_chat_member']['status']}",
                            }
                    r = requests.post(url,json=payload)
                    print(r)
            elif 'new_chat_member' in msg[key]:
                chat_id = msg[key]['chat']['id']
                new_member = msg[key]['new_chat_member']['username']
                url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                payload = {
                           'chat_id': chat_id,
                           'text': f"{new_member} has joined the chat",
                        }
                r = requests.post(url,json=payload)
                print(r)
            elif 'left_chat_member' in msg[key]:
                chat_id = msg[key]['chat']['id']
                left_member = msg[key]['left_chat_member']['username']
                url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
                payload = {
                    'chat_id': chat_id,
                    'text': f"{left_member} has left the chat",
                }
                r = requests.post(url,  json=payload)
                print(r)
        else:
            key = 'message'
            
        return Response('ok', status=200)
    else:
        return '<h><center><bold>You Are Trying To Access Ven_Bot\'s Official Site</center> </bold></h1>'
 
if __name__ == '__main__':
    app.run(threaded=True, debug=True)
