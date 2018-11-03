#import requests

#response = requests.get("http://api.open-notify.org/iss-pass.json")
#print(response.status_code)

#print "Hello"
#print (help('modules') )


import urllib

req = urllib.request.Request('http://www.voidspace.org.uk')
with urllib.request.urlopen(req) as response:
    the_page = response.read()