import requests
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/')
def index(request: Request):
    return templates.TemplateResponse('index.html', {
        'request': request,
        'greeting':'Hello Dear, lets explore Central Asia.'
        })
  
@app.get('/countries')
def CA_countries():
    return 'qazaqstan','ozbekiston','kyrgyzstan','turkmenistan','tadjikistan'

class RequestAPI:
     url = 'https://api.quotable.io/random'
     
     def get_quote(self):
        result = requests.get(self.url).json()
        return result
        
     def get_content(self):
        quote =self.get_quote()
        return quote['content']

     def get_author(self):
        author =self.get_quote()
        return author['author']

my_request = RequestAPI()
    
@app.get('/countries/{country}')
def quote(request: Request,country):
    parameters = { 
        'request': request,
        'country': country.capitalize(),
        'content': my_request.get_content(),
        'author': my_request.get_author()
    }
    return templates.TemplateResponse('quote.html',parameters)