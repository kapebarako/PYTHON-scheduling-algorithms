import os
import time
clear = lambda:os.system('clear')
jobList = []
failed = []
ctr = 0

def header():
  print("PL-ACT6: Single-User Contiguous Scheme")
  print("Programmed by: Alcazar, Faye Therese Simone L.\n")
  
header()
mem = int(input("Input Memory Capacity: "))
opSys = int(input("Input OS Size: "))
cap = mem - opSys

print("\nEnter memory capacity of each job in KB")
i = 1
while i <= 10:
  job = input("Input Job (" + str(i) + "/10):")
  if '.' in job:
    jobList.append(float(job))
  else:
    jobList.append(int(job))
  i += 1
  
print("\nJOB LIST")
time.sleep(0.50)
for j in range(len(jobList)):
  print("Job "+ str(j+1) + ": " + str(jobList[j]) + " KB")
print("Press any key to continue...")
input()
clear()

for k in range(len(jobList)):
  alloc = 1
  dealloc = 0
  header()
  print("Allocating Job "+ str(k+1) + "...")
  time.sleep(1)
  if jobList[k] < cap:
    print("Job " + str(k+1) + " Memory allocated successfully.")
    print("OS(" + str(opSys) + "K) Job "+ str(k+1) + "(" + str(jobList[k]) + "K) Unused space(" + str(cap-jobList[k])  + "K)\n")
    ctr += 1
    alloc += 1
  else:
    print("Job " + str(k+1) + " failed to load. Insufficient memory space for allocation.\n")
    failed.append("Job"+ str(k+1))
    dealloc += 1
  if k == 9:
    print("No more jobs waiting. Press any key to continue...")
    input()
    clear()
    header()
    print("\nSUMMARY")
    print("Total Jobs allocated in the memory: " + str(ctr))
    print("Failed Jobs: ")
    if ctr == 10:
      print("None.")
    else:
      print(', '.join(str(failed) for failed in failed))
  else:
    while (alloc != 0):
      print("Job " + str(k+1))
      print("Allocate or Deallocate?")
      num = int(input("Allocate(1)  Deallocate(2): "))
      if num == 1:
        if dealloc == 0:
          print("Allocation failed. Partition is not empty.\n")
        elif dealloc == 1:
          alloc -= 1
      elif num == 2:
        if alloc == 1:
          print("Deallocation failed. Partition is not handling a job.\n")
        elif alloc == 2:
          print("Job " + str(k+1) + " Memory deallocated successfully.\n")
          alloc -= 1
          dealloc += 1
      else:
        print("Input not recognized. Please input again.\n")
    time.sleep(0.07)
    clear()
  


