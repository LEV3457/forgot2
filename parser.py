import requests




class Parser:
  
    def __init__(self,title,url):
        self.title = title
        self.url = url
        self.chapters = {}
        self.chapter = 1

    def get_webpage(self, link):
        response = requests.get(link)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            logger.info(f"Страница{link} собрана")
        else:
            logger.error(f"Страница{link} не собрана")