from html.parser import HTMLParser
from urllib.request import urlopen

class MyHTMLParser(HTMLParser):
	def __init__(self, site_name, *args, **kwargs):
		self.links = []
		self.site_name = site_name
		super().__init__(*args, **kwargs)
		self.feed(self.read_site_content())
		self.write_to_file()

	def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for attr in attrs:
				if attr[0] == 'href':
					if not self.validate(attr[0]):
						self.links.append(attr[1])

	def validate(self, link):
		return link in self.links or '#' in link or 'javascript:' in link

	def read_site_content(self):
		return str(urlopen(self.site_name).read())

	def write_to_file(self):
		f = open('links.txt', 'w')
		f.write('\n'.join(sorted(self.links)))
		f.close()

parser = MyHTMLParser("http://python.org")

