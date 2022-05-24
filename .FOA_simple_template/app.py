from flask_openapi3 import OpenAPI
from flask_openapi3 import Info
from views.book import api

info = Info(title='book API', version='1.0.0')
app = OpenAPI(__name__, info=info)

app.secret_key = "keep calm"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True


# register api
app.register_api(api)

if __name__ == '__main__':
    from instances.db import db
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.run(debug=True)
