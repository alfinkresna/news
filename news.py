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
    def kemenkumham():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tKemenkumham")
        url = sources['kemenkumham']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
    
    @staticmethod
    def antaranews_hukum():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tAntaranews (Hukum)")
        url = sources['antaranews_hukum']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
            
    @staticmethod
    def antaranews_politik():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tAntaranews (Politik)")
        url = sources['antaranews_politik']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
            
    @staticmethod
    def antaranews_kriminalitas():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tAntaranews (Kriminalitas)")
        url = sources['antaranews_kriminalitas']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
            
    @staticmethod
    def vice_indonesia():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tVice Indonesia")
        url = sources['vice_indonesia']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
            
    @staticmethod
    def cnn_indonesia():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tCNN Indonesia")
        url = sources['cnn_indonesia']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
            
    @staticmethod
    def cnbc_indonesia():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tCNBC Indonesia")
        url = sources['cnbc_indonesia']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
            
    @staticmethod
    def cyware_cybersecurity():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tCyware (Cybersecurity)")
        url = sources['cyware_cybersecurity']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
            
    @staticmethod
    def f5_threats():
        system_clear()
        with open('sources.yml', 'r') as f:
        	sources = safe_load(f)
        print("\n\t\tF5 (Threats)")
        url = sources['f5_threats']
        news = News(url)
        for item in news.news:
            print('\u000AJudul :', item['title'])
            print('\u000ATanggal :', item['date'])
            print('\u000AKonten :', item['content'])
            print('\u000ALink :', item['link'])
            print(news.border)
 

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
    		exit("\n---Keluar Program---\n")
    	else:
    		print("\n[!] Input Salah\n\n[!] Pilih Angka 1-9 / Angka 0 Untuk Keluar\n") 	

if __name__ == "__main__":
    main()
