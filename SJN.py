import os
import time
clear = lambda:os.system('clear')
process = []
arrival = []
burst = []
burstReduced = []
timeElapsed = []
completeTime = []
alloc = []
done = []
tat = []
wt = []
queue=[]

#functions
def header():
  print("FL-ACT5: Processor Management - SJN")
  print("Programmmed by: Alcazar, Faye Therese Simone L.")
  print("======================================================================\n")

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
  process.append(i+1)
  
print("\nARRIVAL TIME(AT) & BURST TIME(BT)")
print(" Input the respective AT & BT for each process:\n")
for i in range(0,processNum):
  print("P" + str(process[i]) + " :")
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
      burstReduced.append(int(burstTime))
      ok = 0
    else:
      print("Error! Invalid input. Please input again.\n")
  print(" ")
cls()
t = 0 #time passed
timeElapsed.append(0) #for timeline
burstSum = sum(burst)
currentProcess = 0
idleTime = 0
#allocation
while len(done) != processNum:
  ok = 1
  min1 = max(burst)
  for j in range(0, processNum):
    if process[j] not in done and min1 >= burstReduced[j] and arrival[j] <= t:
      min1 = burstReduced[j]
      minIndex = j

  for i in range(0, processNum):
    if process[i] in done:
      continue
    elif arrival[i] <= t and burstReduced[minIndex] == burstReduced[i]:
      ok = 0
      
      if len(alloc) == 0:
        alloc.append("P" + str(i+1))
        currentProcess = process[i]
        burstReduced[i] = burstReduced[i]-1
        break
        
      elif process[i] == currentProcess:
        burstReduced[i] = burstReduced[i]-1
        break
        
      elif process[i] != currentProcess:
        burstReduced[i] = burstReduced[i]-1
        alloc.append("P" + str(i+1))
        currentProcess = process[i]
        timeElapsed.append(t)
        break
    else:
      continue
    
  if ok == 1:
    alloc.append('idle')
    min1 = max(arrival)
    for i in range(0, processNum):
      if process[i] not in done and min1 >= arrival[i]:
        min1 = arrival[i]
        minIndex = i
    idleTime = idleTime+arrival[minIndex]
    t = t+arrival[minIndex]-1
    
  for b in range(0, processNum):
    if burstReduced[b] == 0 and process[b] not in done:
      completeTime.append(t+1)
      done.append(process[b])
  t = t+1
  
#display
#process list
display = []
displayTime = []
displayTime.append(0)

for d in range(1,len(timeElapsed)+1):
  display.append(alloc[d-1])
  if d != len(timeElapsed):
    displayTime.append(timeElapsed[d])
  else:
    displayTime.append(burstSum+idleTime)
    
  header()
  print("PROCESS LIST")
  if len(displayTime) == 1:
    time.sleep(0.50)
  print("________________________________________")
  print(" Process | Arrival Time  | Burst Time")
  for i in range(0, processNum):
    print("    " + "P" + str(process[i]) + "\t |\t" + str(arrival[i]) + "\t |\t" + str(burst[i]))

  #timeline
  timeline = []
  for i in range(0,len(display)):
    if display[i] == 'idle':
      timeline.append('|-idle-|')
    else:
      timeline.append('|--'+ display[i] +'--|')
      
  if len(timeElapsed) == 1:
    input("\nPress ENTER to show TIMELINE...\n")
  else:
    print("\nPress ENTER to show TIMELINE...\n")
  print("TIMELINE\n")
  if len(displayTime) == 1:
    time.sleep(0.50)

  print("\t".join(str(displayTime[i]) for i in range(0, len(displayTime))))
  print(" "+"".join(str(timeline[i]) for i in range(0, len(timeline))))
  cls()
  
#computation of TAT and WT
completeTime.append(burstSum)
timeElapsed.append(burstSum+idleTime)
for i in range(0, processNum):
  tat.append(abs(completeTime[i]-arrival[done[i]-1]))
  wt.append(abs(tat[i]-burst[done[i]-1]))

#summary
header()
print("PROCESS LIST")
print("________________________________________")
print(" Process | Arrival Time  | Burst Time")
for i in range(0, processNum):
  print("    " + "P" + str(process[i]) + "\t |\t" + str(arrival[i]) + "\t |\t" + str(burst[i]))
    
print("\nPress ENTER to show TIMELINE...\n")
print("TIMELINE\n")

print("\t".join(str(timeElapsed[i]) for i in range(0, len(timeElapsed))))
print(" "+"".join(str(timeline[i]) for i in range(0, len(timeline))))

print("\n======================================================================")
print("CONCLUSION")
averageTAT = sum(tat)/processNum
averageWT = sum(wt)/processNum
print(" > Average Turnaround Time: " + str(round(averageTAT,2)))
print(" > Average Waiting Time: " + str(round(averageWT,2)))