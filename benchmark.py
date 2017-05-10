#!/usr/bin/python3
import datetime
import os
import subprocess

########### SETTINGS ###########
# Path to script for testing
script_path = "python3 test.py"
# How many executions for multiple_test
exec_times = 1000
# How many seconds for limit_test
limit = 1000
# Where to put results
result_path = "result.txt"
################################


def get_processor_name():
    command = "lscpu | grep name | cut -d: -f2"
    return subprocess.check_output(command, shell=True).strip()

def get_memory_info():
    command = "vmstat -s | grep 'total memory' | awk -F' ' '{print $1}'"
    return subprocess.check_output(command, shell=True).strip()

def run_test(script_path):
    start_time = datetime.datetime.now()
    os.system(script_path)
    finish_time = datetime.datetime.now()
    return (finish_time - start_time)


def multiple_test(n, script_path):
    print("{}\tStarting {} repeating {} times".format(datetime.datetime.now(), script_path, n))
    total = 0
    for i in range(n):
        total += run_test("python3 test.py").total_seconds()
    average = total / n
    print("{}\tMultiexec test finished".format(datetime.datetime.now()))
    return total, average

def limit_test(s, script_path):
    print("{}\tStarting {} for {} seconds".format(datetime.datetime.now(), script_path, s))
    total = 0
    i = 1
    while True:
        total += run_test("python3 test.py").total_seconds()
        if total > s:
            break
        i += 1
    average = total / i
    print("{}\tLimit test finished".format(datetime.datetime.now()))
    return i, average


cpu_name = get_processor_name().decode()
total_memory = get_memory_info().decode()
total_time, m_average_time = multiple_test(exec_times, script_path)
exec_times, l_average_time = limit_test(limit, script_path)

if not os.path.exists(result_path):
    with open(result_path, "w") as result_file:
        result_file.write("timestamp,script path,cpu name,total memory (KB),multiexec total time,multiexec average time,limit test executions,limit test average time\n")

with open(result_path, "a") as result_file:
    result_file.write("{},{},{},{},{},{},{},{}\n".format(datetime.datetime.now(), script_path, cpu_name, total_memory, total_time, m_average_time, exec_times, l_average_time))