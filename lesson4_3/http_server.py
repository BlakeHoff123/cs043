import wsgiref.simple_server


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8'), ('name', 'dolc')]
    start_response('200 OK', headers)
    return ['Hello world?'.encode(), ' Bye'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()