from motor.motor_asyncio import AsyncIOMotorClient 
from app.core.config import settings
import ssl

MONGODB_URI = settings.MONGODB_URI

# Modern approach for Motor/PyMongo 4.x+
client = AsyncIOMotorClient(
    MONGODB_URI,
    tls=True,
    # ssl_context is now tlsContext
    tlsContext=ssl.create_default_context(),
    # These replace the manual ssl_context edits
    tlsAllowInvalidHostnames=True,
    tlsAllowInvalidCertificates=True
)

db = client.youtube_clipper