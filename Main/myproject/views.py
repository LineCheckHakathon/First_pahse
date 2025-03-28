from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User

# GET all users
@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        try:
            users = User.objects.all()
            user_data = [
                {
                    'id': user.id,
                    'email': user.email,
                    'name': user.name
                }
                for user in users
            ]
            return JsonResponse(user_data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# GET a specific user
@csrf_exempt
def get_user(request, user_id):
    if request.method != 'GET':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        
        user_data = {
            'id': user.id,
            'email': user.email,
            'name': user.name
        }
        return JsonResponse(user_data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
@csrf_exempt
def user_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            name = data.get('name')
            
            if not email or not password or not name:
                return JsonResponse({'error': 'Email, password, and name are required'}, status=400)
            
            # Check if user with this email already exists
            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already in use'}, status=400)
            
            # Create new user
            user = User(email=email, password=password, name=name)
            user.save()
            
            return JsonResponse({
                'id': user.id,
                'email': user.email,
                'name': user.name
            }, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

# PUT request to update user completely
@csrf_exempt
def update_user(request, user_id):
    if request.method != 'PUT':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        
        data = json.loads(request.body)
        user.email = data.get('email', user.email)
        user.name = data.get('name', user.name)
        
        # Only update password if provided
        if 'password' in data:
            user.password = data.get('password')
        
        user.save()
        
        return JsonResponse({
            'id': user.id,
            'email': user.email,
            'name': user.name
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# PATCH request to update user partially
@csrf_exempt
def patch_user(request, user_id):
    if request.method != 'PATCH':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        
        data = json.loads(request.body)
        
        # Update only provided fields
        if 'email' in data:
            user.email = data['email']
        if 'name' in data:
            user.name = data['name']
        if 'password' in data:
            user.password = data['password']
        
        user.save()
        
        return JsonResponse({
            'id': user.id,
            'email': user.email,
            'name': user.name
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

# DELETE request to delete user
@csrf_exempt
def delete_user(request, user_id):
    if request.method != 'DELETE':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

