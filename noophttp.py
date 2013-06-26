import os

import socket
import tornado.ioloop
import tornado.web
from opster import command


class EmptyHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("")

application = tornado.web.Application([
    (r"/.*", EmptyHandler),
])


@command(usage='-a ADDRESS -p PORT')
def start(port=('p', 80, 'Port to listen to'),
          address=('a', '0.0.0.0', 'Address to bind to')):
    try:
        application.listen(address=address, port=port)
    except socket.error, e:
        print "Error binding to the port: {error}.".format(error=e.strerror)
        if port < 1024 and os.geteuid() != 0:
            print ("You need to be root to listen to port {port}."
                   .format(port=port))
        return
    tornado.ioloop.IOLoop.instance().start()
