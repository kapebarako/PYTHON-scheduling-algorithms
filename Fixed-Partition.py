import os
import time
clear = lambda:os.system('clear')
partSize = []
jobList = [] 
alloc = [] 
tempList = []
done = []
waiting = []
failed = []

#functions
def header():
  print("PL-ACT7: Fixed Partition - FIRST FIT")
  print("Programmmed by: Alcazar, Faye Therese Simone L.\n")

def cls():
  input("\nPress any key to continue...")
  clear()

def result():
  time.sleep(0.50)
  print(" Memory\t\t\t  Alloc\\DeAlloc")
  print(" OS Partition (" + str(opSys) + "M)\t  OS")
  for i in range(0, numPar):
    if alloc[i] != "FREE":
      print(" Partition " + str(i+1) + "(" + str(partSize[i]) + "M)" + "\t  Job " + str(alloc[i]+1) + "(" +str(tempList[i]) + "M)")
    else:
      print(" Partition " + str(i+1) + "(" + str(partSize[i]) + "M)" + "\t  " + alloc[i])

#input      
header()
mem = float(input("Input Memory Capacity: "))
ok = 1
while ok != 0:
  opSys = float(input("Input OS Size: "))
  if opSys < mem:
    if '.0' in str(opSys):
      opSys = int(opSys)
    ok -= 1
  else:
    print("Error! Input cannot exceed capacity. Please input again.")
numPar = int(input("Number of Partitions: "))

cap = mem - opSys
if '.0' in str(cap):
  cap = int(cap)
rem = cap
print("\nEnter size of each Partition in M unit")
i = 0
while i < numPar-1:
  ok = 1
  while ok != 0:
    print("Remaining Capacity: " + str(rem) + "M")
    par = input("Size of Partition " + str(i+1) + ": ")
    if float(par) > (rem):
      print("Error! Input cannot exceed capacity. Please input again.")
    else:
      if '.' in par:
        partSize.append(float(par))
      else:
        partSize.append(int(par))
      ok -= 1
    rem = cap-sum(partSize)
    print(" ")
  i += 1
print("Remaining Capacity: 0M")
print("Size of Partition " + str(numPar) + ": " + str(rem) + "M")
if '.' in str(rem):
  partSize.append(float(rem))
else:
  partSize.append(int(rem))
print("\nRemaining Capacity has been assigned to the last parition.")
largestPart = max(partSize)
cls()

header()
print("Enter memory capacity of each job in M unit")
i = 1
while i <= 10:
  job = input("Input Job (" + str(i) + "/10): ")
  if '.' in str(job):
    jobList.append(float(job))
  else:
    jobList.append(int(job))
  i += 1
cls()

#job list
header()
print("JOB LIST")
time.sleep(0.50)
for i in range(len(jobList)):
  print("Job "+ str(i+1) + ": " + str(jobList[i]) + "M")
for i in range(0, numPar):
  alloc.append("FREE")
  tempList.append(int(0))
cls()

#alloc/dealloc
ctr = 1
ok = 1
while ok != 0:
  header()
  for i in range(0, numPar): 
    for j in range(0, 10):
      if j in done:
        continue
      elif j in waiting and alloc[i] == "FREE" and jobList[j] <= partSize[i]:
        alloc[i] = j
        tempList[i] = jobList[j]
        done.append(j)
      elif jobList[j] <= partSize[i] and alloc[i] == "FREE":
        alloc[i] = j
        tempList[i] = jobList[j]
        done.append(j)
      elif jobList[j] > largestPart:
        if j not in failed:
          failed.append(j)
      else:
        waiting.append(j)
        
  print("SET " + str(ctr))
  result()
  
  input("\nPress any key to deallocate...")
  print("\nDEALLOCATION")
  
  for i in range(0,2):
    min1 = largestPart
    for j in range(0, numPar):
      if min1 >= tempList[j] and alloc[j] != "FREE":
        min1 = tempList[j]
        minIndex = j
    alloc[minIndex] = "FREE"
    
  result()
  cls()
  ctr += 1
  
  if len(done) + len(failed) == len(jobList):
    for i in range(0, numPar):
      if alloc[i] in range(0,10):
        ok = 1
        break
      else:
        ok = 0

#summary
header()
print("CONCLUSION")
print("\nThere are " + str(ctr-1) + " sets of memory allocation.")
if len(failed) == 0:
  print("All jobs were successfully executed.")
else:
  print(str(len(failed)) + " jobs were not executed: " + ", ".join("Job " + str(failed[i] + 1) for i in range(0, len(failed))) + ".")
