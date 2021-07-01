def run(stackargs):

    import json

    # instantiate stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="show_version")
    stack.parse.add_required(key="hostname")

    # Add shelloutconfigs
    stack.add_shelloutconfig('williaumwu:::demo-repo::hello_world_script',"script")
    stack.add_shelloutconfig('williaumwu:::demo-repo::hello_world_script:2',"script")

    # Add hostgroups
    stack.add_hostgroups("williaumwu:::demo-repo::hello_world_group_delegation", "hello_world_hostgroup")

    # init the stack namespace
    stack.init_variables()
    stack.init_hostgroups()
    stack.init_shelloutconfigs()

    # add run environmental variables
    _env_vars = {"SHOW_VERSION":stack.show_version}
    _env_vars["ENV"] = "demo"
    stack.add_host_env_vars_to_run(_env_vars)

    # print out variables on saas dashboard/run
    stack.publish(_env_vars)

    # demo orchestration shellout execution
    orchestr_env_vars = {"SHOW_VERSION":int(stack.show_version) + 1 }
    orchestr_env_vars["ENV"] = "demo"
    inputargs = {"display":True}
    inputargs["human_description"] = 'Demos Show Version +1 in the orchestration'
    inputargs["env_vars"] = json.dumps(orchestr_env_vars)
    stack.script.run(**inputargs)

    orchestr_env_vars = {"SHOW_VERSION":int(stack.show_version) + 2 }
    orchestr_env_vars["ENV"] = "demo"
    inputargs = {"display":True}
    inputargs["human_description"] = 'Demos Show Version +2 in the orchestration'
    inputargs["env_vars"] = json.dumps(orchestr_env_vars)
    stack.script.run(**inputargs)

    # execute orders on host
    stack.add_groups_to_host(groups=stack.hello_world_hostgroup,hostname=stack.hostname)

    return stack.get_results()
