import os, json
from platformdirs import user_data_dir

APP_NAME = "ruptrk-cli"
APP_AUTHOR = "Aoishik"

BASE_DIR = user_data_dir(APP_NAME, APP_AUTHOR)  # safe across upgrades
CONFIG_DIR = BASE_DIR
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")


def ensure_config_dir():
    os.makedirs(CONFIG_DIR, exist_ok=True)


def load_config():
    ensure_config_dir()
    if not os.path.exists(CONFIG_FILE):
        return {}
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}


def save_config(cfg):
    ensure_config_dir()
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)


def get_default_db():
    return load_config().get("default_db")


def set_default_db(dbname):
    cfg = load_config()
    cfg["default_db"] = dbname
    save_config(cfg)


def get_db_path(dbname: str) -> str:
    ensure_config_dir()
    if not dbname.endswith(".db"):
        dbname = f"{dbname}.db"
    return os.path.join(CONFIG_DIR, dbname)


def list_dbs():
    ensure_config_dir()
    return [f for f in os.listdir(CONFIG_DIR) if f.endswith(".db")]
