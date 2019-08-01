import requests

URL = 'https://gen-net.herokuapp.com/api/users/'

#id = input('Digite o ID: ')
email = input('Digite o email: ')

#response = requests.get(URL.format(id))

response = requests.get(URL)
users = response.json()

for user in users:
	if user.get('email') == email:
		print(user)


#print(response.json())