from django.http import JsonResponse
from django.shortcuts import redirect


def ajax_login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.method == "POST" and request.is_ajax() and not request.user.is_authenticated:
            return JsonResponse(data={'error': 'authentication required'}, status=401)
        return func(request, *args, **kwargs)

    return wrapper


def redirect_predictions(func):
    def wrapper(request, *args, **kwargs):
        if request.method == "GET" and request.user.is_authenticated:
            return redirect('predictions')
        return func(request, *args, **kwargs)

    return wrapper
