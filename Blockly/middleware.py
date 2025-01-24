class AddCOOPHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Cross-Origin-Opener-Policy ヘッダーを追加
        response['Cross-Origin-Opener-Policy'] = 'same-origin'
        return response
