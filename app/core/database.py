from .config import init_firebase

# Singleton for Firestore client
db = init_firebase()

def get_db():
    """Returns the Firestore client instance."""
    return db
