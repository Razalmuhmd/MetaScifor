import requests

# Base URL for the API
base_url = "https://jsonplaceholder.typicode.com/posts"

# 1. GET: Fetching all posts
def get_posts():
    response = requests.get(base_url)
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

# 2. GET: Fetching a single post by ID
def get_post(post_id):
    url = f"{base_url}/{post_id}"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

# 3. POST: Creating a new post
def create_post():
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(base_url, json=new_post)
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

# 4. PUT: Updating a post by replacing it entirely
def update_post(post_id):
    updated_post = {
        "id": post_id,
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    url = f"{base_url}/{post_id}"
    response = requests.put(url, json=updated_post)
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

# 5. PATCH: Updating a part of the post
def patch_post(post_id):
    partial_update = {
        "title": "foo updated"
    }
    url = f"{base_url}/{post_id}"
    response = requests.patch(url, json=partial_update)
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")

# 6. DELETE: Deleting a post by ID
def delete_post(post_id):
    url = f"{base_url}/{post_id}"
    response = requests.delete(url)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

# Example usage:
if __name__ == "__main__":
    get_posts()
    get_post(1)
    create_post()
    update_post(1)
    patch_post(1)
    delete_post(1)
