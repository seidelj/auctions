
sites = []

#GalleryList
sites.append({
	"name": "Albersheims",
	"url": "http://albersheims.com/",
	"element": "id",
	"searchbox": "query",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
	"submit": "SearchBtn",
})

#Huggins
sites.append({
	"name": "Baggers Auctions",
	"url": "http://www.baggersauctions.com/",
	"element": "id",
	"searchbox": "search",
	"resultsClassName": "detail",
	"class": "HugginsAndScott",
})

#GalleryList
sites.append({
	"name": "BST Auctions",
	"url": "http://bst-auctions.com/",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Becket Auction Services",
	"url": "http://auctions.beckett.com/",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "BeckettAuctions",
	"auctionId": "catalogAuctionLabel",
	"noAuctionText": "No auctions currently in system",
})

#GalleryList
sites.append({
	"name": "Clean Sweep Auctions",
	"url": "http://www.cleansweepauctions.com/",
	"element": "name",
	"searchbox": "searchtext",
	"results_container": "listdetail",
	"resultsTagName": "table",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Collect Auctions",
	"url": "http://www.collectauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"altMethod": "searchBy",
	"altId": "searchByDropDown",
	"altKeys": "t",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

# This url will need to be refreshed.  It is powered by 3rd
# party which means a new url will be generated for new auctions
# Current auction begins June 13, 2015
sites.append({
	"name": "Fusco Auctions",
	"url": "https://fusco.infinitebidding.com/?method=getUpcomingAuctions",
	"element": "id",
	"searchbox": "af_searchField",
	"results_container": "af_sessionList",
	"resultsTagName": "li",
	"noResultsClass": "norecords",
	"getUrl": True,
	"class": "FuscoAuctions",
})


#GalleryList
sites.append({
	"name": "Giovanni Sports Auctions",
	"url": "http://www.giovannisportsauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})


#GalleryList
sites.append({
	"name": "Goldin Auctions",
	"url": "http://goldinauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Goodwin and Company",
	"url": "http://www.goodwinandco.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Grey Flannel Auctions",
	"url": "http://greyflannelauctions.com/catalog.aspx?category=9",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
	"submit": "searchButton",
})

#HeritageAuctions
sites.append({
	"name": "Heritage Auctions",
	"url": "http://www.ha.com/",
	"element": "id",
	"searchbox": "text-search",
	"results_container": "batchBids",
	"resultsClassName": "lotname",
	"class" : "HeritageAuctions",
})

#HugginsAndScott
sites.append({
	"name": "Huggins and Scott",
	"url": "http://www.hugginsandscott.com",
	"element": "name",
	"searchbox": "search",
	"resultsClassName": "da_ltextb",
	"class": "HugginsAndScott",
})

#GalleryList
sites.append({
	"name": "Iconic Auctions",
	"url": "http://iconicauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Inside the Park",
	"url": "http://insidetheparkcollectibles.com/catalog.aspx",
	"element": "id",
	"searchbox":  "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Kevin Savage Cards",
	"url": "http://www.kevinsavagecards.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Lelands",
	"url": "http://www.lelands.com/Home/SearchResult?Type=t&Description=",
	"element": None,
	"searchbox": None,
	"altMethod": "getQuery",
	"results_container": "dvContent",
	"resultsTagName": "td",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Love the game auctions",
	"url": "www.loveofthegameauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Mears online auctions",
	"url": "www.mearsonlineauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
	"submit": "searchButton",
})

#GalleryList
sites.append({
	"name": "Memory Lane Inc.",
	"url": "http://memorylaneinc.com/site/lots/gallery?searchin=titledescription&search=",
	"element": "id",
	"searchbox": "ctl00_pnlSidebar_i1_i0_txtSearch",
	"altMethod": "getQuery",
	"results_container": "col-md-9",
	"resultsTagName": "item",
	"class": "MemoryLane",
})

#GalleryList
sites.append({
	"name": "Mile High Card Club",
	"url": "http://www.milehighcardco.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#HigginsAndScott
sites.append({
	"name": "Paragon Auctions",
	"url": "http://www.paragonauctionsite.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"altMethod": "searchBy",
	"altId": "searchByDropDown",
	"altKeys": "t",
	"results_container": "imageTable",
	"resultsClassName": "odd",
	"class": "HugginsAndScott",
})

#HugginsAndScott
sites.append({
	"name": "Pristine Auctions",
	"url": "https://pristineauction.com/auction/index/search/?search=",
	"element": None,
	"searchbox": None,
	"altMethod": "getQuery",
	"resultsClassName": "product-list",
	"class": "HugginsAndScott"
})

#HugginsAndScott
sites.append({
	"name": "PWCC Auctions",
	"url": "http://www.pwccauctions.com/live-auction.php?q=",
	"element": None,
	"searchbox": None,
	"altMethod": "getQuery",
	"resultsClassName": "item",
	"class": "HugginsAndScott",
})

#GalleryList
sites.append({
	"name": "RMY Auctions",
	"url": "http://www.rmyauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "query",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#RRAuction
sites.append({
	"name": "RR Auctions",
	"url": "http://www.rrauction.com/browse.cfm?SearchCrit=",
	"element": None,
	"searchbox": None,
	"altMethod": "getQuery",
	"results_id": "LotSearchMsg",
	"resultsTagName": "cfoutput",
	"class": "RRAuction",
})

#GalleryList
sites.append({
	"name": "SCP Auctions",
	"url": "http://catalog.scpauctions.com/Category/Featured_Items-406.html",
	"element": "id",
	"searchbox": "searchTextBox",
	"altMethod": "searchBy",
	"altId": "searchByDropDown",
	"altKeys": "tt",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Sirius Sports Auctions",
	"url": "http://siriussportsauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Small Traditions",
	"url": "http://www.smalltraditions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Sports World Auctions",
	"url": "http://www.sportsworldauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Steiner Sports",
	"url": "http://auction.steinersports.com/catalog.aspx?searchby=3&searchvalue=",
	"element": None,
	"searchbox": None,
	"altMethod": "getQuery",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Sterling Sports Auctions",
	"url": "http://www.sterlingsportsauctions.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Treasure Tidbits",
	"url": "http://www.treasuretidbitssportsauction.com/catalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryList
sites.append({
	"name": "Wheatland Auction Services",
	"url": "http://www.wheatlandauctionservices.com/catalog.aspx",
	"element": 'id',
	"searchbox": 'searchTextBox',
	"results_container": "galleryList",
	"resultsTagName": "li",
	"class": "GalleryList",
})

#GalleryListClassName
sites.append({
	"name": "Worthridge Auctions",
	"url": "http://www.worthridge.com/itemcatalog.aspx",
	"element": "id",
	"searchbox": "searchTextBox",
	"results_container": "imageTable",
	"resultsClassName": "even",
	"class": "GalleryListClassName"
})
