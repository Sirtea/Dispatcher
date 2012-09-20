Dispatcher
==========

Dispatcher is a WSGI layer that pretends to perform URI and method based routing .

# How to use Dispatcher
An instance of the Dispatcher object is a WSGI application that behaves like a WSGI callable.

Once the WSGI server calls a Dispatcher instance, the callable method passes the call to another WSGI callable, based on the URI and the method. It can also capture segments of the URI as routing parameters. The routing tables is populated through a python decorator.

Learning by example:

```python
from dispatcher import Dispatcher

app = Dispatcher()


@app.route('/')
def app1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    yield 'Hello World!\n'


@app.route('/show/{id}')
def app2(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    args = environ['dispatcher.args']
    yield 'Showing element %s\n' % args['id']
```
