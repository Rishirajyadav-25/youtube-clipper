# from fastapi import FastAPI
# import threading
# from worker.main import start_worker

# app = FastAPI()

# @app.get("/")
# def health():
#     return {"status": "worker running"}

# def run_worker():
#     start_worker()

# # Start Redis worker in background thread
# threading.Thread(target=run_worker, daemon=True).start()



from fastapi import FastAPI
import threading

from worker.main import start_worker

app = FastAPI()

@app.get("/")
def health():
    return {"status": "worker running"}

threading.Thread(target=start_worker, daemon=True).start()
