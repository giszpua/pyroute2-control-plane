import os
import time

node = os.getenv("NODE_NAME", "unknown")

while True:
    print(f"[control-plane] running on node={node}")
    time.sleep(10)