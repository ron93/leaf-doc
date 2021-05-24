#!venv/bin/python
from app import app
app.config.from_object('config.DevelopmentConfig')


app.run(host='0.0.0.0', port=4000, debug=True)