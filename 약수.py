inputnum = input()
inputnum = int(inputnum)

inputvar = input()

inputarr = inputvar.split(" ")
for i in range(inputnum):
    inputarr[i] = int(inputarr[i])

inputarr.sort()

print(inputarr[0] * inputarr[inputnum-1])  
