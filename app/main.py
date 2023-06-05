from fastapi import FastAPI
from .sockets import sio_app
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*', 'http://127.0.0.1:3000/',
                   'http://127.0.0.1:3000/',
                   'https://new-try-react-fast.herokuapp.com/',
                   'https://new-try-react-fast.herokuapp.com'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/home')
async def home():
    return {'message': 'Hello Developers'}


@app.get('/tyy')
async def yum():
    return {'message': 'Hello Developers'}

app.mount('/', app=sio_app)
