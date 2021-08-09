import os
from requests import get
from mw_api_client import Wiki
from configuration import WIKI_ARTICLE_PATH, SCRAP_DIR, API_URL, USERAGENT, INDEX_HEAD, INDEX_BODY

wiki = Wiki(API_URL, USERAGENT)
pages = wiki.allpages()
indexslot = ''
for page in pages:
    if not '/' in page.title:
        try:
            generatedslot = '<tr><td class="px-6 py-4 whitespace-nowrap text-left text-sm font-medium">' + page.title + '</td><td class="px-6 py-4 whitespace-nowrap text-left text-sm font-medium"><a class="text-indigo-500 hover:text-indigo-600" href="' + page.title + '.html">' + 'Visit</a></td></tr>'
            indexslot += generatedslot
            filename1 = SCRAP_DIR + page.title
            if filename1.count('/') > 1:
                for directory in filename1.split('/'):
                    if not directory == '/':
                        path = SCRAP_DIR + directory
                        if not os.path.isdir(path):
                            os.mkdir(path)
            filename = open(filename1 + '.html', 'w', encoding='utf-8')
            articleurl = WIKI_ARTICLE_PATH + page.title + '?action=render'
            filename.write(get(articleurl).text.replace('</body>', '<script src="https://scratchblocks.github.io/js/scratchblocks-v3.5-min.js"></script><script>scratchblocks.renderMatching(`.blocks`, {});</script></body>'))
            filename.close()
        except Exception as err:
            print("An exception occurred" + str(err))

index = open(SCRAP_DIR + '/index.html', 'w', encoding='utf-8')
index.write(INDEX_HEAD + indexslot + INDEX_BODY)
index.close()
