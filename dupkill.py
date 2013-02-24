#!/usr/bin/python
from urlparse import urlparse
build = []
outname = "" #output file
filename = "" #input file
def main():
	cache()
	for url in build:
		info = retlist(url)
		for x in build:
			if retlist(x) == info:
				build.remove(x)
		build.append(url)
	print build
	i = 0
	for x in build:
		i += 1
	writeOut()
	print "I got the job done, the remaining url's is {0}.".format(i)
def retlist(url):
	if not "www." in urlparse(url).netloc:
		url0= "www.{0}".format(urlparse(url).netloc)
	else:
		url0 = urlparse(url).netloc
	path = urlparse(url).path
	url = urlparse(url)
	a = []
	for x in url.query.split("&"):
		a.append(x.split("=")[0])
	return [url0,path,a]
def cache():
	i = 0
	for sor in open(filename, "r"):
		build.append(sor)
		i += 1
	print "We start with {0} url's.".format(i)
def writeOut():
	with open(outname, "w") as out:
		for url in build:
			out.write("{0}".format(url))
if __name__ == '__main__':
	main()
