from fastapi import FastAPI


from .routers import tmp


app = FastAPI()

app.include_router(tmp.router)