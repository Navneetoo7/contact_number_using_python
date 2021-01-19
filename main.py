lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    lst.append(ele)

for i in range(len(lst)):
    print("BEGIN:VCARD", "\nVERSION:3.0", "\nN:;doctor", str(i), ";;;", "\nFN:doctor", str(i), "\nTEL;TYPE=CELL:+91",
          lst[i], "\nEND:VCARD")
