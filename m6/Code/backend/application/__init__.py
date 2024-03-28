from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from application.config import LocalDevelopmentConfig
from application.models import db
# from application.models import User, Role
from application import workers
# from flask_caching import Cache
from algoliasearch.search_client import SearchClient
from dotenv import load_dotenv


app = None
api = None
celery = None
# cache = None

def create_app(conf=LocalDevelopmentConfig):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(conf)
    db.init_app(app)
    app.app_context().push()
    app.logger.info("App setup complete")
    db.create_all()
    app.app_context().push()
    api = Api(app)
    app.app_context().push()
    CORS(app, resources={r'/*':{'origins':'*'}})
    app.app_context().push()
    # create celery
    celery = workers.celery
    celery.conf.update(
        broker_url = app.config['CELERY_BROKER_URL'],
        result_backend = app.config['CELERY_RESULT_BACKEND']
    )
    celery.Task = workers.ContextTask
    app.app_context().push()

    # cache = Cache(app)
    # cache.clear()
    # app.app_context().push()

    return app,api,celery

app,api,celery = create_app()

client = SearchClient.create("K26CF5W1OF", LocalDevelopmentConfig.SEARCH_API_KEY)
index = client.init_index('seproject')

# export ALGOLIA_API_KEY="db82374734d1c6c6357fc188fc040927"
# Discourse API Key -
# 357e339fd825907f23f741bb333e9de0f8ddcd7b12b8b7d5f9f5c08f5302b30a
