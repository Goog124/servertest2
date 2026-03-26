from requests import get, post


print(get('http://localhost:8080/api/jobs/4').json())
# print(get('http://localhost:8080/api/hgfhfgh').json())
# print(get('http://localhost:8080/api/jobs/aaa').json())
# print(get('http://localhost:8080/api/jobs').json())
# print(get('http://localhost:8080/api/jobs/1').json())

# print(post('http://localhost:8080/api/jobs',
#            json={'team_leader': 2,
#                  'job': 'Текст новости',
#                  'work_size': 5,
#                  'is_finished': False,
#                  'collaborators': "1, 2, 3"}).json())