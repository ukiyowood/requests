import requests
from bs4 import BeautifulSoup as bs

if __name__ == "__main__":
	target = 'https://images.unsplash.com'
	req = requests.get(url = target,verify=False)

	print(req.text)
	