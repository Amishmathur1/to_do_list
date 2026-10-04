## Database Schema

2 tables
    - User Table
        - Id
        - User_id
        - username/mail
        - password_hash
        - timestamp

    - To-Do
        - Id
        - User_id
        - Title
        - description
        - status
        - timestamp

## Endpoints

- Auth
    - POST - /register
    - POST - /login

- Todo
    - POST - /todo
    - GET - /todo
    - GET - /todo/{user_id}
    - PUT - /todo/{user_id}
    - DELETE - /todo/{user_id}