def record_user_click(index,keyword,url):
	urls=lookup(index,keyword)
	if urls:
		for entry in urls:
			if entry[0]==url:
				entry[1]=entry[1]+1


#--------------------------------------
def add_to_index(index,keyword,url):
	for item in index:
		if keyword==item[0]:
			if url not in item[1]: 
				item[1].append([url,0])
			return
	index.append([keyword,[[url,0] ]])

def lookup(index,keyword):
    for item in index:
        if item[0]==keyword: return item[1]
    return []


def add_page_to_index(index,url,content):
	words=content.split()
	for word in words:
		add_to_index(index,word,url)

def split_string(source,splitlist):
	output=[]
	atsplit=True
	for char in source:
		if char in splitlist:
			atsplit=True
		else:
			if atsplit:
				output.append(char)
				atsplit=False
			else:
				output[-1]=output[-1]+char
	return output
#------------------------------------
def get_page(url):
    try:
        import urllib
        usock=urllib.urlopen(url)
        data= str(usock.read())
        usock.close()
        return data
    except:
        return ""

def get_next_target(s):
	start_link=s.find('<a href=')
	if start_link==-1: return None,0
	start_quote=s.find('"',start_link)
	end_quote=s.find('"',start_quote+1)
	url=s[start_quote+1:end_quote]
	return url,end_quote

def get_all_links(page):
	links=[]
	while True:
		url, endpos=get_next_target(page)
		if url:
			links.append(url)
			page=page[endpos:]
		else: break
	return links

def crawl_web(seed,max_depth):
	tocrawl=[[seed,0]]
	crawled=[]
	index=[] # building the search index
	while tocrawl:
		page,depth=tocrawl.pop()
		if page not in crawled and depth<=max_depth:
			content=get_page(page)
			add_page_to_index(index,page,content)
			for link in get_all_links(content):
				tocrawl.append([link,depth+1])
			crawled.append(page)
	return index

print crawl_web('http://web.cecs.pdx.edu/~xcheng',1)[0]