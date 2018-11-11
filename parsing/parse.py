import re
f = open (r'/Users/zaffre/Documents/CS/sunhacks2018/sunhacks-2018-project/parsing/pleasework.txt')
s = f.read()
text = re.sub('<[^>]+>', '', s)
print(text)