# Social Media API

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
