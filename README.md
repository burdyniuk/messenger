# IP - Proiect Messenger

## Collaborator:
- Ilie Burdiniuc
- Costin Brebu
- Andrei Petrea
- Catalin Barus

## Backend API:
- ip/auth/login/
	- fields:
		- username
		- password
	- return
		- access token
		- refresh token
- ip/auth/register/
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
- ip/login/refresh/
	- fields:
		- refresh (token de refresh primit la login)
	- return:
		- access token
		- refresh token
