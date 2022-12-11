# import base64
# import io
from http.server import BaseHTTPRequestHandler

# from PIL import Image


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """
        im = Image.open("wp.jpg")

        bytes_io = io.BytesIO()
        im.save(bytes_io, format="JPEG")

        self.send_response(200)
        self.send_header("Content-type", "image/jpeg")
        self.end_headers()
        self.wfile.write(base64.b64encode(bytes_io.getvalue()).decode("UTF-8"))
        """

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Hello, wp!".encode("utf-8"))

        return
