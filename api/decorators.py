from django.http import JsonResponse


def ajax_login(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return JsonResponse(data={'error': 'Login to proceed.'}, status=401)

        return func(request, *args, **kwargs)

    return wrapper
