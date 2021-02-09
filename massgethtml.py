from requests import get
from configuration import REST_ENDPOINT_URL, SCRAP_DIR
from mw_api_client import Wiki
import os

wiki = Wiki('https://snapwiki.miraheze.org/w/api.php', 'Snap! Wiki Scrapper/1.0.0')
pages = wiki.allpages()

for page in pages:

    filename1 = SCRAP_DIR + page.title
    try:
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

    except:
        print("An exception occurred")

