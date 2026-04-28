from cpu_data_handler import ( read_cpu_usage ,
                              read_mem_info,
                              read_load_avg,
                              read_temp)

import csv
from datetime import datetime
import time


def fetch_all_cpu_data():
    
    file_path = "/home/akshatha/Project/CPU_TEMP_HANDLER/cpu_data.csv"
    
    with open("file_path","w" , newline = "") as f:
        writer = csv.writer(f)
        writer.writerow(["current_time","cpu_usage_data" , 
                         "memory_info" , "temprature" , "average_load"])
        
        while True:
           current_time = datetime.now().strftime("%H:%M:%S")
           cpu_usage_data = read_cpu_usage()
           memory_info =read_mem_info()
           temprature = read_temp()
           average_load = read_load_avg()
           
           #log data immediatly
           writer.writerow([current_time,cpu_usage_data , memory_info , 
                            temprature ,average_load])
           
           #save data asap
           f.flush()
        
           time.sleep(3)
    print("CSV created successfully")
    
    
fetch_all_cpu_data()         
           
        
        
        
        
    