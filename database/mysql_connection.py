# replace with SQLDatabase.from_uri
import os

from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

load_dotenv()

db = SQLDatabase.from_uri(
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT')}/"
    f"{os.getenv('DB_NAME')}"
)   