import requests
#response = requests.get('https://httpbin.org/ip')
response = requests.get('https://hello-app-codespace.streamlit.app')
print(response.text)
