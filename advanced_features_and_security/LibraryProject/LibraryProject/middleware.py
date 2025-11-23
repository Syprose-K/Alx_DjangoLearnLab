# LibraryProject/middleware.py

class CSPMiddleware:
    """
    Adds a Content Security Policy header to all responses
    to protect against XSS attacks.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Content-Security-Policy"] = "default-src 'self'; script-src 'self'; style-src 'self';"
        return response
