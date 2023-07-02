from django.http import HttpResponseForbidden
from django.urls import reverse


class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'admin' in request.path:
            if not request.user.is_authenticated or not request.user.is_superuser:
                return HttpResponseForbidden()

        return self.get_response(request)
