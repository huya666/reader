import requests
import json
from bs4 import BeautifulSoup

def searchList(query=''):
	url = "https://www.23txt.com"
	response  = requests.get(url + "/search.php?q=" + query)

	soup = BeautifulSoup(response.text, "html.parser")
	results = soup.select(".result-game-item")

	pagesResults = soup.find("div", class_="search-result-page-main").select('a')

	data = []
	pages = []

	for res in results:
		obj = {}
		obj["link"] = url + res.select_one(".result-game-item-pic-link").get("href")
		obj["title"] = res.select_one(".result-game-item-title-link").get("title")
		obj["lastTextUrl"] = url + res.find("a", cpos="newchapter").get("href")
		obj["new"] = url + res.find("a", cpos="newchapter").get("href")
		obj["newText"] = res.find("a", cpos="newchapter").getText()
		obj["desc"] = res.find("p", class_="result-game-item-desc").getText()
		obj["image"] = url + res.find("a", cpos="img").get("href")

		# 获取作者
		authorInfo = res.find("p", class_="result-game-item-info-tag")
		obj["author"] = authorInfo.select_one('span', class_="result-game-item-info-tag-title preBold").find_next_sibling("span").getText()

		#获取类型
		typeInfo = authorInfo.find_next_sibling("p", class_="result-game-item-info-tag")
		obj["type"] = typeInfo.select_one('span', class_="result-game-item-info-tag-title preBold").find_next_sibling("span").getText()

		#获取类型
		dateInfo = typeInfo.find_next_sibling("p", class_="result-game-item-info-tag")
		obj["lastUpdateDate"] = dateInfo.select_one('span', class_="result-game-item-info-tag-title preBold").find_next_sibling("span").getText()

		data.append(obj)
		# print(dateInfo,

	for page in pagesResults:
		strSearchPage = page.get('href')
		print(strSearchPage)
		pages.append({ "pageText": page.getText(), "pageNum": strSearchPage.split('p=')[1] })

	# jsonData = json.dumps(data, ensure_ascii=False)
	# print(jsonData, type(jsonData))
	print(pages)
	
	return { "pages": pages, "data": data, "success": True }