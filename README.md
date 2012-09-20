# Dispatcher

Dispatcher is a WSGI layer that pretends to perform URI and method based routing .

## How to use Dispatcher
An instance of the Dispatcher object is a WSGI application that behaves like a WSGI callable. Once the WSGI server calls a Dispatcher instance, the callable method passes the call to another WSGI callable, based on the URI and the method. It can also capture segments of the URI as routing parameters. The routing tables is populated through a python decorator. Learn by example:

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

## How to assign a callable to a URI and method
The Dispatcher object has a decorator `route` that accepts an URI and optionally a method. This decorator wraps the WSGI callable that will be used as target in a matching situation.

## Routing process
When the Dispatcher object is called, the `__call__` method will try to match every combination of URI and HTTP method, calling the target that corresponds to this combination, as the method `route` indicates. The first combination found will end the process, but the rules order is not guaranteed. In case of no matching found, the `__call__` method will call the `notfound` property of the Dispatcher object, that can be overwritten. Every matching segment in the URI will be found at `environ['dispatcher.args']` in the target callable.

## Segment matching
Every URI rule in the decorator `route` is a string, but accepts variables that will be found later in `environ['dispatcher.args']`. To define this arguments, is enough to put the argument name between braces, like this: `{name}`. Currently, an argument accepts any string of one or more alphanumeric character (`[a-zA-Z0-9_]+`)

As an example if the rule was `'/show/{year}/{month}'`, the URI `'/show/2012/09'` would match, and the contents of `environ['dispatcher.args']` would be a python dictionary containing `{'year': '2012', 'month': '09'}.`
