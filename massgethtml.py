from requests import get
from configuration import REST_ENDPOINT_URL, SCRAP_DIR, API_URL, USERAGENT, INDEX_HEAD, INDEX_BODY
from mw_api_client import Wiki
import os

wiki = Wiki(API_URL, USERAGENT)
pages = wiki.allpages()
indexslot = ''
for page in pages:
    try:
        generatedslot = '<tr><td class="px-6 py-4 whitespace-nowrap text-left text-sm font-medium">' + page.title + '</td><td class="px-6 py-4 whitespace-nowrap text-left text-sm font-medium"><a class="text-indigo-500 hover:text-indigo-600" href="' + page.title + '.html">' + 'Visit</a></td></tr>'
        indexslot += generatedslot
        filename1 = SCRAP_DIR + page.title
        if filename1.count('/') > 1:
            for dir in filename1.split('/'):
                if not dir == '/':
                    path = SCRAP_DIR + dir
                    if not os.path.isdir(path):
                        os.mkdir(path)
        filename = open(filename1 + '.html', 'w', encoding='utf-8')
        restfilepath = REST_ENDPOINT_URL + page.title
        print(restfilepath)
        print(filename1)
        filename.write(get(restfilepath).text.replace('</body>', '<script src="https://scratchblocks.github.io/js/scratchblocks-v3.5-min.js"></script><script>scratchblocks.renderMatching(`.blocks`, {});</script></body>'))
        filename.close()
    except Exception as err:
        print("An exception occurred" + str(err))

index = open(SCRAP_DIR + '/index.html', 'w', encoding='utf-8')
index.write(INDEX_HEAD + indexslot + INDEX_BODY)
index.close()
