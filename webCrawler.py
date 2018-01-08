import requests

def page_download(): 
    url ="http://movie.daum.net/premovie/released"
    source_code = requests.get(url)
    playin_text = source_code.text
    print(playin_text)
    
    
page_download()
