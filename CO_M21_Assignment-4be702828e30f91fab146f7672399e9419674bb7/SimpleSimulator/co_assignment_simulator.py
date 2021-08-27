# CO project(semester 2) to design a custom simulator
#group members: Aditya, Rishav,Samuel


# <PC (8 bits)><space><R0 (16 bits)><space>...<R6 (16 bits)><space><FLAGS (16 bits)> #


import sys
machinefile=sys.stdin.read().splitlines()

# with open("test1.txt") as r:
    # machinefile = r.read().splitlines()
    # print(machinefile)


REG_ADD={"000":["R0",0], "001":["R1",0], "010":["R2",0], "011":["R3",0], "100":["R4",0], "101":["R5",0], "110":["R6",0]}
Flags_reg={"111":["FLAGS",0]}

Instruction={"00000":"add" , "00001":"sub" , "00010":"mov", "00011":"mov1" , "00100":"ld" ,
 "00101":"st" , "00110":"mul" , "00111":"div" , "01000":"rs" , "01001":"ls" , "01010":"xor" , 
 "01011":"or" , "01100":"and" , "01101":"not" , "01110":"cmp" , "01111":"jmp" ,  "10000":"jlt" , 
 "10001":"jgt" , "10010":"je" , "10011":"hlt" }


#program counter
PC=0

#counting lines in of the code
count=0

mem_addr=dict()
count1=0


#decimal to binary coversion
def Bin8(x):
    b=bin(x)[2:]
    a=(8-len(b))*"0"+str(b)
    return a
def Bin16(x):
    b=bin(x)[2:]
    a=(16-len(b))*"0"+str(b)
    return a

#binary to decimal conversion
def dec(n):
    a=int(n,2)
    return a

# to store memory address of each line
for line in machinefile:
    mem_addr[count]=0
    count+=1
# to store mem_addr of variables
for line in machinefile:
    if(line[0:5]=="00100" or line[0:5]=="00101" or line[0:5]=="01111" or line[0:5]=="10000" or line[0:5]=="10001"
     or line[0:5]=="10010"):
        y= dec(line[8:])
        mem_addr[count]=y
        count+=1

# lists used in plotting graph
memory=[]
cycle=[]
c_count=0

