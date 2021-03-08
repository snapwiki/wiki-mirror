from requests import get
from configuration import REST_ENDPOINT_URL, SCRAP_DIR
from mw_api_client import Wiki
import os

wiki = Wiki('https://snapwiki.miraheze.org/w/api.php', 'Snap! Wiki Scrapper/1.0.0')
pages = wiki.allpages()
indexa = '<!DOCTYPE html><html><head> <title>Snap! Wiki Mirror</title><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><link href="https://unpkg.com/tailwindcss@^2/dist/tailwind.min.css" rel="stylesheet"></head><body><div> <nav class="bg-gray-800"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8"><div class="flex items-center justify-between h-16"><div class="flex items-center"><div class="flex-shrink-0"> <img class="h-8 w-8 inline" src="https://snapwiki.github.io/assets/images/logo.png" alt="Logo"><span class="inline text-gray-200"> Snap<i>!</i> Wiki</span></div><div class="hidden md:block"><div class="ml-10 flex items-baseline space-x-4"> <a href="/wiki-mirror" class="bg-gray-900 text-white px-3 py-2 rounded-md text-sm font-medium">Home</a><a href="Main Page.html" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Main Page</a></div></div></div></div></div> </nav><header class="bg-white shadow"><div class="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8"><h1 class="text-3xl font-bold leading-tight text-gray-900"> Wiki Mirror</h1></div> </header> <main><div class="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8"><div class="flex flex-col"><div class="-my-2 overflow-x-auto sm:-mx-6 lg:-mx-8"><div class="py-2 align-middle inline-block min-w-full sm:px-6 lg:px-8"><div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg"><table class="min-w-full divide-y divide-gray-200"><thead class="bg-gray-50"><tr><th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th><th scope="col" class="relative px-6 py-3"><span class="sr-only">Go</span></th></tr></thead><tbody class="bg-white divide-y divide-gray-200">'
indexb = '</tbody></table></div></div></div></div> </main></div></body></html>'
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
index.write(indexa + indexslot + indexb)
index.close()
