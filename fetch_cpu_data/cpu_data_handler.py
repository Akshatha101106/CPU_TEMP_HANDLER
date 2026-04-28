import os
import pandas as pd

prev_idle = 0
prev_total = 0
""""
fetch the cpu usage data from proc file which will 
include all the neccesary data with respect to comnsumed 
OS data
"""
def read_cpu_usage()->int:
    
    global prev_idle,  prev_total
   
    with open("/proc/stat" , "r") as f:
        data = [int(i) for i in f.readline().split()[1:]]
        
    idle = data[3]
    total = sum(data)
    
    idle_delta = idle - prev_idle
    total_delta = total - prev_total
    
    prev_idle =idle
    prev_total = total
    
    if total_delta == 0:
        return 0
    
    cpu_usage =  ( 1 - idle_delta/total_delta)*100
    
    return round(cpu_usage , 2)
    
    

def read_temp():
    file_path = "/mnt/c/read_temp/temperature.CSV"
    
    df = pd.read_csv(file_path , encoding= 'latin1')
    #convert column to numeric string becomes None
    temp_value = pd.to_numeric(df["Core Temperatures (avg) [°C]"] , errors = "coerce" )
    #return the last row value where numeric value is found
    return temp_value.dropna().iloc[-1]
    
    
def read_mem_info():
    memory = {} #empty dictnary to store the mem values
    with open("/proc/meminfo","r") as f:
        for i in f:
            key ,value = i.split(":")
            memory[key] = int(value.strip().split()[0])
        
        available = memory["MemAvailable"]
        total = memory["MemTotal"]
        
        if total == 0:
            return 0.0
            
        
        used = total - available

    return round((used/total)*100 , 2)            
        


def read_load_avg():
    with open("/proc/loadavg" , "r") as f:
        load = float(f.read().split()[0])
    core_count = os.cpu_count()
    
    load_avg = float((load/core_count)*100)
    
    return round(load_avg ,2)
    
    
    




