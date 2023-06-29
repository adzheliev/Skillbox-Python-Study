import re
import requests


my_req = requests.get('http://www.columbia.edu/~fdc/sample.html')
data = my_req.text
pattern = r"(?<=>).+(?=</h3>)"
match = re.findall(pattern, data)
print(match)
