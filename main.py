from flask import Flask
import routes

app = Flask(__name__)
routes.register(app)

if __name__ == '__main__':
      app.run(debug=True)
