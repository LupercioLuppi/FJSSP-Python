# FJSSP Datasets Reader to Dictionaries
# Lupercio F Luppi 2022

import re                           # Regular Expressions - to read dataset and parse
from operator import itemgetter

# Classes for the FJSSP
from job import Job

# Kacem 4 Jobs x 5 Machines
file = 'datasets/Kacem1_4x5.fjs'

# Kacem 15 Jobs x 10 Machines
#file = 'datasets/Kacem4.fjs'

# A list of Jobs
jobs_list = []

with open(file) as data:
    total_jobs, total_machines, max_operations = re.findall('\S+', data.readline())
    number_total_jobs, number_total_machines, number_max_operations = int(total_jobs), int(total_machines), int(float(
        max_operations))

    # Set Job Id to 1 to initiate dataset load
    currentJob = 1

    for key, line in enumerate(data):

        # Check if there are extra lines at the end of the dataset and stop the loop
        if key >= number_total_jobs:
            break
        parsed_line = re.findall('\S+', line)

        # For each Job a dict of operations
        job_operations = {}

        i = 1   # pointer to current item of parsed line

        currentOperation=1
        # while there are operations to retrieve for the current job in the parsed line extract tuples (machine, time)
        while i < len(parsed_line):
            number_operations = int(parsed_line[i])

            # a list to store pairs machine, time for each operation
            operation_tuples = []
            for id_operation in range(1, number_operations + 1):
                # operation tuple (machine, time)
                operation_tuple = int(parsed_line[i + 2 * id_operation - 1]), int(parsed_line[i + 2 * id_operation])
                # fill operation vector with machine,time
                operation_tuples.append(operation_tuple)

            # add operation and tuple sequence [(machine, exec_time)...] to dictionary
            job_operations[currentOperation] = operation_tuples
            currentOperation += 1

            # advance pointer to the next set of op sequences from dataset
            i += 1 + 2 * number_operations

        # add dictionary of operations for Job
        jobs_list.append(job_operations)

        # set next job to be processed
        currentJob += 1


print("List of ", len(jobs_list), " JOBs created")

for j in range(len(jobs_list)):
    print("JOB [", j+1, "] has ", len(jobs_list[j]), " operations")
    for key in jobs_list[j]:
        print(key, ' -> ', jobs_list[j][key])
