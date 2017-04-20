from flask import Flask, Response, request
app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=('GET', 'POST'))
@app.route('/<path:path>', methods=('GET', 'POST'))
def catch_all(path):
    print('******** NEW REQUEST ********')
    print('PATH: %s' % path)
    print('HEADERS:')

    for k, v in request.headers.items():
        print '  %s %s' % (k, v)

    if request.method == 'POST':
        if len(request.data) > 0:
            print('BODY: %s' % request.data)
        if len(request.form) > 0:
            print('FORM: %s' % request.form)
        if len(request.files) > 0:
            print('FILES: %s' % request.files)

        content_type = request.headers.get('Content-Type')
        if content_type == 'application/xml':
            return Response('<status>OK</status>', content_type='application/xml')
        elif content_type == 'application/json':
            return Response('{"status": "OK"}', content_type='application/json')

    return Response('OK', content_type='text/plain')


if __name__ == '__main__':
    app.run(port=8099)
