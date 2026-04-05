# Django REST Framework API with Swagger & JWT

## Overview
Minimal Django REST Framework app with Swagger documentation and JWT authentication.

**Superuser credentials:**
- Username: `admin`
- Password: `admin123`

---

## API Endpoints

### 1. Token Endpoints (No auth required)
- **POST** `/api/token/` — Obtain JWT access token
  - Body: `{"username": "admin", "password": "admin123"}`
  - Response: `{"access": "<token>", "refresh": "<token>"}`

- **POST** `/api/token/refresh/` — Refresh expired access token
  - Body: `{"refresh": "<refresh_token>"}`
  - Response: `{"access": "<new_token>"}`

### 2. Protected API Endpoints (Auth required)
- **GET** `/api/hello/` — Returns personalized greeting
  - Header: `Authorization: Bearer <access_token>`
  - Response: `{"message": "Hello, admin!"}`
  - Without token: `401 Unauthorized`

### 3. Documentation Endpoints
- **GET** `/api/schema/` — OpenAPI schema (JSON)
- **GET** `/api/schema/swagger/` — Swagger UI (interactive)
- **GET** `/api/schema/redoc/` — ReDoc UI (alternative docs)

---

## How to Test

### Option A: Using Swagger UI (Recommended)
1. Open http://localhost:8000/api/schema/swagger/
2. Click **Authorize** (top-right)
3. POST `/api/token/` with admin credentials to get token
4. Copy the `access` token value only (without "Bearer" prefix)
5. In Authorize dialog, paste the raw token (Swagger adds "Bearer" automatically)
6. Test GET `/api/hello/` — should return `{"message": "Hello, admin!"}`
7. Logout from Authorize → GET `/api/hello/` → should get 401

### Option B: Using cURL
```bash
# 1. Get access token
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"admin123"}'

# 2. Use token to call protected endpoint (copy access token from response)
curl -X GET http://localhost:8000/api/hello/ \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN_HERE"

# 3. Test without token (should return 401)
curl -X GET http://localhost:8000/api/hello/
```

### Option C: Using Python
```python
import requests

# Get token
response = requests.post(
    'http://localhost:8000/api/token/',
    json={'username': 'admin', 'password': 'admin123'}
)
token = response.json()['access']

# Call protected endpoint
headers = {'Authorization': f'Bearer {token}'}
response = requests.get('http://localhost:8000/api/hello/', headers=headers)
print(response.json())  # {"message": "Hello, admin!"}

# Without token (401)
response = requests.get('http://localhost:8000/api/hello/')
print(response.status_code)  # 401
```

---

## Expected Behavior

✅ **POST /api/token/** → Returns access & refresh tokens  
✅ **GET /api/hello/** (with token) → `{"message": "Hello, admin!"}`  
✅ **GET /api/hello/** (without token) → 401 Unauthorized  
✅ **Swagger UI** → Fully interactive with token authorization  

---

## Quick Start

1. **Server already running?** Visit http://localhost:8000/api/schema/swagger/
2. **Server down?** Run: `python manage.py runserver`
3. **Need fresh database?** Run: `python manage.py migrate`
4. **Need new superuser?** Run: `python manage.py createsuperuser`
