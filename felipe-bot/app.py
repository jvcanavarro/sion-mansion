import requests

limit = 3
api_url = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'hJrrXZX8OVAvZeEPrK4N4Q==3RzmrplwkPVtbidS'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)