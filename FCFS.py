import os
import time
clear = lambda:os.system('clear')
process = []
arrival = []
burst = []
timeElapsed = []
completeTime = []
alloc = []
done = []
tat = []
wt = []

#functions
def header():
  print("FL-ACT5: Processor Management - SJN")
  print("Programmmed by: Alcazar, Faye Therese Simone L.")
  print("==========================================================\n")

def cls():
  input("\nPress ENTER to continue...")
  clear()

#input
header()
print("PROCESS")
ok = 1
while ok != 0:
  processNum = input(" > Input number of Processes: ")
  if processNum.isnumeric() and str(processNum) != '0':
    processNum = int(processNum)
    ok = 0
  else:
    print("Error! Invalid input. Please input again.\n")
for i in range(0, processNum):
  process.append("P" + str(i+1))
  
print("\nARRIVAL TIME(AT) & BURST TIME(BT)")
print(" Input the respective AT & BT for each process:\n")
for i in range(0,processNum):
  print("P" + str(i+1) + " :")
  ok = 1
  while ok != 0:
    arrivalTime = input(" > Arrival Time: ")
    if arrivalTime.isnumeric():
      arrival.append(int(arrivalTime))
      ok = 0
    else:
      print("Error! Invalid input. Please input again.\n")    
  ok = 1
  while ok != 0:
    burstTime = input(" > Burst Time: ")
    if burstTime.isnumeric():
      burst.append(int(burstTime))
      ok = 0
    else:
      print("Error! Invalid input. Please input again.\n")
  print(" ")
cls()
timeElapsed.append(0)
t = 0 #for time elapsed
c = 0 #for completion time
#allocation
while len(done) != processNum:
  ok = 1
  min1 = max(burst)
  for j in range(0, processNum):
    if process[j] not in done and min1 >= burst[j] and arrival[j] <= timeElapsed[t]:
      min1 = burst[j]
      minIndex = j
        
  for i in range(0, processNum):
    if process[i] in done:
      continue
    elif arrival[i] <= timeElapsed[t] and burst[minIndex] == burst[i]:
      alloc.append("P" + str(i+1))
      timeElapsed.append(timeElapsed[t]+burst[i])
      completeTime.append(timeElapsed[t]+burst[i])
      tat.append(abs(completeTime[c]-arrival[i]))
      wt.append(abs(tat[c]-burst[i]))
      done.append(process[i])
      ok = 0
      t = t+1
      c = c+1
    else:
      continue
  
  if ok == 1:
    alloc.append('idle')
    min1 = max(arrival)
    for i in range(0, processNum):
      if process[i] not in done and min1 >= arrival[i]:
        min1 = arrival[i]
        minIndex = i
    timeElapsed.append(timeElapsed[t]+arrival[minIndex])
    t = t+1
  
  #display
  #process list
  header()
  print("PROCESS LIST")
  if len(timeElapsed) == 1:
    time.sleep(0.50)
  print("________________________________________")
  print(" Process | Arrival Time  | Burst Time")
  for i in range(0, processNum):
    print("    " + str(process[i]) + "\t |\t" + str(arrival[i]) + "\t |\t" + str(burst[i]))

  #timeline
  timeline = []
  for i in range(0,len(alloc)):
    if alloc[i] == 'idle':
      timeline.append('|-idle-|')
    else:
      timeline.append('|--'+ alloc[i] +'--|')
      
  if len(timeElapsed) == 1:
    input("\nPress ENTER to show TIMELINE...\n")
  else:
    print("\nPress ENTER to show TIMELINE...\n")
  print("TIMELINE\n")
  if len(timeElapsed) == 1:
    time.sleep(0.50)

  print("\t".join(str(timeElapsed[i]) for i in range(0, len(timeElapsed))))
  print(" "+"".join(str(timeline[i]) for i in range(0, len(timeline))))
  cls()

#summary
header()
print("PROCESS LIST")
print("________________________________________")
print(" Process | Arrival Time  | Burst Time")
for i in range(0, processNum):
  print("    " + str(process[i]) + "\t |\t" + str(arrival[i]) + "\t |\t" + str(burst[i]))
    
print("\nPress ENTER to show TIMELINE...\n")
print("TIMELINE\n")

print("\t".join(str(timeElapsed[i]) for i in range(0, len(timeElapsed))))
print(" "+"".join(str(timeline[i]) for i in range(0, len(timeline))))

print("\n==========================================================")
print("CONCLUSION")
averageTAT = sum(tat)/processNum
averageWT = sum(wt)/processNum
print(" > Average Turnaround Time: " + str(round(averageTAT,2)))
print(" > Average Waiting Time: " + str(round(averageWT,2)))