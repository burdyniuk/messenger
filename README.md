# IP - Proiect Messenger

## Backend To-Do:
- [x] Login
- [x] Registration
- [x] Refresh Token
- [x] Change password
- [x] Update profile
- [x] Logout ✅ 2022-05-06
- [x] Change password e-mail ✅ 2022-05-09
- [x] Message tables ✅ 2022-05-06
- [x] Create socket for client connections? Request update every second ✅ 2022-05-09
- [x] Create new chat ✅ 2022-05-06
- [x] Create new group chat ✅ 2022-05-06
- [x] Send message ✅ 2022-05-06
- [ ] Update profile picture
- [ ] Send photo in message
- [ ] Send file in message

#### Credentiale:
- catalin - Barus123!
- costin - Brebu123!

> Ca sa testati backend-ul folositi postman! 
> Hello, PCom!

## Backend API:
- `ip/auth/login/` - method POST
	- fields:
		- username
		- password
	- return
		- access token
		- refresh token
- `ip/auth/register/` - method POST
	- fields:
		- username
		- password
		- password2
		- email
		- first_name
		- last_name
	- return 
		- username
		- email
		- first_name
		- second_name
- `ip/auth/login/refresh/` - method POST
	- fields:
		- refresh (token de refresh primit la login)
	- return:
		- access token
		- refresh token
- `ip/auth/change_password/`+id - method PUT
	- fields:
		- password
		- password2
		- old_password
	- returnL
		- nothing if all ok
		- detail with error
- `ip/auth/update_profile/`+id - method PUT
	- fields:
		- username
		- first_name
		- last_name
		- email
	- return:
		- username
		- first_name
		- last_name
		- email
- `ip/auth/me/` - method GET
	- needs authentification token
	- return
		- id
		- username
		- first_name
		- last_name
		- last_online
		- email
		- profile_picture
- `ip/chat/` - method Post - (il folositi pentru a crea un chat nou cu nume useri si daca e chat privat puneti privat, altfel e grup)
	- needs authentification token
```json
{
	"name": "Nume",
	"users": [1, 3],
	"type": "privat"
}
```
- `ip/chat/?name=`+nume chat method Get (e pentru search in chat-uri)
	- intoarce chat-urile cu numele dat
- `ip/chat/?users=`+users_id chat method Get
	- intoarce chat-urile in care e implicat user-ul (sa-l folositi pentru a afla ce chat-uri are userul)
- `ip/chat/`+id - method PATCH (adauga persoana in chat)
```json
{
	"users": 4
}
```
	- intoarce chat-ul updatat
- `ip/chat/messages/`+id - method POST
```json
{
    "chat_id": 1,
    "from_user": 1,
    "text": "Hello"
}
```
	- intoarce obiectul mesajului
- `ip/auth/password_reset/` - method POST
```json
{
	"email": "ilya.burdyniuk@yandex.com"
}
```
trimite token pe mail, raspunde daca e ok cu:
```json
{
	"status": "OK"
}
```
- `ip/auth/password_reset/confirm/` - method POST
```json
{
	"token": "codul primit pe mail",
	"password": "parola nou",
}
```
asta se va trimite din screen dupa screen de forgot password, cu 2 input:
	- code
	- parola noua
va intoarce in caz de succes:
```json
{
	"status": "OK"
}
```
