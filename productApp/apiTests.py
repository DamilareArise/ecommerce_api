import requests


def getProducts():
    url = "http://127.0.0.1:8000/productApp/get-product/"
    responds = requests.get(url)
    print(responds.json())
    
    
def addProduct(payload):
    url = "http://127.0.0.1:8000/productApp/add-product/"
    responds = requests.post(url, payload)
    print(responds.json())
    
addProduct({
    "name": "Product 3",
    "price": 100.0,
    "description": "Product 1 description",
    "imageUrl":'nil'
})

    
# getProducts()