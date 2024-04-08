# UYGA VAZIFA

# import requests

# BOT_TOKEN = "6186043302:AAEZW3U27HKY2gqO6WyrJlumt7N3-EeVrzQ"
# CHAT_ID = "1245143580"

# def send_message(chat_id, text):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendmessage?chat_id={chat_id}&text={text}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         print("Habaringiz yuborildi")

# text = input("Biron narsa yozing: ")
# send_message(CHAT_ID, text)


# def send_photo(photo, text):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/SendPhoto?chat_id={CHAT_ID}&photo={photo}"
#     response = requests.get(url)
#     if response.status_code == 200:
#         print("Habaringiz yuborildi")
#     else:
#         print("Xatolik yuz berdi:", response.status_code)
        
# text = input("Biron narsa yozing: ")
# photo = "https://www.linearity.io/blog/content/images/2023/06/how-to-create-a-car-NewBlogCover.png"
# send_photo(photo, text)


# def send_video(video, text):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendvideo?chat_id={CHAT_ID}&video={video}"
#     response = requests.get(url)
#     print(response)
#     if response.status_code == 200:
#         print("Habaringiz yuborildi")

# text = input("Biron narsa yozing: ")
# print(f"Your message: {text}")

# video = "https://uzhits.net/dl3/2017/mobile/2018/Shahzod_Mirzo_-_Ongga_chapga_(HD_Clip)_(UzHits.Net).mp4"
# send_video(video=video, text=text)


# def send_animation(animation, text):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendAnimation?chat_id={CHAT_ID}&animation={animation}"
#     response = requests.get(url)
#     print(response)
#     if response.status_code == 200:
#         print("Habaringiz yuborildi")

# text = input("Biron narsa yozing: ")
# print(f"Your message: {text}")

# animation = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Animhorse.gif/225px-Animhorse.gif"
# send_animation(animation=animation, text=text)


# def send_audio(audio, text):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendaudio?chat_id={CHAT_ID}&audio={audio}"
#     response = requests.get(url)
#     print(response)
#     if response.status_code == 200:
#         print("Habaringiz yuborildi")

# text = input("Biron narsa yozing: ")
# print(f"Your message: {text}")

# audio = "http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/theme_01.mp3"
# send_audio(audio=audio, text=text)


# def send_document(document, text):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/senddocument?chat_id={CHAT_ID}&document={document}&caption={text}"
#     response = requests.get(url)
#     print(response)
#     if response.status_code == 200:
#         print("Habaringiz yuborildi")

# text = input("Biron narsa yozing: ")
# print(f"Your message: {text}")

# document = "http://ferlibrary.uz/f/chingiz_aytmatov_oxirzamon_nishonalari_roman15.pdf"
# send_document(document=document, text=text)

# def send_document(location, text):
#     url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendLocation"
#     data = {'chat_id': CHAT_ID, 'latitude': 39.863011, 'longitude': 64.770685, 'caption': text}
#     response = requests.post(url, data=data)
#     print(response)
#     if response.status_code == 200:
#         print("Habaringiz yuborildi")

# text = input("Biron narsa yozing: ")
# print(f"Your message: {text}")

# location = "https://maps.google.com/maps?q=39.863011,64.770685&ll=39.863011,64.770685&z=16"
# send_document(location=location, text=text)

import requests

def send_location(latitude, longitude, text, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendLocation"
    data = {'chat_id': chat_id, 'latitude': latitude, 'longitude': longitude, 'caption': text}
    response = requests.post(url, data=data)
    print(response)
    if response.status_code == 200:
        print("Habaringiz yuborildi")

text = input("Biron narsa yozing: ")
latitude = 39.863011
longitude = 64.770685
bot_token = "6186043302:AAEZW3U27HKY2gqO6WyrJlumt7N3-EeVrzQ"
chat_id = "1245143580"

send_location(latitude, longitude, text, bot_token, chat_id)