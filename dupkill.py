#!/usr/bin/python
from urlparse import urlparse
build = []
filename = "akarmi.txt"
def main():
  cache()
	for url in build:
		info = retlist(url)
		for x in build:
			if retlist(x) == info:
				build.remove(x)
				pass
			pass
		build.append(url)
		pass
	print build
	i = 0
	for x in build:
		i += 1
		pass
	print "I got the job done, the remaining url's is {0}.".format(i)
	#print ret
	pass
def retlist(url):
	if not "www." in urlparse(url).netloc:
		url0= "www.{0}".format(urlparse(url).netloc)
	else:
		url0 = urlparse(url).netloc
		pass
	path = urlparse(url).path
	url = urlparse(url)
	a = []
	for x in url.query.split("&"):
		a.append(x.split("=")[0])
		pass
	ret = []
	ret.append(url0)
	ret.append(path)
	ret.append(a)
	return ret
def cache():
	i = 0
	for sor in open(filename, "r"):
		build.append(sor)
		i += 1
		pass
	print "We start with {0} url's.".format(i)
	pass
if __name__ == '__main__':
	main()
