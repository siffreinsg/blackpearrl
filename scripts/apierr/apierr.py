import logging
import os
import secrets
import sys
from pathlib import Path

import uvicorn
from dotenv import load_dotenv
from fastapi import Depends, FastAPI, HTTPException

load_dotenv()
app = FastAPI(
    title=os.getenv("SERVER_NAME", "Black Pearl"),
    description="Black Pearrl API",
    version="1.0.0",
)

# Setup logging
LOG_LEVEL = os.getenv("APIERR_LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=LOG_LEVEL, format="[%(asctime)s][%(levelname)s] %(message)s")

# Add the parent directory to the path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

# Import script functions
from notify_disk_usage import notify_usage
from tautulli_notify.tautulli_notify import notify

# Load API key
API_KEY = os.getenv("APIERR_API_KEY")
if not API_KEY or API_KEY == "supersecretkey":
    logging.warn("APIERR_API_KEY has not been set! Please set it to a secure value. Generating a random key for this session.")
    API_KEY = secrets.token_urlsafe(16)
logging.info(f"API key: {API_KEY}")

def check_api_key(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Forbidden")


# ========================
# === ENDPOINTS ===
# ========================
@app.get("/script/tautulli_notify", dependencies=[Depends(check_api_key)])
def tautulli_notify(subject: str, body: str, notifier_id: int | None = None, tautulli_url: str | None = None, tautulli_api_key: str | None = None):
    args = {
        'subject': subject,
        'body': body,
    }

    if notifier_id:
        args["notifier_id"] = str(notifier_id)
    if tautulli_url:
        args["tautulli_url"] = tautulli_url
    if tautulli_api_key:
        args["tautulli_api_key"] = tautulli_api_key

    return notify(**args)


@app.get("/script/disk_usage", dependencies=[Depends(check_api_key)])
def disk_usage():
    _, disk_usage_gb = notify_usage()
    return disk_usage_gb


# ============
# === MAIN ===
# ============
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("APIERR_PORT", 8000)))
