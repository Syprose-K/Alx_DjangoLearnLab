# Social Media API

## https://your-app-name.herokuapp.com/
POST /api/accounts/register/
POST /api/accounts/login/
GET  /api/feed/
POST /api/posts/{id}/like/
GET  /api/notifications/


## Setup
1. `pip install -r requirements.txt`
2. `python manage.py migrate`
3. `python manage.py createsuperuser`
4. `python manage.py runserver`

## Endpoints
- `POST /api/accounts/register/` → Register a new user.
- `POST /api/accounts/login/` → Login and get token.
- `GET /api/accounts/profile/` → Get user profile (token required).

## User Model
- `username`
- `email`
- `bio`
- `profile_picture`
- `followers` (ManyToMany to self)

## Posts
- GET /api/posts/
- POST /api/posts/
- PUT /api/posts/{id}/
- DELETE /api/posts/{id}/

Supports search:
GET /api/posts/?search=keyword

## Comments
- GET /api/comments/
- POST /api/comments/
- PUT /api/comments/{id}/
- DELETE /api/comments/{id}/

Authentication required for all endpoints.


## Follow System

- **Follow a user**
POST /api/accounts/follow/{user_id}/
Authorization required

- **Unfollow a user**
POST /api/accounts/unfollow/{user_id}/
Authorization required

## Feed

- **Get feed**
GET /api/feed/
Returns posts from users you follow, newest first.
Authorization required


## Likes

POST /api/posts/{id}/like/
POST /api/posts/{id}/unlike/

## Notifications

GET /api/notifications/

Returns recent notifications such as:
- New followers
- Likes on posts
- Comments on posts


## Deployment

This project is deployed on Heroku.

### Live URL
https://your-app-name.herokuapp.com/

### Technologies Used
- Django
- Django REST Framework
- PostgreSQL
- Gunicorn
- WhiteNoise

### Deployment Steps
1. Configure production settings
2. Set environment variables
3. Deploy using Heroku Git
4. Run migrations
5. Collect static files
