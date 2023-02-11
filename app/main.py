import uvicorn

from fastapi import FastAPI
from app.routes.route1 import router1


app = FastAPI()
app.include_router(prefix='/test-route', router=router1)


@app.get('/', status_code=200)
def root():
    """
    docstring for root
    """
    return {
        'status': "I'm Alive!"
    }


if __name__ == "__main__":
    uvicorn.run("main:app", port=9999)
