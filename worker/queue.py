import os
import redis
import time
from dotenv import load_dotenv

from worker.job_handler import process_job

# Load environment variables
load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    raise RuntimeError("REDIS_URL is not set in environment")

redis_client = redis.Redis.from_url(
    REDIS_URL,
    decode_responses=True
)

QUEUE_NAME = "clip_jobs"


def listen_for_jobs():
    """
    Blocking loop that waits for jobs from Redis
    """
    print("📡 Listening for jobs on Redis queue...")

    while True:
        try:
            # BLPOP blocks until a job is available
            _, job_id = redis_client.blpop(QUEUE_NAME)
            print(f"📥 Received job: {job_id}")

            # Process the job
            process_job(job_id)

        except Exception as e:
            print(f"❌ Worker error: {e}")
            time.sleep(5)









# import os
# import redis
# from dotenv import load_dotenv

# # Load environment variables from .env
# load_dotenv()

# REDIS_URL = os.getenv("REDIS_URL")

# if not REDIS_URL:
#     raise RuntimeError("REDIS_URL is not set in environment")

# redis_client = redis.Redis.from_url(
#     REDIS_URL,
#     decode_responses=True
# )

# QUEUE_NAME = "clip_jobs"
