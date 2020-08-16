#If the tornado is still listening to port,stop the execution by following commands
#ps -a
#kill -9 PID
#the pid is provided in previous command.Type only the pid where the command is for python3

import tornado.web 
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("This is a list of http protocols")

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        a=int(self.get_argument("a"))
        if a>=0:
            b="positive"
        else:
            b="negative"
        self.write("The number "+str(a)+" is "+b)

class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self,id):
        self.write("This action takes regular expressions with id "+id)

if __name__ == "__main__":
    app=tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/html",staticRequestHandler),
        (r"/ispositive",queryStringRequestHandler),
        (r"/action/([0-9]+)",resourceRequestHandler)
    ])

    app.listen(8881)
    print("Testing port 8881")
    tornado.ioloop.IOLoop.current().start()

