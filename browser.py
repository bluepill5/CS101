import urllib2
## Idea:
# page =('<div id="top_bin"><div id="top_content" class="width960">'
# '<div class="udacity float-left"><a href="http://udacity.com">')
# start_link = page.find('<a href=') + page[page.find('<a href='):].find('http')
# end_link = page[start_link: ].find('"') + start_link
# url = page[start_link: end_link]
# print url


## (string) -> string
## Given a string with the content of a page, return the first url found.
## get_next_target("content") #stub
## >>> get_next_target(page)
## http://udacity.com

def get_page(url):
	return urllib2.urlopen(url).read()

def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link < 0:
		return None, 0
	else:
		start_quote = page.find('"', start_link)
		end_quote = page.find('"', start_quote + 1)
		url = page[start_quote + 1:end_quote]
		return url, end_quote

def print_all_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break
	
print print_all_links(get_page('http://xkcd.com/353'))


