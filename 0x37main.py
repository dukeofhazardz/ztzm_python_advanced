import requests

url = "https://blog-backend-pi-two.vercel.app"
token = None

def register():
    first_name = str(input("Enter your First Name: "))
    last_name = str(input("Enter your Last Name: "))
    username = str(input("Enter your Username: "))
    email = str(input("Enter your Email: "))
    password = str(input("Enter your Password: "))

    if not (first_name and last_name and username and email and password):
        print("All fields are required.")
        return

    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "email": email,
        "password": password
    }
    response = requests.post(url=url + "/api/register", json=payload)
    if response.status_code == 201:
        print("User registered successfully", response.json())
    else:
        print("Failed to register user.", response.status_code)

def login():
    global token
    email = str(input("Enter your Email: "))
    password = str(input("Enter your Password: "))

    if not (email and password):
        print("All fields are required.")
        return

    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(url=url + "/api/login", json=payload)
    if response.status_code == 200:
        data = response.json()
        print("User logged-in successfully.", data)
        token = data["access"]
        return token
    else:
        print("Failed to log in user.", response.status_code)

def create_blog(token):
    title = str(input("Enter your Post Title: "))
    content = str(input("Enter your Content: "))
    category = str(input("Enter your Category: "))
    tags = str(input("Enter your Tags e.g (#life #fyp): "))

    if not (title and content and category and tags):
        print("All fields are required.")
        return
    if not token:
        print("You need to log in first.")
        return

    payload = {
        "title": title,
        "content": content,
        "category": category,
        "tags": tags
    }
    
    headers = {
        "Authorization": f"Bearer {token}"
    }
    
    response = requests.post(url=url + "/api/create", data=payload, headers=headers)
    if response.status_code == 201:
        print("Blogpost created successfully.", response.json())
    else:
        print("Failed to create blogpost.", response.status_code)

def view_blogs():
    response = requests.get(url=url + "/api/blogs")
    if response.status_code == 200:
        print("Blogposts", response.json())
    else:
        print(f"Failed to view blogposts.", response.status_code)

while True:
    try:
        print("\n==== Welcome to the Blogsite Backend CLI ====")
        command = int(input(
            "Select an option to continue:\n"
            "1. Register\n"
            "2. Login\n"
            "3. Create a new Blogpost\n"
            "4. View all Blogs\n"
            "5. Exit\n"
            "> "
        ))

        if command == 1:
            register()
        elif command == 2:
            token = login()
        elif command == 3:
            if token:
                create_blog(token)
            else:
                print("You need to log in first.")
        elif command == 4:
            view_blogs()
        elif command == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select between 1-5.")

    except ValueError:
        print("Invalid input. Please enter a number (1-5).")
    except Exception as e:
        print(f"Unexpected error: {e}")
