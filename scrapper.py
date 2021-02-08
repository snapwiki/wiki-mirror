from requests import get

somefile = open('main.html', 'w', encoding='utf-8')
somefile.write(get('https://snapwiki.miraheze.org/w/rest.php/snapwiki.miraheze.org/v3/page/html/Main%20Page/4696').text)
somefile.close()