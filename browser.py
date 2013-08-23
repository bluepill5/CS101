
# ALternative:
# start_link = page.find('<a href=')
# start_quote = page.find('"', start_link)
# end_quote = page.find('"', start_quote + 1)
# url = page[start_quote + 1: end_quote]

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=') + page[page.find('<a href='):].find('http')

end_link = page[start_link: ].find('"') + start_link

url = page[start_link: end_link]

print url


## (string) -> string
## Given a string with the content of a page, return 
#  the first url found.
## get_next_target("content") #stub
## >>> get_next_target(page)
## http://udacity.com

def get_next_target(page):
    try: 
      start_link = page.find('<a href=') + page[page.find('<a href='):].find('http')
      end_link = page[start_link: ].find('"') + start_link
      url = page[start_link: end_link]
      return url, end_link
    except ValueError:
      return "", 0


print get_next_target(page[117: ]) 
