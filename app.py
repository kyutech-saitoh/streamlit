
import sys
import streamlit as st

import psutil
import platform
import GPUtil

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

mem = psutil.virtual_memory()

st.title("Hello World !")

# CPU
uname = platform.uname()
st.write("System information")
st.write(uname.system)

# メモリ
svmem = psutil.virtual_memory()
st.write("RAM information")
st.write(get_size(svmem.total))

#import subprocess
#import json

# GPU
gpus = GPUtil.getGPUs()
list_gpus = []
for gpu in gpus:
    # get the GPU id
    gpu_id = gpu.id
    # name of GPU
    gpu_name = "name: " + gpu.name
    # get % percentage of GPU usage of that GPU
    gpu_load = "load: %.2f %%" % (gpu.load * 100)
    # get free memory in MB format
    gpu_free_memory = "free memory: %.1f MB" % gpu.memoryFree
    # get used memory
    gpu_used_memory = "used memory: %.1f MB" % gpu.memoryUsed
    # get total memory
    gpu_total_memory = "total memory: %.1f MB" % gpu.memoryTotal
    # get GPU temperature in Celsius
    gpu_temperature = "temperature: %.1f °C" % gpu.temperature
#    gpu_uuid = gpu.uuid
    list_gpus.append((
        gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
        gpu_total_memory, gpu_temperature
    ))

st.write("GPU information")
st.write(list_gpus)
