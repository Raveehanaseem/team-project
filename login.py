# Login System Module
def login(username, password):
    valid_users = {"admin": "admin123", "user1": "pass123"}
    if username in valid_users and valid_users[username] == password:
        print(f"[+] Login successful! Welcome, {username}")
        return True
    else:
        print("[-] Invalid credentials.")
        return False

if __name__ == "__main__":
    login("admin", "admin123")
