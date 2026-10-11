import os
import sys
from urllib.parse import urlsplit

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.wsgi import application


def app(environ, start_response):
    # A Vercel reescreve a URL para /api/index; aqui restauramos o caminho original
    original = (
        environ.get('HTTP_X_VERCEL_FORWARDED_PATH')
        or environ.get('HTTP_X_MATCHED_PATH')
        or environ.get('HTTP_X_INVOKE_PATH')
    )
    if original:
        path = urlsplit(original).path
        if path and not path.startswith('/api/index'):
            environ['PATH_INFO'] = path
            environ['RAW_URI'] = original
    return application(environ, start_response)