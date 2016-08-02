#!/bin/env python
#coding=utf-8
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/vendor/')

import tornado
import tornado.ioloop
import tornado.web
import tornado.options

from controller.base import WebRequest
from controller.base import WebSocket

class MainHandler(WebRequest):
    def get(self):
        self.finish("It's jes6ka_box, welcome!")
        
class ToolsVrPhotoHandler(WebRequest):
    @tornado.gen.coroutine
    def get(self):
        self.title = self.get_argument("title",u"HOTPOOR · Panorama")
        self.url = self.get_argument("url",None)
        self.move = self.get_argument("move",u"false")
        self.target_x = self.get_argument("target_x",0)
        self.target_y = self.get_argument("target_y",0)
        self.target_z = self.get_argument("target_z",0)
        if self.url:
            self.render("template/tools/webgl_panorama_dualfisheye.html")
            return
        else:
            self.render("template/tools/error.html")
            return

settings = {
    "static_path":os.path.join(os.path.dirname(__file__),"static"),
    "cookie_secret": "hotpoorinchina"
    }

application = tornado.web.Application([
        (r"/tools/vr_photo", ToolsVrPhotoHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
        (r"/(.*)", MainHandler),
    ], **settings)

if __name__ == "__main__":
    tornado.options.define("port", default=8888, help="Run server on a specific port", type=int)
    tornado.options.parse_command_line()
    application.listen(tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()