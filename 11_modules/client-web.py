# work with an web api

# verify if api is responding / working
import requests 

response_status = requests.get('https://www.python.org/ravi')
print(response_status)
