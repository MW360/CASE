#!/usr/bin/python2

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import parse_qs
import cgi

class GP(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    def do_HEAD(self):
        self._set_headers()
    def do_GET(self):
        self._set_headers()
        print self.path
        parse_a = parse_qs(self.path[2:]) #{'bin': ['go'], 'foo': ['bar']}
        print parse_a
        if 'id' in parse_a:
            p_path = parse_a['id'][0] #'w1.json'
            print p_path
            try:
                with open(p_path) as f:
                    read_data = f.read()
                self.wfile.write(read_data)
            except:
                self.send_error(404, "File not found: '%s'" % p_path) 
        else:
            self.send_error(404, "GET-Option not found: %s" % parse_a) 
            
    def do_POST(self):
        self._set_headers()
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )
        w_id = form.getvalue('id')
        content = form.getvalue('content')
        if w_id != None:
            if content != None:
                try:
                    f = open(w_id, "w")
                    f.write(content)
                    f.close()
                    self.wfile.write("<html><body><h1>POST Request Received!</h1><p>wrote to file '%s'</body></html>" % w_id)
                    
                    #main loop.update(w_id)
                    #print "updated the workflow or script"
                    
                except:
                    self.send_error(404, "Error writing file: '%s'" % w_id)
            else:
                self.send_error(404, "'content' not found: '%s'" % form)
        else:
            self.send_error(404, "'id' not found: '%s'" % form)

def run(server_class=HTTPServer, handler_class=GP, port=8088):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server running at localhost:8088...'
    httpd.serve_forever()

run()