############# simulator code ##################
for line in machinefile:
    
    memory.append(PC)
    cycle.append(c_count)
    c_count+=1
    # Type A
    #addition instruction
    if (line[0:5]=="00000"):
        
        REG_ADD.get(line[7:10])[1] = REG_ADD.get(line[10:13])[1] + REG_ADD.get(line[13:])[1]
        
        #Flag SET condition
        if (REG_ADD.get(line[7:10])[1]>((2**16)-1)):
            binary=bin(REG_ADD.get(line[7:10])[1])
            #removing first two bits '0b'
            binary=binary[2:]
            result=binary[len(binary)-16:]
            result1=int(result,2)
            REG_ADD.get(line[7:10])[1]=result1
            Flags_reg.get("111")[1]+=8
        

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))

        
        PC+=1
        
    #subtraction instruction
    if (line[0:5]=="00001"):

        REG_ADD.get(line[7:10])[1] = REG_ADD.get(line[10:13])[1] - REG_ADD.get(line[13:])[1]
        
        #Flag SET condition
        if(REG_ADD.get(line[7:10])[1]<0):
            REG_ADD.get(line[7:10])[1]=0    
            Flags_reg.get("111")[1]+=8

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))

        
        PC += 1

    #mult instruction
    if (line[0:5]=="00110"):

        REG_ADD.get(line[7:10])[1] = REG_ADD.get(line[10:13])[1] * REG_ADD.get(line[13:])[1]
        
        #Flag SET condition
        if (REG_ADD.get(line[7:10])[1]>((2**16)-1)):
            binary=bin(REG_ADD.get(line[7:10])[1])
            #removing first two bits '0b'
            binary=binary[2:]
            result=binary[len(binary)-16:]
            result1=int(result,2)
            REG_ADD.get(line[7:10])[1]=result1
            Flags_reg.get("111")[1]+=8

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1    

    # Bitwise XOR
    if (line[0:5]=="01010"):

        REG_ADD.get(line[7:10])[1] = REG_ADD.get(line[10:13])[1] ^ REG_ADD.get(line[13:])[1]
        

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
        Flags_reg.get("111")[1]=0
        
    # Bitwise OR
    if (line[0:5]=="01011"):

        REG_ADD.get(line[7:10])[1] = REG_ADD.get(line[10:13])[1] | REG_ADD.get(line[13:])[1]
        

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1           
        Flags_reg.get("111")[1]=0

    # Bitwise AND
    if (line[0:5]=="01100"):

        REG_ADD.get(line[7:10])[1] = REG_ADD.get(line[10:13])[1] & REG_ADD.get(line[13:])[1]
        

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
        Flags_reg.get("111")[1]=0


    # Type B inst
    # Move Imm
    if (line[0:5]=="00010"):
        
        REG_ADD.get(line[5:8])[1] = dec(line[8:])
        

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
        Flags_reg.get("111")[1]=0

    # Right Shift
    if (line[0:5]=="01000"):
        imm = dec(line[8:])
        reg = REG_ADD.get(line[5:8])[1]
        temp = ( reg >> imm )
        
        REG_ADD.get(line[5:8])[1] = temp

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
        Flags_reg.get("111")[1]=0
    
    # Left Shift 
    if (line[0:5]=="01001"):

        imm = dec(line[8:])
        reg = REG_ADD.get(line[5:8])[1]
        temp = ( reg << imm )
        
        REG_ADD.get(line[5:8])[1] = temp

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
        Flags_reg.get("111")[1]=0

    
    # Type C
    # move reg
    if (line[0:5]=="00011"):
        
        if(line[13:] in REG_ADD.keys()):
            REG_ADD.get(line[10:13])[1] = REG_ADD.get(line[13:])[1]
        
        if(line[13:] in Flags_reg.keys()):    
            REG_ADD.get(line[10:13])[1] = Flags_reg.get(line[13:])[1]
        
        Flags_reg.get("111")[1]=0

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            
        
        PC+=1
  

    # Divide
    if (line[0:5]=="00111"):

        # REG_ADD.get("000")
        # print(REG_ADD.get("000")[1])
        # q -> qoutient r -> remainder 
        q, r = divmod(REG_ADD.get(line[10:13])[1], REG_ADD.get(line[13:])[1])

        REG_ADD.get("000")[1] = q
        REG_ADD.get("001")[1] = r

        

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
        Flags_reg.get("111")[1]=0

    # Bitwise NOT
    if (line[0:5]=="01101"):

        REG_ADD.get(line[10:13])[1] = ~REG_ADD.get(line[13:])[1]
        

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
        Flags_reg.get("111")[1]=0

    # compare
    if (line[0:5]=="01110"):

        # less than
        if (REG_ADD.get(line[10:13])[1] < REG_ADD.get(line[13:])[1] ):
            
            
            Flags_reg.get("111")[1]=4
        
        
    
        # greater than
        if ( REG_ADD.get(line[10:13])[1] > REG_ADD.get(line[13:])[1] ):

            Flags_reg.get("111")[1]=2

        # equal to
        if ( REG_ADD.get(line[10:13])[1] == REG_ADD.get(line[13:])[1] ):

            Flags_reg.get("111")[1]=1


        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
    
  # Type D opcode(5) reg1(3) mem_Address(8)
    # Load
    if (line[0:5]=="00100"):
       

        REG_ADD.get(line[5:8])[1] = mem_addr.get(dec(line[8:]))
        memory.append(mem_addr.get(dec(line[8:])))
        cycle.append(c_count-1)
        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+
        Bin16(REG_ADD.get("010")[1])+" "+Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+
        Bin16(REG_ADD.get("101")[1])+" "+Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]) )            

        
        PC+=1
        Flags_reg.get("111")[1]=0

    # Store
    if (line[0:5]=="00101"):
        
        
        mem_addr[dec(line[8:])]=REG_ADD.get(line[5:8])[1]
        #print(Bin8(PC))
        memory.append(mem_addr.get(dec(line[8:])))
        cycle.append(c_count-1)
        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        
        PC+=1
        Flags_reg.get("111")[1]=0

    #Type E
    #jump
    if(line[0:5]=="01111"):
        Flags_reg.get("111")[1]=0
        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        PC=mem_addr[dec(line[8:])]
        

    # jump if less than
    if(line[0:5]=="10000"):
        y = Flags_reg.get("111")[1]
        Flags_reg.get("111")[1]=0
        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        if(y==4):
            PC=PC=mem_addr[dec(line[8:])]
        else:
            PC+=1
        
        
    
    #jump if greater than
    if(line[0:5]=="10001"):
        y = Flags_reg.get("111")[1]
        Flags_reg.get("111")[1]=0
        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        if(y==2):
            PC=PC=mem_addr[dec(line[8:])]
        else:
            PC+=1

       

    # jump if equal
    if(line[0:5]=="10010"):
        y = Flags_reg.get("111")[1]
        Flags_reg.get("111")[1]=0
        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))            

        if(y==1):
            PC=PC=mem_addr[dec(line[8:])]
        else:
            PC+=1
       
    
    # Type F 
    # halt
    if (line[0:5]=="10011"):

        print(Bin8(PC)+" "+Bin16(REG_ADD.get("000")[1])+" "+Bin16(REG_ADD.get("001")[1])+" "+Bin16(REG_ADD.get("010")[1])+" "
        +Bin16(REG_ADD.get("011")[1])+" "+Bin16(REG_ADD.get("100")[1])+" "+Bin16(REG_ADD.get("101")[1])+" "
        +Bin16(REG_ADD.get("110")[1])+" "+Bin16(Flags_reg.get("111")[1]))          

        break



#print the input code after the output of it.
for line in machinefile:
    print(line)


#store memory address of each line
for line in machinefile:
    mem_addr[count1]=0
    count1+=1
# to store mem_addr of variables
for line in machinefile:
    if(line[0:5]=="00100" or line[0:5]=="00101" or line[0:5]=="01111" or line[0:5]=="10000" or line[0:5]=="10001"
     or line[0:5]=="10010"):
        x=mem_addr[dec(line[8:])]
        
        # printing the variables after the code ends
        print(Bin16(x))
        count1+=1

# printing 16 '0's to complete 256 lines of the code
for i in range(256-count1):
    print("0"*16)







#********************************************************************************
# Plotting the graph for the simulator
import numpy as np
import matplotlib.pyplot as plt

plt.scatter(np.array(cycle),np.array(memory),marker="+")
plt.ylabel("MEMORY")
plt.xlabel("CYCLE")
plt.show()                        

