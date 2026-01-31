import time
from fastapi import Request 

async def timing_middleware(request:Request, call_next_):
    start = time.perf_counter()
    response = await call_next_(request)
    response.headers["X-Process-Time"] = f"{time.perf_counter() - start:.4f}"
    return response