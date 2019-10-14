import urllib.request 
request_url = urllib.request.urlopen('https://www.bing.com/') 
print(request_url.read()) 

