import uvicorn

from fastapi import FastAPI
from routes.route1 import router1


app = FastAPI()
app.include_router(prefix='/route1', router=router1)


@app.get('/')
def root():
    """
    docstring for root
    """
    return {
        'status': "I'm Alive!", "code": 200
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=9999)
