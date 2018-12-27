'''

WebCrawler Practice!

'''


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re #need to explore regex too!

# So far, this webcrawler will pour through wikipedia data from the 
# list of largest cities and their coresponding pages to find the 
# Associated elevations


def grab_tags(url, tag): #will return soup list from all tags in url
    client = urlopen(url) 
    raw_html = client.read()
    client.close()
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.find_all(tag)

def find_elevation(url):
	for tag in [x for x in grab_tags(url,'tr') if "ELEVATION" in str(x).upper()]:
		for text in re.findall("<td>(.*?)</td>",str(tag)): 
			# there should be only one, but it would be smart to allow for multiple 
			return(text.replace(u'\xa0', u' '))

def grab_cities_list():
	list_of_links = []
	for item in grab_tags('https://en.wikipedia.org/wiki/List_of_largest_cities','tbody'):
		for link in [x for x in re.findall("<a href=\"(.*?)\"",str(item)) if '#' not in x and ':' not in x]:
			list_of_links.append(link)
	return list_of_links

def create_elevation_csv():
	for city_link in grab_cities_list():
		temp_city = city_link.replace("/wiki/","").replace("_"," ")
		temp_elevation = find_elevation("https://en.wikipedia.org"+city_link)
		if temp_elevation is not None:
			elevation_cleaned = re.sub(r'\([^)]*\)', '',temp_elevation)
			elevation_cleaned = elevation_cleaned.replace('from','').replace('to','').replace(',','') #TODO: handle ranges 
			if 'ft' in elevation_cleaned.lower():
				elevation_cleaned = str(round(float(re.search('[0-9]+',elevation_cleaned).group(0))*3.28084))
			else:
				elevation_cleaned = re.search('[0-9]+',elevation_cleaned).group(0)
			#todo unicode garbo
			print(temp_city + " --- " + elevation_cleaned)
			with open('elevation.csv','a') as file:
				file.write(temp_city+"| "+elevation_cleaned+"\n")

create_elevation_csv()