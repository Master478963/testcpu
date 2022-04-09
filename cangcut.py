import time


ativar = True #@param {type:'boolean'}

temps = 0
sec = 360
while(temps < 43200):
  if(temps == sec):
    sec += 360
    x = (temps/60)/60
    print("pass",x," minute")
  time.sleep(1)
  temps += 1
