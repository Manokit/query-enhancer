import re
s = '''
<text start="0" dur="2.12">Hey, this is kinda like a part two video</text>
<text start="2.18" dur="2">
I mean you don&#39;t have to have seen the part one video
</text>
<text start="4.18" dur="2.34">to understand what I talk about in this video,</text>
<text start="6.52" dur="3.06">
But I mean if you haven&#39;t watched part one, uh, you should.
</text>'''
text = re.sub('<[^>]+>', '', s)
print(text)