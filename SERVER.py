from http.server import HTTPServer, BaseHTTPRequestHandler
import logging
import urllib.parse
from pathlib import Path
import base64
import CNN_train as CN
import os
class SHTPRH(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		url_parts = urllib.parse.urlparse(self.path)
		req_path = Path(url_parts.strip("/"))
		if not req_path.is_file():
			self.path = "index.html"
		else:
			with open(req_path, "rb") as fh:
				html = fh.read()
				self.wfile.write(html)
		CN.run_test()
		print(type(os.listdir()))

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length)
		with open("picture.png", 'wb') as fh:
			fh.write(base64.decodebytes(post_data[22:]))
		logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",str(self.path), str(self.headers), post_data.decode('utf-8'))
		self.send_response(200)
		self.end_headers()

httpd = HTTPServer(('localhost', 4443), SHTPRH)

httpd.serve_forever()
