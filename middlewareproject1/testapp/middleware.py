class ExecutionFlowMiddleware(object):

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed at pre processing of request')
        response = self.get_response(request)
        print('This line is printed at post processing of request')
        return response

from django.http import HttpResponse
class AppMaintananceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return HttpResponse('<h1>Currently Application under maintanance.... Please try After 2 Days !!!!</h1>')

class ErrorMessegeMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response

    def process_exception(self,request,exception):
        s1='<h1>Currrently we are facing  some technical problems, plz try after some time</h1><hr>'
        s2='<h2>Raised Exception:{}</h2>'.format(exception.__class__.__name__)
        s3='<h3>Exception Description/Messege:{}</h2>'.format(exception)

        return HttpResponse(s1+s2+s3)

class FirstMiddleware(object):

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed by first Middleware at Pre-Processing of request')
        response = self.get_response(request)
        print('This line printed by first Middleware at Post-Processing of request')
        return response

class SecondMiddleware(object):

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed by Second Middleware at Pre-Processing of request')
        response = self.get_response(request)
        print('This line printed by Second Middleware at Post-Processing of request')
        return response

class ThirdMiddleware(object):

    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        print('This line printed by Third Middleware at Pre-Processing of request')
        response = self.get_response(request)
        print('This line printed by Third Middleware at Post-Processing of request')
        return response
