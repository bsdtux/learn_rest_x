import os
from api.app import create_app


if __name__ == '__main__':
    app = create_app(os.environ.get('APP_ENV', 'development'))
    app.run(debug=app.config.DEBUG)