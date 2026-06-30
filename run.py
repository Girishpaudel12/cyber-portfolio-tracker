import os
from app import create_app
from config import DevelopmentConfig, ProductionConfig

env = os.environ.get("FLASK_ENV", "development")
config_class = ProductionConfig if env == "production" else DevelopmentConfig

app = create_app(config_class)

if __name__ == "__main__":
    app.run(debug=config_class.DEBUG)
