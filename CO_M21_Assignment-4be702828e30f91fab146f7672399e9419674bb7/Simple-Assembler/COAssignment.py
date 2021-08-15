# CO project(semester 2) to design a custom assembler 
#group members: Aditya, Rishav,Samuel
import sys
assemblyfile=sys.stdin.read().splitlines()
#with open("read.txt") as r:
 #   assemblyfile=r.read().splitlines()


REG_ADD={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
Instruction={"add":["00000","A"],"sub":["00001","A"],"mov":["00010","B"],"mov1":["00011","C"],"ld":["00100","D"],"st":["00101","D"],"mul":["00110","A"],"div":["00111","C"],"rs":["01000","B"],"ls":["01001","B"],"xor":["01010","A"],"or":["01011","A"],"and":["01100","A"],"not":["01101","C"],"cmp":["01110","C"],"jmp":["01111","E"],"jlt":["10000","E"],"jgt":["10001","E"],"je":["10010","E"],"hlt":["10011","F"],}

Address=[]
variable=[]
Var={}


def Bin(x):
    b=bin(x)[2:]
    a=(8-len(b))*"0"+str(b)
    return a



flag = 0
add_count=0
#counting instructions other than var.
for line in assemblyfile:
    if(len(line)==0):continue
    x=list(line.split())
    variable.append(x[0])
    if x[0]=="var":
        continue    
    else:
        Address.append(add_count)
        add_count+=1
y=add_count

# variable count
for line in assemblyfile:
    if(len(line)==0):continue
    y=list(line.split())
    if y[0]=="var":
        Var[y[1]]=add_count+1
        add_count+=1

# error of var not used at beginning
for i in range(0,len(variable)-1):
    if(len(line)==0):continue
    if variable[i]!="var":
        if variable[i+1]=="var":
            print("Variables not declared at beginning.")

Label_add={}
c=0
for line in assemblyfile:   # will store add of labels
    c+=1
    if(len(line)==0):continue
    y=list(line.split())

    if y[0][-1]==":":
        Label_add[y[0]]=c



if add_count>256:
    print("Lines in code exceed 256 limit.")

else:    
    #code to print errors if any
    for line in assemblyfile:
        
        if(len(line)==0):continue
        x=list(line.split())
        #print(x[0])
        if len(x)>1 and x[0] in Label_add and x[1] in Instruction:
            x.pop(0)
       

        if x[0]=="var":
            continue    
        else:
            Address.append(add_count)
            add_count+=1
            
            if x[0]==":":
                print(end='')
            else:
                if x[0]=="add" or x[0]=="sub" or x[0]=="mul" or x[0]=="xor" or x[0]=="or" or x[0]=="and":                
                        
                        if(x[1] not in REG_ADD.keys() or x[2] not in REG_ADD.keys() or x[3] not in REG_ADD.keys()):
                            flag=1
                            print("Typos in register name.")
                

                if x[0]=="mov" or x[0]=="rs" or x[0]=="ls":
                    if (x[1] in REG_ADD.keys()):
                        if(x[2][0]=="$"):
                            z=int(x[2][1:])
                            if(z<0 or z>255):
                                flag=1
                                print("Illegal immediate values.")
                        
                        else:
                            flag=1
                            print("General Syntax error.")
                    else:
                        flag=1
                        print("Typos in register name.")
                



                if x[0]=="mov1" or x[0]=="div" or x[0]=="cmp" or x[0]=="not":
                    
                    if(x[1] not in REG_ADD.keys() and x[2] not in REG_ADD.keys()):
                        flag=1
                        print("Typos in register name.")                
                


                if x[0]=="ld" or x[0]=="st":
                    
                    if(x[1] not in REG_ADD.keys()):
                        flag=1
                        print("Typos in register name.")

                    if(x[2] not in Var.keys()):
                        flag=1
                        print("Use of undefined variables.")
                
                if x[0]=="hlt" and c!=len(assemblyfile):
                    print("hlt must be at the end")

                if x[0]=="jmp" or x[0]=="jlt" or x[0]=="jgt" or x[0]=="je":
                    
                    if((x[1] +":") not in Label_add.keys()):
                        flag=1
                        print("Use of undefined labels.")
                else:           
                    if (x[0] not in Instruction.keys()):
                        print("Typos in instruction name.")

                
    #hlt not used error
    if("hlt" not in assemblyfile):
        flag=1
        print("Missing hlt instruction") 
    
                
    
    #code to print machine code if no error
    for line in assemblyfile:
        x=list(line.split())
        if flag ==1:
            break
        if flag==0:
            if len(x)>1 and x[0] in Label_add and x[1] in Instruction:
                x.pop(0)

            if x[0]=="var":
                continue    
            else:
                Address.append(add_count)
                add_count+=1
                
                if x[0]==":":
                    print(end='')
                else:
                    if x[0]=="add" or x[0]=="sub" or x[0]=="mul" or x[0]=="xor" or x[0]=="or" or x[0]=="and":
                        if((x[1] and x[2] and x[3]) in REG_ADD.keys()):
                            print (Instruction[x[0]][0]+"00"+REG_ADD.get(x[1])+REG_ADD.get(x[2])+REG_ADD.get(x[3]))
                        
                    if x[0]=="mov" or x[0]=="rs" or x[0]=="ls":
                        if (x[1] in REG_ADD.keys()):
                            if(x[2][0]=="$"):
                                z=int(x[2][1:])
                                if(0<=z<=255):
                                    print(Instruction[x[0]][0]+REG_ADD.get(x[1])+Bin(z))

                            

                    if x[0]=="mov1" or x[0]=="div" or x[0]=="cmp" or x[0]=="not":
                        if(x[1] and x[2] in REG_ADD.keys()):
                            print (Instruction[x[0]][0]+"00000"+REG_ADD.get(x[1])+REG_ADD.get(x[2]))
                        
                    
                    if x[0]=="ld" or x[0]=="st":
                        if(x[1] in REG_ADD.keys() and x[2] in Var.keys()):
                            z=Var.get(x[2])
                            print(Instruction[x[0]][0]+REG_ADD.get(x[1])+Bin(z))
                    
                    
                    if x[0]=="jmp" or x[0]=="jlt" or x[0]=="jgt" or x[0]=="je":
                            print(Instruction[x[0]][0]+"000"+Bin(Label_add[x[1]+":"]) )
                        
                    
                    if  x[0]=="hlt":
                        print(Instruction[x[0]][0]+"00000000000")
                



    

    

     


    