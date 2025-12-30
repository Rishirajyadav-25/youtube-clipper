from motor.motor_asyncio import AsyncIOMotorClient 
from app.core.config import settings
import os
import ssl


MONGODB_URI=settings.MONGODB_URI

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

client = AsyncIOMotorClient(
    MONGODB_URI,
    tls=True,
    ssl_context=ssl_context,
)

db = client.youtube_clipper