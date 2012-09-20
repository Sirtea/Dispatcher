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
