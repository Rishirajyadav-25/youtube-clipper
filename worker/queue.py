import os
import asyncio
from redis import asyncio as aioredis  # Use the async version of Redis
from worker.job_handler import process_job

# 1. Load and Verify URL
REDIS_URL = os.getenv("REDIS_URL")
if not REDIS_URL:
    raise RuntimeError("REDIS_URL is not set in environment")

# 2. Setup Async Redis Client
# Note: Since REDIS_URL starts with rediss://, SSL is handled automatically.
redis_client = aioredis.from_url(
    REDIS_URL,
    decode_responses=True
)

QUEUE_NAME = "clip_jobs"

async def listen_for_jobs():
    """
    Async loop that waits for jobs from Redis without blocking the whole program.
    """
    print("📡 Worker started. Listening for jobs on Redis queue...")
    
    while True:
        try:
            # blpop in aioredis returns a tuple: (queue_name, value)
            # It "awaits" here without freezing the CPU
            result = await redis_client.blpop(QUEUE_NAME, timeout=0)
            
            if result:
                _, job_id = result
                print(f"📥 Received job: {job_id}")

                # ✅ Simply await the job. No need for asyncio.run()
                await process_job(job_id)
                print(f"✅ Finished job: {job_id}")

        except Exception as e:
            print(f"❌ Worker error: {e}")
            # Wait a bit before retrying if Redis connection fails
            await asyncio.sleep(5)

if __name__ == "__main__":
    # Start the async event loop once
    try:
        asyncio.run(listen_for_jobs())
    except KeyboardInterrupt:
        print("Stopping worker...")








# import os
# import redis
# import time
# import asyncio
# # from dotenv import load_dotenv

# from worker.job_handler import process_job

# # Load environment variables
# # load_dotenv()

# REDIS_URL = os.getenv("REDIS_URL")
# if not REDIS_URL:
#     raise RuntimeError("REDIS_URL is not set in environment")

# redis_client = redis.Redis.from_url(
#     REDIS_URL,
#     decode_responses=True,
#     # ssl=True,
#     # ssl_cert_reqs=None
# )


# QUEUE_NAME = "clip_jobs"


# def listen_for_jobs():
#     """
#     Blocking loop that waits for jobs from Redis
#     """
#     print("📡 Listening for jobs on Redis queue...")

#     while True:
#         try:
#             # BLPOP blocks until a job is available
#             _, job_id = redis_client.blpop(QUEUE_NAME)
#             print(f"📥 Received job: {job_id}")

#             # ✅ Run async job correctly
#             asyncio.run(process_job(job_id))
#             # asyncio.run(process_job(job_id))

#         except Exception as e:
#             print(f"❌ Worker error: {e}")
#             time.sleep(5)






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
