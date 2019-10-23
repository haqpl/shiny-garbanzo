#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import unquote_plus
from shlex import quote
import subprocess
import sys
import argparse

def Parse_args():
    parser = argparse.ArgumentParser(description='Non-HTTP sqlmap proxy')
    parser.add_argument("--host", default="127.0.0.1", help="IP to listen on.")
    parser.add_argument("--port", type=int, default=31337, help="Port to listen on.")
    parser.add_argument("--tool", help="Tool to use for non-HTTP communication.")
    parser.add_argument("--arguments", help="Arguments passed to interesting tool, use SQLMAP token to pass SQLMAP's input there.", type=str, nargs='*')
    args = parser.parse_args()
    return args

def Assembly_cmd(sqlmap_input):
    cmd = str(known_args.tool + " " + known_args.arguments[0]).replace("SQLMAP", "{"+sqlmap_input+"}")
    return cmd

class Proxy(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            cl = int(self.headers.get("content-length"))
            body = self.rfile.read(cl).decode()
            sqlmap_input = quote(unquote_plus(body.split("=", 1)[1]))
            cmd = Assembly_cmd(sqlmap_input)
            cmd_result = subprocess.check_output(
                cmd, shell=True
            )
            self.send_response(200)
            self.end_headers()
            self.wfile.write(cmd_result)
        except Exception:
            self.send_error(500)

known_args = Parse_args()

print("[i] Starting server on %d PORT" % known_args.port)
print("Start with this:")
print("sqlmap -u \"%s\" --data \"cmd=\" -p \"cmd\" --method POST" % (known_args.host +":"+ str(known_args.port)))
with HTTPServer((known_args.host, known_args.port), Proxy) as httpd:
    httpd.serve_forever()
