# implement exponential backoff

import time

attempts=0
wait_time=1
retries=5

while attempts<retries:
  print(f'Attempt {attempts+1}: wait time {wait_time} sec')
  time.sleep(wait_time)
  attempts+=1
  wait_time*=2