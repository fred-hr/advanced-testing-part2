def authenticate_user(username, password, role, device, network):
    valid_users = {
        "admin": {"password": "Admin123", "role": "admin"},
        "student": {"password": "Student123", "role": "student"},
        "guest": {"password": "Guest123", "role": "guest"},
    }

    if not username or not password:
        return {
            "success": False,
            "message": "Incomplete credentials",
        }

    if username not in valid_users:
        return {
            "success": False,
            "message": "User not found",
        }

    if valid_users[username]["password"] != password:
        return {
            "success": False,
            "message": "Invalid password",
        }

    if valid_users[username]["role"] != role:
        return {
            "success": False,
            "message": "Invalid role",
        }

    if device == "unknown" or network == "public":
        return {
            "success": True,
            "message": "Access granted with warning",
        }

    return {
        "success": True,
        "message": "Access granted",
    }