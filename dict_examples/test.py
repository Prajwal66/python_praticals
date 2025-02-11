import requests

#to fetch the url and store it in response
response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json()

for data in range(len(complete_details)):
    print(complete_details[data]["user"]["login"])

