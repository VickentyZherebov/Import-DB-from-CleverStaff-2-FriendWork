import re
url = "https://www.linkedin.com/in/denis-kleshchev-759b3211a/"
if url is not None and re.fullmatch("http\S+\s*", url):
    print(url)
else:
    print("bar re")
