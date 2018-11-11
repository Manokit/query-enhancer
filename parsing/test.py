import requests

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {"v": "2yFCyPX3kT0", "lang": "en"}

response = requests.get("https://www.youtube.com/api/timedtext?", params=parameters)



print response.content
#print response.content == response.text

