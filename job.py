class Job:
    def __init__(self, job_id):
        self.__job_id = job_id
        self.__job_operations = 1
        self.__job_num_machines = 1
        self.__job_op_times = []
        self.__job_op_sequence = []
        self.__job_op_done = []

    # Add Operation and time sequence for the Job
    def add_operation_tuple(self, machine_time):
        self.__job_op_times.append(machine_time)

    # Display Job and Operation times
    def __str__(self):
        job_times = "Job [" + str(self.__job_id) + "] = "

        # Display possible op times in single line - for small setups
        for op_time in self.__job_op_times:
            job_times += str(op_time) + " "

        return job_times

    def operation_tuples(self):
        return self.__job_op_times