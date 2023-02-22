import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/")
def get_list():
    return[1,2,3]


@app.get("/contact", response_class= HTMLResponse)
def get_list():
    return """
        <h1> Hola no tengo idea lo que hago ahora </h1>
        <p>soy un parrafo muy corto</p>
    """

def run():
    store.get_categories()


if __name__=="__main__":
    run()