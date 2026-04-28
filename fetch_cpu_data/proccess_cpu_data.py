from cpu_data_handler import ( read_cpu_usage ,
                              read_mem_info,
                              read_load_avg,
                              read_temp)

import csv
from openpyxl import Workbook
from datetime import datetime
import time


def fetch_all_cpu_data():
    
    file_path = "/home/akshatha/Project/CPU_TEMP_HANDLER/cpu_data.xlsx"
    
    wb = Workbook()
    ws = wb.active
    ws.title = "CPU Data"

    # Header row
    ws.append([
        "current_time",
        "cpu_usage_data",
        "memory_info",
        "temperature",
        "average_load"
        ])
        
    while True:
           current_time = datetime.now().strftime("%H:%M:%S")
           cpu_usage_data = read_cpu_usage()
           memory_info =read_mem_info()
           temperature = read_temp()
           average_load = read_load_avg()
           
           #log data immediatly
           ws.append([
            current_time,
            cpu_usage_data,
            memory_info,
            temperature,
            average_load
        ])
           
           #save data asap
           wb.save(file_path)
        
           #after every one second update the data to excel sheet
           time.sleep(1)
    print("excel created successfully")
    
    
fetch_all_cpu_data()         
           
        
        
        
        
    