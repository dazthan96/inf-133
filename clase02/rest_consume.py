import requests
card_btn="BT1-010"
url = f"https://digimoncard.io/api-public/search.php?card={card_btn}"
response = requests.request(
    method="GET",
    url=url,
    headers={"Content-Type": "application/json"},
    data={}
    
)
print(response.text)