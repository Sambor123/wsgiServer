import os

def app(environ, start_response):
    """A barebones WSGI application.
 
    This is a starting point for your own Web framework :)
    """
    start_response('200 OK', [('Content-Type', 'text/html')])
    body=''
    if environ['PATH_INFO'][1:].endswith('.html'):
    	if os.path.exists(environ['PATH_INFO'][1:]):
    		file=open(environ['PATH_INFO'][1:])
	    	try:
	    		all_the_text=file.read()
	    	finally:
	    		file.close()
	    	body=all_the_text
    	else:
    		body='404 Not Found!'
    	
    else:
    	body = '<h1>Hello %s</h1>' % environ['PATH_INFO'][1:]
    return [body.encode('utf-8')]