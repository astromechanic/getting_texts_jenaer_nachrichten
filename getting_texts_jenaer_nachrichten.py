import urllib.request
import re

def download_page(url): #downloading the html code of one page

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            f = open('html.txt', 'a', encoding='utf-8')
            f.write(html)
            f.close()
    except:
        print('Error at', url)
        return

def raw_texts(txt): #getting the fragments of the texts (raw)

    f = open(txt, 'r', encoding='utf-8')
    content = f.read() #type = str
    f.close()
    nachrichten = re.findall('itemFullText.*?Quelle', content) #type = list

    for line in nachrichten:
        f1 = open('raw_texts.txt', 'a', encoding='utf-8')
        f1.write(line + '\n\n')

    f1.close()

def clean_text(txt): #cleaning the fragments from tags etc

    f = open(txt, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    content1 = re.sub('itemFullText">', '', content)
    content2 = re.sub('<.*?>', '', content1)

    f1 = open('clean_texts.txt', 'w', encoding='utf-8')
    f1.write(content2)
    f1.close()


def main():
    
    # collecting texts
    url = 'https://www.jenaer-nachrichten.de/stadtleben/'
    for i in range(13400, 13500):
        page_url = url + str(i)
        download_page(page_url)

    raw_texts('html.txt')
    clean_text('raw_texts.txt')

 
if __name__ == '__main__':
    main()

