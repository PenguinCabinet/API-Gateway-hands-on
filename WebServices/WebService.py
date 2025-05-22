from http.server import BaseHTTPRequestHandler
import socketserver
import os


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(
            "WebService {}\nThis is working on hostname {}".format(
                os.getenv("SERVICE_ID"), os.uname()[1]
            ).encode()
        )


socketserver.TCPServer(("", 13000), MyHandler).serve_forever()
