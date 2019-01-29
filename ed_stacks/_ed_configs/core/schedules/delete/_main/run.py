def run(instructargs):

    stack = newStack(instructargs)

    # Add default variables
    stack.parse.add_required(key="parallel_instances",default="_None",null_allowed=True)
    stack.parse.add_required(key="sequential_instances",default="_None",null_allowed=True)
    stack.parse.add_required(key="sched_refs",default=[])
    stack.parse.add_required(key="_schedule_id")
    stack.parse.add_required(key="destroy_instance",default=True,null_allowed=True)

    # init variables
    stack.init_variables()

    # Delete parallel instances
    if stack.parallel_instances:
        for iteration,instance_info in enumerate(stack.parallel_instances):
            stack.delete_instance(cluster=instance_info[0],instance=instance_info[1])
            if iteration == 0: stack.set_parallel()

    # Delete sequential instances
    #####################################
    stack.unset_parallel()
    #####################################

    input_args = { "queue_host":"instance","max_wt":"self"}
    stack.wait_all_instance(**input_args)

    if stack.sequential_instances:
        for instance_info in stack.sequential_instances:
            stack.delete_instance(cluster=instance_info[0],instance=instance_info[1])

    input_args = { "queue_host":"instance","max_wt":"self"}
    stack.wait_all_instance(**input_args)

    #####################################
    stack.set_parallel()
    #####################################

    for sched_ref in stack.sched_refs:
        default_values = {}
        default_values["match"] = sched_ref

        stack.insert_builtin_cmd('schedule reference delete',
                                 order_type="delete_sched_ref::api",
                                 role="schedule/delete",
                                 default_values=default_values)

    # Delete sequential instances
    #####################################
    stack.unset_parallel()
    #####################################

    input_args = { "queue_host":"instance","max_wt":"self"}
    stack.wait_all_instance(**input_args)

    default_values = {}
    default_values["schedule_id"] = stack._schedule_id
    default_values["background"] = False
    default_values["ref_only"] = True

    stack.insert_builtin_cmd('schedule delete',
                             order_type="delete_sched::api",
                             role="schedule/delete",
                             default_values=default_values)
    
    stack.delete_cluster(cluster=instance_info[0])

    return stack.get_results(stack.destroy_instance)









