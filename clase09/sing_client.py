import requests
url = "http://localhost:8000/"

response = requests.request(method="GET", url=url+"player")

print(response.text)

post_response = requests.request(method="POST", url=url +"player/damage", json={"damage":50})
print(post_response.text)