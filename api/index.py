def app(environ, start_response):
    chaves = ('PATH_INFO', 'RAW_URI', 'REQUEST_URI', 'QUERY_STRING', 'SCRIPT_NAME')
    linhas = []
    for k, v in sorted(environ.items()):
        if k in chaves or any(p in k for p in ('VERCEL', 'FORWARDED', 'PATH', 'URI', 'HOST')):
            linhas.append(f'{k} = {v}')
    start_response('200 OK', [('Content-Type', 'text/plain; charset=utf-8')])
    return ['\n'.join(linhas).encode('utf-8')]