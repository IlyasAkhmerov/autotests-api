import httpx


login_payload = {
    "email": "user@example.com",
    "password": "password123"
}

login_response = httpx.post("http://127.0.0.1:8000/api/v1/authentication/login", json=login_payload)
access_token = login_response.json()['token']['accessToken']

headers = {
    "Authorization": f"Bearer {access_token}"
}

get_user_response = httpx.get("http://127.0.0.1:8000/api/v1/users/me", headers=headers)

print(get_user_response.status_code)
print(get_user_response.json())

