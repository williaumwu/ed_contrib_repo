def run(stackargs):

    import json

    # instantiate stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="show_version")
    stack.parse.add_required(key="hostname")

    # Add shelloutconfigs
    stack.add_shelloutconfig('williaumwu:::demo-repo::hello_world_script',"script")
    stack.add_shelloutconfig('williaumwu:::demo-repo::hello_world_script:2',"script2")

    # Add hostgroups
    stack.add_hostgroups("williaumwu:::demo-repo::hello_world_group_delegation:1", "hello_world_hostgroup_1")
    stack.add_hostgroups("williaumwu:::demo-repo::hello_world_group_delegation:2", "hello_world_hostgroup_2")

    # init the stack namespace
    stack.init_variables()
    stack.init_hostgroups()
    stack.init_shelloutconfigs()

    # add run environmental variables
    _env_vars = {"SHOW_VERSION":stack.show_version}
    _env_vars["ENV"] = "demo"
    _env_vars["EXECUTION_LAYER"] = "delegation"
    stack.add_host_env_vars_to_run(_env_vars)

    # print out variables on saas dashboard/run
    stack.publish(_env_vars)

    # demo orchestration shellout execution
    # version 1 of script
    orchestr_env_vars = {"SHOW_VERSION":int(stack.show_version) + 1 }
    orchestr_env_vars["ENV"] = "demo"
    orchestr_env_vars["EXECUTION_LAYER"] = "orchestration"
    inputargs = {"display":True}
    inputargs["human_description"] = 'Demos Show Version +1 in the orchestration'
    inputargs["env_vars"] = json.dumps(orchestr_env_vars)
    stack.script.run(**inputargs)

    # version 2 of script
    orchestr_env_vars = {"SHOW_VERSION":int(stack.show_version) + 2 }
    orchestr_env_vars["ENV"] = "demo"
    inputargs = {"display":True}
    inputargs["human_description"] = 'Demos Show Version +2 in the orchestration'
    inputargs["env_vars"] = json.dumps(orchestr_env_vars)
    stack.script2.run(**inputargs)

    # execute orders on host
    # version 1 of hostgroup
    stack.add_groups_to_host(groups=stack.hello_world_hostgroup_1,hostname=stack.hostname)

    # version 2 of hostgroup
    stack.add_groups_to_host(groups=stack.hello_world_hostgroup_2,hostname=stack.hostname)

    return stack.get_results()
