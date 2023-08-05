import numpy as np
import os

def main():
    cur_pwd = os.getcwd()
    dataMat = []
    index = []
    address = []
    IC = []
    cnt = 0
    IC_cnt = 0

    for line in open(cur_pwd + "/memaccess/dram.out"):
        curLine=line.strip().split(" ")
        dataMat.append(curLine)
        cnt += 1

    for i in range(cnt): 
        IC_cnt += 1
        if dataMat[i][0] != "0:":
            if dataMat[i][1] == 'global:' and dataMat[i][3] =='from':
                if dataMat[i][2] == 'Read':
                    IC.append(IC_cnt)
                    index.append('0')
                    add = dataMat[i][10]
                    address.append(add[2:])
                    
                    IC_cnt = 0
                elif dataMat[i][2] == 'Write':
                    IC.append(IC_cnt)
                    index.append('1') 
                    add = dataMat[i][10]
                    address.append(add[2:])

                    IC_cnt = 0
#    print(index)
#    print(address)
#    print(IC)

    trace = open(cur_pwd + "/memaccess/memaccess.trace", "w")
    for i in range (len(index)):
        trace.write("# " + index[i] + ' ' + address[i] + ' ' + str(IC[i]) + '\n')

    trace.close()

if __name__ == '__main__':
    main()
