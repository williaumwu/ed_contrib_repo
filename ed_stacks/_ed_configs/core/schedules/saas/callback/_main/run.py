def run(instructargs):

    stack = newStack(instructargs)

    # Add default variables
    stack.parse.add_required(key="run_id")
    stack.parse.add_required(key="schedule_id")
    stack.parse.add_required(key="callback_api_endpoint")
    stack.parse.add_required(key="callback_token")
    stack.parse.add_required(key="sched_token")

    stack.parse.add_required(key="edata",default="_None")
    stack.parse.add_required(key="cluster_id",default="_None")
    stack.parse.add_required(key="epassphrase",default="_None")
    stack.parse.add_required(key="project_id",default="_None")
    stack.parse.add_required(key="sched_destroy",default="_None")
    stack.parse.add_required(key="status",default="unknown")

    # Init the variables
    stack.init_variables()

    ##############################################
    values = {}
    values["schedule_id"] = stack.schedule_id
    values["run_id"] = stack.run_id
    values["cluster"] = stack.cluster
    values["instance"] = stack.instance
    values["status"] = stack.status
    values["sched_token"] = stack.sched_token
    if stack.epassphrase: values["epassphrase"] = stack.epassphrase
    if stack.edata: values["edata"] = stack.edata
    if stack.cluster_id: values["cluster_id"] = stack.cluster_id

    # If the callback is confirm the destroying of a project/schedule ids
    if stack.sched_destroy and stack.project_id: values["sched_destroy"] = stack.project_id

    default_values = {}
    default_values["http_method"] = "post"
    default_values["api_endpoint"] = stack.callback_api_endpoint
    default_values["callback"] = stack.callback_token
    default_values["values"] = "{}".format(str(stack.dict2str(values)))

    human_description = "Reporting of schedule_id={}, run_id={} callback to SaaS".format(stack.schedule_id,stack.run_id)
    long_description = "Reporting of schedule_id={}, run_id={} callback to SaaS with other information; specifically, the env_vars".format(stack.schedule_id,stack.run_id)

    stack.insert_builtin_cmd("execute restapi",
                             order_type="saas-report_sched::api",
                             default_values=default_values,
                             human_description=human_description,
                             long_description=long_description,
                             display=True,
                             role="ed/api/execute")

    #####################################
    return stack.get_results()
    #####################################

def example():

    '''

    '''


















