import requests

# TODO: @Owen_Desai - give me a link to use. I don't have a facebook
url = 'https://www.facebook.com/ical/b.php?uid=100001111111111&key=ABCDEFGHIJKLMNOP'

#Open downloaded calendar file
data = requests.get(url)
#Append all data into a single continuous string
text_data = data.content
