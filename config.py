
from pathlib import Path

# Project root: COSS/
BASE_DIR = Path(__file__).resolve().parent

# Directories
APP_DIR = BASE_DIR / "app"
DATABASE_DIR = BASE_DIR / "database"
DATA_DIR = BASE_DIR / "data"

# Database files
DATABASE_PATH = DATA_DIR / "coss.db"
SCHEMA_PATH = DATABASE_DIR / "schema.sql"
SEED_PATH = DATABASE_DIR / "seed.sql"

# Database settings
DATABASE_TIMEOUT = 10