""""
fetch the cpu usage data from proc file which will 
include all the neccesary data with respect to comnsumed 
OS data
"""
def read_cpu_usage()->list:
    data = []
    with open("/proc/stat" , "r") as f:
        data = [int(i) for i in f.readline().split()[1:]]
    return data 

def test():
   a = 0
   print(read_cpu_usage())
   
test()




