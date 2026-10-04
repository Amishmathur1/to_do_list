## Workflow of this Project

Idea :-
    - To make a TO-DO List with auth support so every individual user will have its own to-do list
    - in V1 support basic login page with password hashing, after that think about google login via oauth
    - A normal simple UI and a basic TO-DO list with the options such as:-
        - Create new Item
        - Delete entry
        - Check Box 
        - Deadline (V2)
        - Reminder via registered mail (V2)

BackEnd Components:-
    - User registration
    - Password hashing
    - Login
    - JWT access tokens
    - Authentication dependency
    - Protected endpoints
    - Middleware
    - User ↔ Todo relationship
    - CRUD for todos
    - Authorization — user can only access their own todos
    - PostgreSQL
    - Direct SQL again no ORM's used
    - Environment variables
    - Proper project structure
    - Error handling
    - Validation

FrontEnd Components:-
    - Login
    - Register
    - Todo dashboard
    - Create/update/delete todo
    - Mark complete
    - Logout
    - Store/use JWT
    - Handle expired/invalid tokens


    Request
        ↓
    Middleware
        ↓
    Router
        ↓
    Dependency
        ↓
    JWT verification
        ↓
    Get current user
        ↓
    Authorization
        ↓
    Database
        ↓
    Response
    