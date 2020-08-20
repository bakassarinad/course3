from bs4 import BeautifulSoup
import re
def parse(path_to_link):
    imgs, headers, linkslen, lists = 0, 0, 0, 0
    with open(path_to_link, encoding="utf-8") as file:
        soup = BeautifulSoup(file, 'lxml')

    header_list = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    letters = ['C', 'E', 'T']
    letters_mass = ['ul', 'ol']

    div = soup.find('div', attrs = {'id':'bodyContent' })
    for link in div.findAll("img"):
        try:
            if int(link.get('width')) >= 200:
                imgs += 1
            
        except Exception as e:
            pass
    for h in header_list:
        for link in div.findAll(h):
            if link.text[0] in letters:
                headers += 1
    print(headers)

    for element in letters_mass:
        for link in div.findAll(element):
            if not link.find_parents(letters_mass):
                lists += 1
    print(lists)

    for a in div.findAll('a'):
        current = 1

        for tag in a.find_next_siblings():
            if tag.name == 'a':
                current += 1
            else:
                break
        if current > linkslen:
            linkslen = current


    return [imgs, headers, linkslen, lists]

#parse('wiki/Spectrogram')

