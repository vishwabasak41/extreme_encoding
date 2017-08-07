#function to add values to integers.
def create_array(s,arr_list=[]):
    i=0
    arr_list
    print "Enter value for array between 0- 30000 for %d"%(s)
    for i in range(s):
        inp=int(raw_input("value:?"))
        arr_list.append(inp)
# function from the code
def encodeInteger(x,n):
	n = n<<(1<<(1<<(1<<1)));
	x = x | n;
	return x;
def encodeArray(n,A,B,N=[]):
    for i in range(n):
    	N.append(encodeInteger(A[i], B[i]));
    return N

def decodeInteger(arr,n):
    a=[]
    b=[]
    for i in range(n):
        val_a=arr[i]%65536
        val_b=arr[i]/65536
        a.append(val_a)
        b.append(val_b)
    return a,b
    #code
size=int(raw_input("Enter the size of the array"))
A=[]
B=[]
ARR=[]
create_array(size,A)
create_array(size,B)
ARR=encodeArray(size,A,B)
print ARR
A=decodeInteger(ARR,size)
print A
