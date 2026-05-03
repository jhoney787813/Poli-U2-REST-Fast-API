import os
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials, firestore

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Poli U2 REST Fast API"
    FIREBASE_SERVICE_ACCOUNT_PATH: str = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH", "serviceAccountKey.json")

settings = Settings()

def init_firebase():
    """Initializes Firebase Admin SDK."""
    if not firebase_admin._apps:
        # Check if the service account file exists
        if os.path.exists(settings.FIREBASE_SERVICE_ACCOUNT_PATH):
            cred = credentials.Certificate(settings.FIREBASE_SERVICE_ACCOUNT_PATH)
            firebase_admin.initialize_app(cred)
        else:
            # Fallback to default credentials (e.g., if running on GCP or if env vars are set)
            # This is useful for production environments like Render/Azure
            firebase_admin.initialize_app()
    
    return firestore.client()
