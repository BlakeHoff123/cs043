import wsgiref.simple_server
import urllib.parse
from lesson2_2.database import Simpledb


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]

    path = environ['PATH_INFO']
    params = urllib.parse.parse_qs(environ['QUERY_STRING'])
    db = Simpledb('db.txt')

    if path == '/insert':
        name = params['key'][0] if 'key' in params else None
        phone = params['value'][0] if 'value' in params else None
        if name and phone:
            db.insert(name, phone)
            message = "inserted"
        else:
            message = 'You must enter a name and a phone.'
        start_response('200 OK', headers)
        return [message.encode()]
    elif path == '/select':
        name = params['key'][0] if 'key' in params else None
        if name:
            phone = db.select_one(name)
            if phone:
                message = phone
            else:
                message = 'Nothing found'
        else:
            message = 'You must enter a name.'
        start_response('200 OK', headers)
        return [message.encode()]

    elif path == '/delete':
        name = params['key'][0] if 'key' in params else None
        if name:
            found = db.delete(name)
            if found:
                message = 'That name was deleted.'
            else:
                message = 'That name was not found.'
        else:
            message = 'You must enter a name.'
        start_response('200 OK', headers)
        return [message.encode()]
    elif path == '/update':
        name = params['key'][0] if 'key' in params else None
        phone = params['value'][0] if 'value' in params else None
        if name:
            old_phone = db.select_one(name)
            if old_phone:
                if phone:
                    db.update(name, phone)
                    message = 'Updated the phone.'
                else:
                    message = 'You must enter a phone'
            else:
                message = 'Nothing found'
        else:
            message = 'You must enter a name'
        start_response('200 OK', headers)
        return [message.encode()]
    else:
        start_response('404 Not Found', headers)
        return ['Status 404: Resource not found'.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
