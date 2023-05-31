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
   


 

def logout_user(refresh, access):
    response = requests.post('http://127.0.0.1:8000/accounts/api-vi/logout/',{'refresh':refresh}, headers={
        "Authorization": f"Bearer {access}"
    })
    print(response)

def login(phone, password):
    response = requests.post('http://127.0.0.1:8000/accounts/api-vi/login/',{'phone':phone,'password':password})
    print(response.json(
        
    ))
    refresh = response.json()['refresh']
    access = response.json()['access']
    
    return refresh, access


def t_view(access):
    response = requests.get('http://127.0.0.1:8000/accounts/api-vi/t-view/',headers={
        "Authorization": f"Bearer {access}"
    })
    print(response)

def refresh_login(refresh):
    response = requests.post('http://127.0.0.1:8000/accounts/api-vi/refresh/',{'refresh':refresh}
                             
                             )
    print(response.json())


# access, refresh = login('+989017963636','pan123456')
# print(access)
# print('---------------------------------------')
# print(refresh)
# access = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NDIwMzIyLCJpYXQiOjE2ODUyMTA3MjIsImp0aSI6IjM4MGJhZmEyNDUwNTRkZTY5NWJiMTA3MGY5NmFiYzgwIiwidXNlcl9pZCI6M30.wFWZQCTwz_fvWKaLzzfaBffBM7Sjk_Psv5HLK7FsrNY'
# refresh = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzYyOTkyMiwiaWF0IjoxNjg1MjEwNzIyLCJqdGkiOiIyYzU0NjViZTliMmM0NmNkOWVkY2FlY2RjMjI4N2VkNCIsInVzZXJfaWQiOjN9.7aytPF6SKLXRRvHZVLfksYXSxI4TT5xKUaZKOG9bq5Y'
# logout_user(refresh)
# t_view('8cd63af3918e4f6ce5d7bf1ae17c24a3de8738d8')
# register_user('+989017963535','pan12345','pan12345')

# access = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NTE2MzIzLCJpYXQiOjE2ODUzMDY3MjMsImp0aSI6ImU2ZmQ4YWRmNDgwZjRkZTA5OTgzZDI0MzY3MjZiOTExIiwidXNlcl9pZCI6N30._KDBlaaO5BrTtCV_SLCuiU3VmHopwzywgKF7qYc_boU'
# refresh = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4NzcyNTkyMywiaWF0IjoxNjg1MzA2NzIzLCJqdGkiOiI3OWExNmIzOTMxN2U0YTczODU2MDg1ZDczYmFiMjlkYSIsInVzZXJfaWQiOjd9.rfDNIk-lyh4rt3j7OPyK7m2idQJHvdDB1x0sBdCfGiA'

# logout_user(refresh, access)
# t_view('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NTEzMzk0LCJpYXQiOjE2ODUzMDM3OTQsImp0aSI6IjY5MTgwNGZkNWY5NjQyZTlhMjZkNjNjM2U2OGM3ZDdkIiwidXNlcl9pZCI6NH0.tRouSsvjSowxIvyK8OyBVathdJm-gMAHh3dltjOc8XM')

# refresh_login(refresh)
# refresh,access, = login('+989017963535','pan12345')
# print(access)
# print('---------------------------------------')
# print(refresh)
# t_view('')
def cart(token):
    response = requests.get('http://127.0.0.1:8000/products/api-vi/cartitem', headers={
        "Authorization": f"Bearer {token}"
    })
        
    print(response.json())

def addcart(cart,owner,item,quantity,token):
    response = requests.post('http://127.0.0.1:8000/products/api-vi/cartitem', {'cart':cart,'owner':owner,'item':item,'quantity':quantity},headers={
        "Authorization": f"Bearer {token}"
    }
    )
        
    print(response.json())

# addcart('8','3','2','2','eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NzUxNjQzLCJpYXQiOjE2ODU1NDIwNDMsImp0aSI6IjEyMDIzYzljNmZkMTQ5NzI5ZjdjMzM4MTEyMjk4MzVkIiwidXNlcl9pZCI6M30.34k6O_8ssn7_1SSDSgLzO-Msl5XUlBStM5ncLJS393g')

# register_user('+989017963535','pan12345','pan12345')

    

# refresh,access, = login('+989017963535','pan12345')
# print(access)
# print('---------------------------------------')
# print(refresh)

cart('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg2NzUxNjQzLCJpYXQiOjE2ODU1NDIwNDMsImp0aSI6IjEyMDIzYzljNmZkMTQ5NzI5ZjdjMzM4MTEyMjk4MzVkIiwidXNlcl9pZCI6M30.34k6O_8ssn7_1SSDSgLzO-Msl5XUlBStM5ncLJS393g')