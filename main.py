from loguru import logger

from novel import Novel
from parser import Parser
def main():


    logger.add("file.log",
               format='{time:YYYY-M-DD at HH:mm:ss} | {level} | {message}',
               rotation="3 days",
               backtrace=True,
               diagnose=True)
    

    title = input("Введите название новеллы:")
    url = input("Введите ссылку новеллы:")
    #pars = Parser(title, url)
    #pars.get_novel()

    novel = Novel(title)
    novel.load_novel_from_bd()
    novel.print_novel_to_terminal()
    


if __name__ == "__main__":
    main()