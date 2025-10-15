import os
from lotusrpg import create_app
from flask_cors import CORS

app = create_app()
origins = os.getenv("CORS_ORIGINS", "http://localhost:3000,https://lotusrpg.fly.dev").split(",")
CORS(app, resources={r"/api/*": {"origins": [o.strip() for o in origins]}})

if __name__ == "__main__":
    app.run(debug=True)