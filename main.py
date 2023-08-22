import requests
for i in range(1, 5001):
    url = "http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id=" + str(i)
    response = requests.get(url)
    print(response.json())
    if response.status_code == 200:
        print(url)
    
    




