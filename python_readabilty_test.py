import sys
from bs4 import BeautifulSoup
#sys.path.append("/Users/Muthu/Sites/isi/python-readability")
sys.path.insert(0, '/Users/Muthu/Sites/isi/readability_code/python_readability')
#print sys.path
from readability1.readability import Document
# sys.path.insert(0, '/Users/Muthu/Sites/isi/python-readability/readability')
# from . import Document
import urllib

arr = ["http://losangeles.backpage.com/FemaleEscorts/late-date-with-busty-blonde-bombshell-upscale-ready-to-play-sexycome-to-me/24646204",
	"http://losangeles.backpage.com/FemaleEscorts/real-young-asian-girls-kelly-and-sexy-chinese-niki-excellent-services/50040514",
	"http://losangeles.backpage.com/FemaleEscorts/young-hot-mixed-asian/63756660",
	"http://losangeles.backpage.com/FemaleEscorts/424-224-2136-charming-sexy-arabian-incall-lax105/64435652",
	"http://losangeles.backpage.com/FemaleEscorts/hablo-espanol-1000-me-or-its-free-outcalls-only/63434905",
	"http://losangeles.backpage.com/FemaleEscorts/global-sexxys-latinas-gentlemen-new-treatment-girls-gg-spa/61106281",
	"http://losangeles.backpage.com/FemaleEscorts/sunshine-available-now-incall-oonlyqv90-30min130-hr-150/64913111",
	"http://losangeles.backpage.com/FemaleEscorts/new-y-o-u-n-g-girl-asian-young/64834860",
	"http://losangeles.backpage.com/FemaleEscorts/100-specials-limited-time-jessica-rain-ptit-nd-sweet-100-me-or-free/54873052",
	"http://losangeles.backpage.com/FemaleEscorts/sexy-caramel-barbie-doll-cute-girl/63871582",
	"http://losangeles.backpage.com/FemaleEscorts/realy-new-japanese-young-girl-pretty-sweet-cozy-massage-services-6572276076/65033335",
	"http://losangeles.backpage.com/FemaleEscorts/morning-specials-beautiful-and-latina-come-see-a-and-juicy-girl-who-loves-handsome-men/65025069",
	"http://losangeles.backpage.com/FemaleEscorts/luxuryspa-lovelylatinas-40510-freeway/62359660",
	"http://losangeles.backpage.com/FemaleEscorts/sexy-belizean-godess-big-booty-caramel-all-r-e-l-come-get-your-fixutit/62497186",
	"http://losangeles.backpage.com/FemaleEscorts/sexy-belizean-godess-big-booty-caramel-all-r-e-l-come-get-your-fixutit/62268601",
	"http://losangeles.backpage.com/FemaleEscorts/b-g-213331o692-8oqv-lax/64991663",
	"http://losangeles.backpage.com/FemaleEscorts/i-can-come-to-yuh/65054337",
	"http://losangeles.backpage.com/FemaleEscorts/lax-incall-1oo-specials-h0t-asian-latina-mix/63277038",
	"http://losangeles.backpage.com/FemaleEscorts/way-2-hot-2-handle-foxxy-brazilian-looking-2-have-fun-fun-fun-and-play-play-play/49623772",
	"http://losangeles.backpage.com/FemaleEscorts/sexy-beauty-andso-hot/33317924",
	"http://losangeles.backpage.com/FemaleEscorts/open-minded-sexy-brunette-janet-outcall/33471446"
] 

html = urllib.urlopen("http://www.eroticmugshots.com/ftlauderdale-escorts/954-601-7752/?pid=36770728").read()
readable_article = Document(html).summary(True)
print readable_article
sys.exit()

i = 21
for urlex in arr:
	html = urllib.urlopen(urlex).read()
	readable_article = Document(html).summary(True)
	i += 1

	tags = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head><body>'
	data = readable_article.encode('utf-8')
	tags_end = "</body></html>"
	# soup = BeautifulSoup(data,"lxml")
	# metatag = soup.new_tag('head')
	# soup.html.insert(0,metatag)

	# metatag = soup.new_tag('meta')
	# metatag.attrs['http-equiv'] = 'Content-Type'
	# metatag.attrs['content'] = 'text/html; charset=utf-8'
	# soup.head.append(metatag)

	# print soup.prettify()
	# #print soup.contents
	# break

	f = open('fileHtml'+str(i)+".html",'w')
	f.write(tags + data + tags_end) # python will convert \n to os.linesep
	f.close()

	# soup = BeautifulSoup(your_old_html)
	# soup.body.insert(0, your_tag)
	# print soup

	# markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
	# soup = BeautifulSoup(markup)
	# tag = soup.a

	# tag.insert(1, "but did not endorse ")
	# tag
	# # <a href="http://example.com/">I linked to but did not endorse <i>example.com</i></a>
	# tag.contents

# readable_title = Document(html).short_title()


# print readable_article.encode('utf-8')


# #print readable_title