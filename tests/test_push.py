
def test_push_handler_callable(dogu_handler):
    def application(environ, start_response):
        assert environ.get('dogu.push') is not None
        assert hasattr(environ.get('dogu.push'), '__call__')

        def push_application(environ, start_response):
            return bytearray()

        environ['dogu.push']([('Accept', 'text/html, text/css')], push_application)

        return bytearray()

    dogu_handler(application)


def test_push_enabled_valid(dogu_handler):
    def application(environ, start_response):

        assert environ['dogu.push_enabled']

        if environ['PROTOCOL_VERSION'] <= 'HTTP/1.1':
            assert environ['dogu.push_enabled'] is False

        return bytearray()

    dogu_handler(application)
