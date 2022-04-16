import os

BOT_NAME = os.environ.get("BOT_NAME", "Img")
CSE_KEY = os.environ.get("CSE_KEY", "AIzaSyAOwCwFthTiWetXPeF23a6qOodf_1zn0eg")
CSE_CX = os.environ.get("CSE_CX", "29c252a559c43ec88")
API_TOKEN = os.environ.get("API_TOKEN", "5104307142:AAFW-V-WmTyb58a4qABgKGhmFDBQsjrDXNo")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL", "")
NGINX_SUBPATH = os.environ.get("NGINX_SUBPATH", "")
BATCH = int(os.environ.get("BATCH", 10))
POLLING = bool(os.environ.get("POLLING", False))
