import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
    
except Exception as erro:
    print('site fora do ar')
else:
    print('Site no ar')