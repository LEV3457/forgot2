from loguru import logger
from bs4 import BeautifulSoup
import requests

from novel import Novel



class Parser:
  
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.chapters = {}
        self.chapter = 1

    def get_novel(self):
        page = self.get_webpage(self.url)
        chapters_list = page.find('ul', class_="list clearfix")
        elements = chapters_list.find_all("a")
        links = []
        for element in elements:
            href = element.get('href')
            if href:
                links.append(href)

        logger.info(f"Все ссылки  на главы новеллы {self.title} собраны")



        for link in links:
            chapter_page = self.get_webpage(link)
            text = chapter_page.find('div', class_="book_con fix")
            self.chapters.update({str(self.chapter): link + text.text})
            
            logger.info(f'Глава {self.chapter} собрана по ссылке {link}')
            self.chapter += 1
        logger.info(f"Все тесты  на глав новеллы {self.title} собраны")   
        novel = Novel(self.title)
        novel.write_novel_to_bd(self.chapters)


            
        #return links

    def get_webpage(self, link):
        response = requests.get(link)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            logger.info(f"Страница{link} собрана") 
            return BeautifulSoup(response.text, "html.parser")
        else:
            logger.error(f"Страница{link} не собрана")