#If the tornado is still listening to port,stop the execution by following commands
#ps -a
#kill -9 PID
#the pid is provided in previous command.Type only the pid where the command is for python3

import tornado.web 
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello,World")

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n=int(self.get_argument("n"))
        r="odd" if n%2 else "even"
        self.write("The number "+str(n)+" is "+r)

class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self,id):
        self.write("Querying tweet with id "+id)

if __name__ == "__main__":
    app=tornado.web.Application([
        (r"/",basicRequestHandler),
        (r"/blog",staticRequestHandler),
        (r"/isEven",queryStringRequestHandler),
        (r"/tweet/([0-9]+)",resourceRequestHandler)
    ])

    app.listen(8881)
    print("Im listening on port 8881")
    tornado.ioloop.IOLoop.current().start()

