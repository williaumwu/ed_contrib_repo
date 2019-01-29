def run(instructargs):

    stack = newStack(instructargs)

    # Add default variables
    stack.parse.add_required(key="run_id")
    stack.parse.add_required(key="data")
    stack.parse.add_required(key="job_name")
    stack.parse.add_required(key="sched_name")
    stack.parse.add_required(key="mkey",default="default")

    # Initialize Variables in stack
    stack.init_variables()

    inputargs = {}
    inputargs["run_id"] = stack.run_id
    inputargs["data"] = stack.data
    inputargs["mkey"] = stack.mkey
    inputargs["job_name"] = stack.job_name
    inputargs["sched_name"] = stack.sched_name
  
    stack.run_metadata.add(**inputargs)

    return stack.get_results()

def example():

    '''
    '''


















