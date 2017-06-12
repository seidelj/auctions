from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

class MemoryLane:

	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		results = self.browser.find_element_by_class_name(self.siteDict['results_container'])
		results = results.find_elements_by_class_name(self.siteDict['resultsTagName'])
		if len(results) > 0:
			return True
		else:
			return False

class RMYAuctions(MemoryLane):

	def search_website(self):
		results = self.browser.find_element_by_class_name(self.siteDict['results_container'])
		results = results.find_elements_by_class_name(self.siteDict['resultsTagName'])
		if len(results) > 0:
			return True
		else:
			return False



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


class BeckettAuctions(GalleryList):

	def search_website(self):
		auctionId = self.browser.find_element_by_id(self.siteDict['auctionId'])
		if self.siteDict['noAuctionText'].upper() in auctionId.text:
			print "No auctions currently in system"
			return False
		else:
			results = self.browser.find_element_by_id(self.siteDict['results_container'])
			results = results.find_elements_by_tag_name(self.siteDict['resultsTagName'])
			if len(results) > 0:
				return True
			else:
				return False


class SearchForId:

	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		try:
			results = self.browser.find_element_by_id(self.siteDict['results_id'])
		except NoSuchElementException:
			return False
		else:
			return True

class FuscoAuctions:

	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		try:
			noresult = self.browser.find_element_by_class_name(self.siteDict['noResultsClass'])
		except NoSuchElementException:
			result = True
		else:
			result = False

		return result


class RRAuction:

	def __init__(self, siteDict, browser):
		self.siteDict = siteDict
		self.browser = browser

	def search_website(self):
		results = self.browser.find_element_by_id(self.siteDict['results_id'])

		try:
			results_list = results.find_element_by_tag_name(self.siteDict['resultsTagName'])
		except StaleElementReferenceException:
			return False

		else:
			try:
				q = int(results_list.text)
			except ValueError:
				return False
			else:
				if int(q) > 0:
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
