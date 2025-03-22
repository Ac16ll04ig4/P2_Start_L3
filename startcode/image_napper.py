import requests
url = "https://www.shutterstock.com/_next/data/5672de8ee3a/en/search/auto.json?term=auto"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"

}
response = requests.get(url, headers=headers)
print(response)

