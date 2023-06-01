import feedparser as fp
from ruamel.yaml import safe_load
from bs4 import BeautifulSoup as bs
from system.system_clear import system_clear
from system.banner import banner


class News:
    
    def __init__(self, url):
        self.url = url
        self.parse = fp.parse(self.url)
        self._border = "-" * 60

    @property
    def border(self):
        return self._border

    @border.setter
    def border(self, value):
        self._border = value

    @property
    def news(self):
        news = []
        for post in self.parse.entries:
            data = {}
            data['title'] = post.title
            data['date'] = post.published
            soup = bs(post.summary, 'html.parser')
            data['content'] = soup.get_text()
            data['link'] = post.link
            news.append(data)
        return news
        
    @staticmethod
    def get_sources():
        with open('system/sources.yml', 'r') as f:
            sources = safe_load(f)
        return sources
    
    @staticmethod
    def print_news(news, border):
        for item in news:
            print('\nJudul :', item['title'])
            print('\nTanggal :', item['date'])
            print('\nKonten :', item['content'])
            print('\nLink :', item['link'])
            print(border)
            
    @staticmethod
    def kemenkumham():
        system_clear()
        print("\n\t\tKemenkumham")
        sources = News.get_sources()
        url = sources['kemenkumham']
        news = News(url)
        News.print_news(news.news, news.border)
    
    @staticmethod
    def antaranews_hukum():
        system_clear()
        print("\n\t\tAntaranews (Hukum)")
        sources = News.get_sources()
        url = sources['antaranews_hukum']
        news = News(url)
        News.print_news(news.news, news.border)
            
    @staticmethod
    def antaranews_politik():
        system_clear()
        print("\n\t\tAntaranews (Politik)")
        sources = News.get_sources()
        url = sources['antaranews_politik']
        news = News(url)
        News.print_news(news.news, news.border)
            
    @staticmethod
    def antaranews_kriminalitas():
        system_clear()
        print("\n\t\tAntaranews (Kriminalitas)")
        sources = News.get_sources()
        url = sources['antaranews_kriminalitas']
        news = News(url)
        News.print_news(news.news, news.border)
            
    @staticmethod
    def vice_indonesia():
        system_clear()
        print("\n\t\tVice Indonesia")
        sources = News.get_sources()
        url = sources['vice_indonesia']
        news = News(url)
        News.print_news(news.news, news.border)
            
    @staticmethod
    def cnn_indonesia():
        system_clear()
        print("\n\t\tCNN Indonesia")
        sources = News.get_sources()
        url = sources['cnn_indonesia']
        news = News(url)
        News.print_news(news.news, news.border)
            
    @staticmethod
    def cnbc_indonesia():
        system_clear()
        print("\n\t\tCNBC Indonesia")
        sources = News.get_sources()
        url = sources['cnbc_indonesia']
        news = News(url)
        News.print_news(news.news, news.border)
            
    @staticmethod
    def cyware_cybersecurity():
        system_clear()
        print("\n\t\tCyware (Cybersecurity)")
        sources = News.get_sources()
        url = sources['cyware_cybersecurity']
        news = News(url)
        News.print_news(news.news, news.border)
            
    @staticmethod
    def f5_threats():
        system_clear()
        print("\n\t\tF5 (Threats)")
        sources = News.get_sources()
        url = sources['f5_threats']
        news = News(url)
        News.print_news(news.news, news.border)
 

def main():
    menu_options = {
        1 : News.kemenkumham,
        2 : News.antaranews_hukum,
        3 : News.antaranews_politik,
        4 : News.antaranews_kriminalitas,
        5 : News.vice_indonesia,
        6 : News.cnn_indonesia,
        7 : News.cnbc_indonesia,
        8 : News.cyware_cybersecurity,
        9 : News.f5_threats
    }
    
    while True:
        print(banner)
        user_input = int(input("\nPilih Menu : "))
        if user_input in menu_options:
            menu_options[user_input]()
        elif user_input == 0 :
            exit("\n" + ("-" * 3) + "Keluar Program" + ("-" * 3) + "\n")
        else:
            print("\n[!] Input Salah\n\n[!] Pilih Angka 1-9 / Angka 0 Untuk Keluar\n")         


if __name__ == "__main__":
    main()
