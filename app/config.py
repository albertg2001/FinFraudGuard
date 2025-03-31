import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    APP_ENV = os.getenv(\"APP_ENV\", \"development\")
    PORT = os.getenv(\"PORT\", 8000)
    MODEL_PATH = os.getenv(\"MODEL_PATH\", \"./models/finfraud_model.pt\")
    # Add other configuration parameters as needed

config = Config()
