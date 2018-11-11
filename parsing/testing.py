import re
s = '<@ """@$ FSDF >something something <more noise>'
text = re.sub('<[^>]+>', '', s)
print(text)