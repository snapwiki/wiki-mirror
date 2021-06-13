from requests import get

somefile = open(input("File name: "), 'w', encoding='utf-8')
somefile.write(get(input("REST endpoint: ")).text)
somefile.close()
