# FJSSP Solver using Google ortools library
# Lupercio F Luppi 2022
# Reference from samy-barrech FJSSP GitHub @
# https://github.com/samy-barrech/Flexible-Job-Shop-Scheduling-Problem/
# and Colab from ortools @
# https://colab.research.google.com/github/google/or-tools/blob/master/examples/notebook/examples/flexible_job_shop_sat.ipynb#scrollTo=ZUzZC3_t5jPK

#import collections
#from ortools.sat.python import cp_model
#import numpy as np

import re                           # Regular Expressions - to read dataset and parse
from operator import itemgetter     # i

# Classes for the FJSSP
from job import Job

# Dataset must follow the standard format (Jobs x Machines x Max Operations) and each line represents a Job
# with particular machine possibilities and tuples for each machine, time

# Kacem 4 Jobs x 5 Machines
file = 'datasets/Kacem1_4x5.fjs'

# Kacem 15 Jobs x 10 Machines
#file = 'datasets/Kacem4.fjs'

with open(file) as data:

    total_jobs, total_machines, max_operations = re.findall('\S+', data.readline())
    number_total_jobs, number_total_machines, number_max_operations = int(total_jobs), int(total_machines), int(float(
        max_operations))

    # An array of Jobs just for the fun of it
    jobs_list = []
    machine_list = []

    # Set Job Id to 1 to initiate dataset load
    currentJob = 1

    for key, line in enumerate(data):

        # Check if there are extra lines at the end of the dataset and stop the loop
        if key >= number_total_jobs:
            break

        parsed_line = re.findall('\S+', line)

        i = 1   # pointer to current item of parsed line

        # instantiate a job object to store dataset info
        job = Job(currentJob)

        # while there are operations to retrieve for the current job in the parsed line extract tuple (machine, time)
        while i < len(parsed_line):
            number_operations = int(parsed_line[i])
            sequence_for_operation = []
            for id_operation in range(1, number_operations + 1):
                # operation tuple (machine, time)
                operation_tuple = int(parsed_line[i + 2 * id_operation - 1]), int(parsed_line[i + 2 * id_operation])
                # fill operation vector with machine,time
                sequence_for_operation.append(operation_tuple)

            # add operation tuple sequence [(machine, exec_time)...] to the job
            job.add_operation_tuple(sequence_for_operation)
            i += 1 + 2 * number_operations

        # all operations possible for the job are done... store the job to a list
        jobs_list.append(job)

        # set next job to be processed
        currentJob += 1


print('           Possible Machine, Units of Time to execute each task (operation) of each Job')
for j in jobs_list:
    print(j)
    operations = j.operation_tuples()
    for o in operations:
        min_dur = min(o, key=itemgetter(1))[1]
        max_dur = max(o, key=itemgetter(1))[1]

        print("Min / Max duration for Operation : ", min_dur , " / ", max_dur)
"""
print("Total Jobs ", len(jobs_list))
print("Range ", range(len(jobs_list)))
"""
