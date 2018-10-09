import requests

response = requests.get('http://teamtreehouse.com')

print('Status code is: ' + str(response.status_code))
