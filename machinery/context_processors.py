def add_user_role(request):
    return {
        'user_role': request.session.get('user_role', None)
    }