# requests para requisições HTTP
import requests

# http:// -> 80
# https:/ -> 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json())
print(response.text)
