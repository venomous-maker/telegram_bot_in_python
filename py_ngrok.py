from pyngrok import ngrok, conf, exception
global link1
def ngrok_link(TOKEN, PORT, SERVICE):
    try:
        ngrok.set_auth_token(TOKEN)
        link1 = ngrok.connect(PORT, SERVICE)
        if True:
            link = str(link1)
            link = link[link.index('"http') + 1: link.rindex('" ->')]
        else:
            link = 0
    except exception.PyngrokNgrokHTTPError:
        link = 0
        #Sngrok.disconnect(link1.public_url)
    return link
#print(ngrok_link("1fOk1IbTTrO7B1rtKB1igwpJ5PW_6Pzyc7Wyrg59VfdJPstd3", 5000, 'http'))