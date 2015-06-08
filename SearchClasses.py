from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class GalleryList:
	
	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		results = self.browser.find_element_by_id(self.siteDict['results_container'])
		results = results.find_elements_by_tag_name(self.siteDict['resultsTagName'])
		if len(results) > 0:
			return True
		else:
			return False

class RRAuction:

	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		results = self.browser.find_element_by_id(self.siteDict['results_id'])

		try:
			quantity = results.find_element_by_tag_name(self.siteDict['resultsTagName'])
		except StaleElementReferenceException:
			return False
		
		else:
			try:
				q = int(quantity.text)
			except ValueError:
				return False
			else:
				if int(quantity.text) > 0:
					return True
				else:
					return False

class GalleryListClassName:

	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		results = self.browser.find_element_by_id(self.siteDict['results_container'])
		results = results.find_elements_by_class_name(self.siteDict['resultsClassName'])
	
		if len(results) > 0:
			return True
		else:
			return False


class HugginsAndScott:

	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		results = self.browser.find_elements_by_class_name(self.siteDict['resultsClassName'])
		if len(results) > 0:
			return True
		else:
			return False


class HeritageAuctions:
	
	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		try:
			results = self.browser.find_element_by_id(self.siteDict['results_container'])
		except NoSuchElementException:
			return False
		else:
			results = results.find_elements_by_class_name(self.siteDict['resultsClassName'])

			if len(results) > 0:
				return True
			else:
				return False

 

