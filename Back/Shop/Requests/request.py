import requests

def products_list():
    response = requests.get('http://127.0.0.1:8000/products/api-vi/products-list/')
    return response.json()


def register_user(phone,password,password2):
    response = requests.post('http://127.0.0.1:8000/accounts/api-vi/register/',{'phone':phone,'password':password,'password2':password2})
    access = response.json()['access_token']
    refresh = response.json()['refresh_token']
    print(refresh)
    print('-------------------------')
    print(access)
    
    return access, refresh

register_user('+989017963838','pan12345','pan12345')
   
def login(phone, password):
    response = requests.post('http://127.0.0.1:8000/accounts/api-vi/login/',{'phone':phone,'password':password})
    print(response.json(
        
    ))
    refresh = response.json()['refresh']
    access = response.json()['access']
    
    return refresh, access

# refresh,access, = login('+989017963535','pan12345')
# print(access)
# print('---------------------------------------')
# print(refresh)


def logout_user(refresh, access):
    response = requests.post('http://127.0.0.1:8000/accounts/api-vi/logout/',{'refresh':refresh}, headers={
        "Authorization": f"Bearer {access}"
    })
    print(response)


def t_view(access):
    response = requests.get('http://127.0.0.1:8000/accounts/api-vi/t-view/',headers={
        "Authorization": f"Bearer {access}"
    })
    print(response)

def refresh_login(refresh):
    response = requests.post('http://127.0.0.1:8000/accounts/api-vi/refresh/',{'refresh':refresh}
                             
                             )
    print(response.json())


def cart(token):
    response = requests.get('http://127.0.0.1:8000/products/api-vi/cart', headers={
        "Authorization": f"Bearer {token}"
    })
        
    print(response.json())

# cart('')

def addtocart(owner,item,quantity,token):
    response = requests.post('http://127.0.0.1:8000/products/api-vi/cart/', {'owner':owner,'item':item,'quantity':quantity},headers={
        "Authorization": f"Bearer {token}"
    }
    )
        
    print(response.json())

# addtocart('2','1','2','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NDU5MzU1LCJpYXQiOjE2ODYyNDk3NTUsImp0aSI6ImIyZjg3YmE3MDhiYzQ5NTc4NzljMjJmNWQxZmUwMjJmIiwidXNlcl9pZCI6Mn0.MH4XjaCAxv3p4eqkIKL4Twi1HTtmfhhOMybL9S_HCk8')

def cartitem(token):
    response = requests.get('http://127.0.0.1:8000/products/api-vi/cart/', headers={
        "Authorization": f"Bearer {token}"
    })
        
    print(response.json())

# cartitem('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjAzNTUxLCJpYXQiOjE2ODYzOTM5NTEsImp0aSI6ImM2YTk4MGRjYWIwMjQ0ZDI4NTJhMjY0YTQzMjIwYTQ2IiwidXNlcl9pZCI6Mn0.RNBB6pr7HKAqqBBfepNjVvUpzBK8E-fCwXich5wrF3c')

def update_cart(owner,item,quantity,token):
    response = requests.put('http://127.0.0.1:8000/products/api-vi/cart-detail/27', {'owner':owner,'item':item,'quantity':quantity}, headers={
        "Authorization": f"Bearer {token}"
    })
        
    print(response.json())

# update_cart('2','2','6','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjAzNTUxLCJpYXQiOjE2ODYzOTM5NTEsImp0aSI6ImM2YTk4MGRjYWIwMjQ0ZDI4NTJhMjY0YTQzMjIwYTQ2IiwidXNlcl9pZCI6Mn0.RNBB6pr7HKAqqBBfepNjVvUpzBK8E-fCwXich5wrF3c')

def delete_cart(token):
    response = requests.delete('http://127.0.0.1:8000/products/api-vi/cart-detail/26',  headers={
        "Authorization": f"Bearer {token}"
    })
        
    print(response.json())

# delete_cart('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NjAzNTUxLCJpYXQiOjE2ODYzOTM5NTEsImp0aSI6ImM2YTk4MGRjYWIwMjQ0ZDI4NTJhMjY0YTQzMjIwYTQ2IiwidXNlcl9pZCI6Mn0.RNBB6pr7HKAqqBBfepNjVvUpzBK8E-fCwXich5wrF3c')
    
def create_comment(id,body,token):
    response = requests.post(f'http://127.0.0.1:8000/products/api-vi/product-detail/{id}' , {'body':body},headers={
        "Authorization": f"Bearer {token}"})

    print(response.json())
                             
# create_comment('1','helo','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3Mjg5MjE3LCJpYXQiOjE2ODYwNzk2MTcsImp0aSI6Ijk0M2UzNmUxNTljODRmNDZiZjJlYjdjZDljNWQ0MzFkIiwidXNlcl9pZCI6Mn0.Ei0tyAXfdNXyH0kerItvJGXhKXGtKwXqxZUiyjbYYmc')                        

def favoritlist(token):
    response = requests.get(f'http://127.0.0.1:8000/products/api-vi/favorit-list' , headers={
        "Authorization": f"Bearer {token}"})

    print(response.json())

# favoritlist('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzA0ODczLCJpYXQiOjE2ODY0OTUyNzMsImp0aSI6ImNhMDc3NjE3YTZjMDQ2ZTRhNGViODVkZjMyYWY0ODIyIiwidXNlcl9pZCI6Mn0.SyCF_qxdIm4XrekqJsFCrsfmCphJVssCpXtUXycx0vM')



def addto_favoritlist(token):
    response = requests.post(f'http://127.0.0.1:8000/products/api-vi/addto-favorit-list/3' , headers={
        "Authorization": f"Bearer {token}"})

    print(response.json())

# addto_favoritlist('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg3NzA0ODczLCJpYXQiOjE2ODY0OTUyNzMsImp0aSI6ImNhMDc3NjE3YTZjMDQ2ZTRhNGViODVkZjMyYWY0ODIyIiwidXNlcl9pZCI6Mn0.SyCF_qxdIm4XrekqJsFCrsfmCphJVssCpXtUXycx0vM')