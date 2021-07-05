import wsgiref.simple_server
import urllib.parse
from random import randint

luckyNumber = randint(0,26)
result = ' '


def application(environ, start_response, result=result):
    if environ['QUERY_STRING']:
        params = urllib.parse.parse_qs(environ['QUERY_STRING'])
        if 'guess' in params:
            user_guess = int(params['guess'][0])
            if luckyNumber == user_guess:
                result = '<p>You guessed the number!</p>'
            else:
                result = '<p>You guessed wrong...try again.</p>'

    page = '''<!DOCTYPE html>
<html>
<head><title>NumberGame</title></head>
<body>
<h1>A web form</h1>
<form action="/login">
    Guess <input type="number" name="guess" value="Enter a number"><br>
    <input type="submit" name="thebutton" value="Submit">
</form>
<hr>
<p>QUERY_STRING: {}</p>
<hr>
<p>Lucky Number: {}</p>
</body></html>'''.format(environ['QUERY_STRING'], luckyNumber) + result

    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])

    return [page.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()
