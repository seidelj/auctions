from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from sites import sites as WEBSITES
import itertools, os, time, sys
import ConfigParser

# EMAIL STUFF
import smtplib
server = smtplib.SMTP('smtp.gmail.com:587')

config = ConfigParser.ConfigParser()
try:
	config.read("settings.ini")
	EMAIL = config.get('creds', 'email')
	PASSWD = config.get('creds', 'passwd')
except ConfigParser.NoSectionError:
	sys.exit("Improperly configured settings.ini file")


from SearchClasses import GalleryList, RRAuction, GalleryListClassName, HugginsAndScott, HeritageAuctions

browser = webdriver.Firefox()
browser.implicitly_wait(10)

SEARCH_PHRASES = ['Cal Ripken', '1982 Fleer card #176 ', 'PSA 10']

SEARCH_PHRASE = "Cal Ripken 1982 Fleer PSA 10 card #176"

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(PROJECT_DIR, 'results')

email = []



def main():
	for website in WEBSITES[23:]:
		get_search_page(website)
	print email

def send_mail(email):
	server.ehlo()
	server.starttls()

	server.login(EMAIL, PASSWD)
	
	msg = "\r\n".join([
		"From: AuctionMonitor",
		"To: jlist@uchicago.edu",
		"Subject: Cal Ripken Card Alert",
		"",
		"{}".format(email),
		])
 

def get_auction_link(browser, website):
	browser.get(website['url'])
	link = browser.find_element_by_id("af_sessionList").find_elements_by_tag_name("a")[0]
	link = link.get_attribute('href')
	return link

def get_search_page(website):
	if website['name'] == "Fusco Auctions":
		url = get_auction_link(browser, website)
		website['url'] = url
	search_for_card(website, browser)


def handle_alt_method(website, browser):
	url = None
	if website['altMethod'] == 'searchBy':
		d = browser.find_element_by_id(website['altId'])
		d.send_keys(website['altKeys'], Keys.RETURN)

def get_search_box(website, browser):
	if website['element'] == "class":
		searchBox = browser.find_element_by_class_name(website['searchbox'])
	if website['element'] == "id":
		searchBox = browser.find_element_by_id(website['searchbox'])
	if website['element'] == "name":
		searchBox = browser.find_element_by_name(website['searchbox'])
	return searchBox

def search_for_card(website, browser):
	#phrases = itertools.permutations(SEARCH_PHRASES)
	browser.get(website['url'])
	url = None
	if "altMethod" in website:
		handle_alt_method(website, browser)
		if website['altMethod'] == "getQuery":
			url = website['url'] + SEARCH_PHRASE.replace(" ","+")
	if url:
		browser.get(url)
		time.sleep(2)
	else:
		search_box = get_search_box(website, browser)
		search_box.send_keys(SEARCH_PHRASE)
		if "submit" in website:
			browser.find_element_by_id(website['submit']).click()
		else:
			search_box.send_keys(Keys.RETURN)
		time.sleep(2)
	classname = website['class']
	searchClass = globals()[classname](website, browser)
	if searchClass.search_website():
		email.append(website)

if __name__ == "__main__":
	main()




	
		
