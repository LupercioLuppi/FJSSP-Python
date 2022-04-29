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
from operator import itemgetter

# Classes for the FJSSP
from job import Job

# Dataset must follow the standard format
# First Line - Jobs x Machines x Max Operations
# Each line represents a Job with particular machine possibilities and tuples for each machine, time
# First digit number of operations for each job (n >=1)
# Next digits number of machines that can process each operation (task) followed by pairs of [machine, time]
# Ex...
# 4	5	5
#  3  5 1 2 2 5 3 4 4 1 5 2 5 1 5 2 4 3 5 4 7 5 5 5 1 4 2 5 3 5 4 4 5 5
#  3  5 1 2 2 5 3 4 4 7 5 8 5 1 5 2 6 3 9 4 8 5 5 5 1 4 2 5 3 4 4 54 5 5
#  4  5 1 9 2 8 3 6 4 7 5 9 5 1 6 2 1 3 2 4 5 5 4 5 1 2 2 5 3 4 4 2 5 4 5 1 4 2 5 3 2 4 1 5 5
#  2  5 1 1 2 5 3 2 4 4 5 12 5 1 5 2 1 3 2 4 1 5 2
# This dataset has 4 Jobs and 5 Machines (with max/average of 5 machines per operation - this is optional)
# First Job (J1) has 3 operations
# First operation for J1 can be processed by 5 machines [1,2][2,5][3,4][4,1][5,2]
# Second Operation can also be processed by 5 machines [1,5][2,4][3,5][4,7][5,5]... and so on
# Job 2 has 3 operations and follows the same logic
# Job 3 has 4 operations and follows the same logic
# Job 4 has 2 operations and follows the same logic

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
            job.add_operation_tuples(sequence_for_operation)
            i += 1 + 2 * number_operations

        # all operations possible for the job are done... store the job to a list
        jobs_list.append(job)

        # set next job to be processed
        currentJob += 1


print('           Possible Machine, Units of Time to execute each task (operation) of each Job')
for j in jobs_list:
    print(j)

    # Uncomment to display Min/Max for each operation
    #operations = j.operation_tuples()
    #for o in operations:
    #    min_dur = min(o, key=itemgetter(1))[1]
    #    max_dur = max(o, key=itemgetter(1))[1]
    #
    #    print("Min / Max duration for Operation : ", min_dur , " / ", max_dur)
"""
print("Total Jobs ", len(jobs_list))
print("Range ", range(len(jobs_list)))
"""
