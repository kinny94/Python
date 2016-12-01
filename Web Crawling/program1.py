import re
import urllib
url = "https://github.com/kiiiiNNNNNNNNNyyyy/"

stock = raw_input("Enter name of the repository: ")
url = url + stock
print url

data = urllib.request.urlopen(url).read()
data1 = data.decode("utf-8")
print data1

m = re.search('python', data1)
print m

start = m.start()
end = start + 50
new = data1[start: end]