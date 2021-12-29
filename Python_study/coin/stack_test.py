import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2887580007333-2890578944355-ybCWYsA7VYMfpm3Kv0knX693"
 
post_message(myToken,"#stock","jocoding")
