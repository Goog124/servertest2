from requests import get, post, delete
from pprint import pprint


pprint(post('http://localhost:8080/api/v2/users',
           json={'surname': "Oleg",
                 'age': '15',
                 'name': "Oleg",
                 'position': "123",
                 'speciality': "123",
                 'address': "123",
                 'email': "123ddd32@123ddd23.ru",
                 'hashed_password': "123"}).json())
pprint(get('http://localhost:8080/api/v2/users/1').json())
pprint(get('http://localhost:8080/api/v2/users').json())
# pprint(delete('http://localhost:8080/api/v2/users/3').json())
