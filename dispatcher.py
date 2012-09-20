import re


class Dispatcher(object):

    @staticmethod
    def notfound(environ, start_response):
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ''

    def __init__(self):
        self._routes = []
        self.notfound = Dispatcher.notfound

    def route(self, route, method='GET'):
        def wrapper(target):
            _route = re.sub(r'{(\w+)}', r'(?P<\1>\w+)', route)
            _route = re.compile('%s$' % _route)
            self._routes.append((_route, method, target))
            return target
        return wrapper

    def __call__(self, environ, start_response):
        for route, method, target in self._routes:
            m = route.match(environ['PATH_INFO'])
            if m and method == environ['REQUEST_METHOD']:
                environ['dispatcher.args'] = m.groupdict()
                return target(environ, start_response)
        return self.notfound(environ, start_response)
