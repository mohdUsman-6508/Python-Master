import time

secret='password'
num_of_attempts=5
waiting_time=1
temp = num_of_attempts

while temp>0:
  
  print("Waiting for ",waiting_time, "s")
  time.sleep(waiting_time)
  
  user_input_secret=input("Enter secret key: ")  
  if secret==user_input_secret:
    print("Access Granted!")
    exit()
  else:
    waiting_time*=2
  temp-=1
    
print("Access Denied!")