from livestreamer import Livestreamer
from bs4 import BeautifulSoup
import requests



def test_start(model):
    model_link_api = 'https://chaturbate.com/api/chatvideocontext/' + model + '/'
    result = requests.get(model_link_api).json()
    session = Livestreamer()
    session.set_option('http-header',"referer=https://www.chaturbate.com/{}/".format(model))
    stream = session.streams("hlsvariant://{}".format(result['hls_source'].rsplit('?')[0]))
    stream = stream['best']
    fd = stream.open()
    
    with open(model + '.mp4', 'wb') as file:
        while True:
            data = fd.read(1024)
            file.write(data)
            
def get_online_model(pages, f):
    
    page_link = "https://chaturbate.com"
    req = requests.get(pages)
    soup = BeautifulSoup(req.text, 'html.parser')

    for i in soup.find_all("div" , {"class":"title"}):
        if i.a['href'][0] == "/":
            models = i.a['href'].replace('/','') + '\n'
            f.write(models)
    
    

    
    
if __name__ == "__main__":
    no_pages = 2
    model_list = 'wanted.txt'
    with open(model_list, "w") as f:
        for i in range(1, no_pages+1):
            print(i)
            pages = "https://chaturbate.com/female-cams/?page={}".format(i)
            get_online_model(pages, f)
    f.close()
 

                




























