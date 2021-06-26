def run(stackargs):

    # instantiate stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="show_version")
    stack.parse.add_required(key="hostname")

    # Add shelloutconfigs
    stack.add_shelloutconfig('williaumwu:::demo-repo::hello_world_script')

    # Add hostgroups
    stack.add_hostgroups("williaumwu:::demo-repo::hello_world_group", "latest_hostgroup")

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

    # execute orders on host
    stack.add_groups_to_host(groups=stack.latest_hostgroup,hostname=stack.hostname)

    return stack.get_results()
