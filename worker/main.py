import asyncio
from worker.queue import redis_client, QUEUE_NAME
from worker.job_handler import process_job


async def worker_loop():
    print("Worker started. Waiting for jobs...")

    while True:
        job = redis_client.brpop(QUEUE_NAME, timeout=5)

        if job:
            _, job_id = job
            await process_job(job_id)
        else:
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(worker_loop())
