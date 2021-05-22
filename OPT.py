import os
import time
clear = lambda:os.system('clear')
frames = []
pages = []
requested = []
alloc = []
done = []
waiting = []
turns = []
future = []
check=[]

#functions
def header():
  print("FL-ACT3: Replacement Algorithm - OPT")
  print("Programmmed by: Alcazar, Faye Therese Simone L.")
  print("==========================================================\n")

def cls():
  input("\nPress ENTER to continue...")
  clear()
  
def allocate():
  for i in range(0, frameNum):
    if page in done:
      continue
    elif alloc[i] == 'FREE' and page in waiting:
      alloc[i] = requested[page]
      break
    elif alloc[i] == 'FREE':
      alloc[i] = requested[page]
      break
    else:
      waiting.append(page)
    
#input
header()
print("FRAMES")
ok = 1
while ok != 0:
  frameNum = input(" > Input number of frames: ")
  if frameNum.isnumeric() and str(frameNum) != '0':
    frameNum = int(frameNum)
    ok = 0
  else:
    print("Error! Invalid input. Please input again.\n")

print("\nPAGES")
ok = 1
print("Input desired type of pages (0 or A/a only) \n  0 - numbers\n  A - letters")
while ok != 0:
  pageType = input(" > Desired Type: ")
  if pageType == '0':
    ok = 0
  elif pageType == 'A' or pageType == 'a':
    ok = 0
  else:
    print("Error! Invalid input. Please input again.\n")    
ok = 1
while ok != 0:
  pageNum = input(" > Input number of pages: ")
  if pageNum.isnumeric() and str(pageNum) != '0':
    pageNum = int(pageNum)
    ok = 0
  else:
    print("Error! Invalid input. Please input again.\n")
#page set-up
if pageType == '0':
  for i in range(0, pageNum):
    pages.append(i)
if pageType == 'A' or pageType == 'a':
  for i in range(0, pageNum):
    pages.append(chr(65 + i))
print("\nList of Available Pages:\n " + str(pages))

cls()
header()
print("REQUESTED PAGES")
ok = 1
while ok != 0:
  requestNum = input(" > Input number of Requested Pages: ")
  if requestNum.isnumeric() and str(requestNum) != '0':
    requestNum = int(requestNum)
    ok = 0
  else:
    print("Error! Invalid input. Please input again.\n")
print("\nAvailable Pages:\n " + str(pages) + "\n")

if pageType == 'A' or pageType == 'a':
  print("** Not case-sensitive. Inputs will be converted to uppercase.\n")
  
i = 0
while i < requestNum:
  ok = 1
  while ok != 0:
    req = input(" > Input Requested Page(" + str(i+1) + "/" + str(requestNum) + "): ")
    if str(req).upper() in str(pages) and str(req).isalnum():
      requested.append(req.upper())
      ok = 0
    else:
      print("Error! Page does not exist. Please input again.\n")
  i += 1

#requested pages display
cls()
header()
print("REQUESTED PAGES LIST\n")
time.sleep(0.50)
for i in range(0, requestNum):
  print("Page Request#" + str(i+1) + ": " + str(requested[i]))
cls()

#alloc/dealloc
for i in range(0, frameNum):
  alloc.append('FREE')
  turns.append(0)
  future.append('-')
#allocation
hit = 0
fault = 0
page = 0
header()
print("OUTPUT")
print("__________________________________________________________")
print(" Request|   " + "   ".join("Frame " + str(i + 1) for i in range(0, frameNum)) + "   Page Fault")
time.sleep(0.50)
while page != requestNum:
  if str(requested[page]) not in str(alloc) and 'FREE' in alloc:
    allocate()
    print("    " + str(requested[page]) + "\t|      " +  " \t".join(str(alloc[i]) for i in range(0, frameNum)) + "\t    *")
    fault += 1
    
  elif str(requested[page]) not in str(alloc) and 'FREE' not in alloc:
    for l in range(page, requestNum):
      check.append(requested[l])
    
    for k in range(0, frameNum):   
      for j in range(0,len(check)):
        if str(alloc[k]) == str(check[j]):
          future[k] = check.index(check[j])
          break
    del check[:]
    
    if future.count('-') == frameNum: #apply lru
      deallocIndex = turns.index(max(turns))
      turns[deallocIndex] = 0
      alloc[deallocIndex] = 'FREE'
      
    else:#apply opt
      deallocIndex = future.index(max(future))
      alloc[deallocIndex] = 'FREE'
    allocate()
    
    print("    " + str(requested[page]) + "\t|      " +  " \t".join(str(alloc[i]) for i in range(0, frameNum)) + "\t    *")
    for i in range(0, frameNum):
      future[i] = '-'
    fault += 1
  
  else:
    print("    " + str(requested[page]) + "\t|      " +  " \t".join(str(alloc[i]) for i in range(0, frameNum)) + "\t    -")
    hit += 1
  
  for i in range(0,frameNum):
    if alloc[i] is not 'FREE' and requested[page] == alloc[i]:
      turns[i] = 1
    elif alloc[i] is not 'FREE':
      turns[i] = turns[i]+1
      
  page += 1
  time.sleep(0.50)
  
#summary
print("__________________________________________________________")
print("\nCONCLUSION")
print(" > There are " + str(hit) + " page hits and " + str(fault) + " page faults.")


