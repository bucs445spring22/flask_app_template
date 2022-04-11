
from src import create_app

#application factory
app = create_app()

if __name__ == "__main__":
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
    )