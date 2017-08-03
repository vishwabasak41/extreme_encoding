def encrypt(character,key,i,dict):
        j=i%key
        dict[j].append(character)
        return dict
input_string=raw_input("Enter you choice of string")
dict={}
i=0
x=0
key=int(raw_input("Enter your key for encrypting"))
while i<key:
    dict[i]=[]                  # print dict
    i=i+1
for character in input_string:
    final_output=encrypt(character,key,x,dict)
    x=x+1
y=0
output_string=[]
while y < key:
    output_string=output_string+final_output[y]
    y=y+1
string_of_lists = ""
for a in output_string:
    string_of_lists += str(a)
print "HI!Your encrypted string is",string_of_lists
