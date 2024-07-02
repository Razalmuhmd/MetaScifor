from django.http import JsonResponse, HttpResponseNotAllowed ,HttpResponse
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

# Existing views
def index(request):
    return HttpResponse("Welcome to the API. Go to /api/posts/ to see the posts.")

def get_posts(request):
    response = requests.get(base_url)
    return JsonResponse(response.json(), safe=False)

def get_post(request, post_id):
    url = f"{base_url}/{post_id}"
    response = requests.get(url)
    return JsonResponse(response.json(), safe=False)

def create_post(request):
    new_post = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    response = requests.post(base_url, json=new_post)
    return JsonResponse(response.json(), safe=False)

def update_post(request, post_id):
    updated_post = {
        "id": post_id,
        "title": "foo",
        "body": "bar",
        "userId": 1
    }
    url = f"{base_url}/{post_id}"
    response = requests.put(url, json=updated_post)
    return JsonResponse(response.json(), safe=False)

def patch_post(request, post_id):
    partial_update = {
        "title": "foo updated"
    }
    url = f"{base_url}/{post_id}"
    response = requests.patch(url, json=partial_update)
    return JsonResponse(response.json(), safe=False)

def delete_post(request, post_id):
    url = f"{base_url}/{post_id}"
    response = requests.delete(url)
    return JsonResponse({"status_code": response.status_code})

# New view to handle all methods for the /api/post/ endpoint
def post_methods(request):
    if request.method == 'GET':
        return get_posts(request)
    elif request.method == 'POST':
        return create_post(request)
    else:
        # Return HTTP 405 Method Not Allowed for unsupported methods
        return HttpResponseNotAllowed(['GET', 'POST'])

# New viewset for Django REST Framework
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        # Handle GET request for getting all posts
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

    def retrieve(self, request, pk=None):
        # Handle GET request for getting a specific post
        queryset = self.get_queryset()
        post = queryset.filter(pk=pk).first()
        if not post:
            return JsonResponse({"error": "Post not found"}, status=404)
        serializer = self.serializer_class(post)
        return JsonResponse(serializer.data, safe=False)

    def create(self, request):
        # Handle POST request for creating a post
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def update(self, request, pk=None):
        # Handle PUT request for updating a post
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found"}, status=404)
        serializer = self.serializer_class(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        # Handle PATCH request for partially updating a post
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found"}, status=404)
        serializer = self.serializer_class(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        # Handle DELETE request for deleting a post
        try:
            post = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return JsonResponse({"error": "Post not found"}, status=404)
        post.delete()
        return JsonResponse({"message": "Post deleted"}, status=204)
