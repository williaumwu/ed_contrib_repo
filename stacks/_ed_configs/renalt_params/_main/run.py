def run(stackargs):

    import json

    # instantiate stack
    stack = newStack(stackargs)

    # Add default variables
    stack.parse.add_required(key="hostname")
    stack.parse.add_required(key="wheel_color",default="green")

    # Add shelloutconfigs
    stack.add_shelloutconfig('williaumwu:::demo-repo::show_model')

    # Add hostgroups
    stack.add_hostgroups("williaumwu:::demo-repo::wheel_green", "wheel_green")
    stack.add_hostgroups("williaumwu:::demo-repo::wheel_blue:1", "wheel_blue")
    stack.add_hostgroups("williaumwu:::demo-repo::chassis")
    stack.add_hostgroups("williaumwu:::demo-repo::dashboard")
    stack.add_hostgroups("williaumwu:::demo-repo::engine")

    # init the stack namespace
    stack.init_variables()
    stack.init_hostgroups()
    stack.init_shelloutconfigs()

    orchestr_env_vars = {"race_team":int(stack.team) + 1 }
    orchestr_env_vars["ENV"] = "demo"
    orchestr_env_vars["EXECUTION_LAYER"] = "orchestration"
    inputargs = {"display":True}
    inputargs["human_description"] = 'Demos Show Version +1 in the orchestration'
    inputargs["env_vars"] = json.dumps(orchestr_env_vars)
    stack.script.run(**inputargs)

    # version 2 of script
    # print out variables on saas dashboard/run
    _publish_vars = {"wheel_color":stack.wheel_color}
    _publish_vars["chassis"] = stack.chassis
    _publish_vars["dashboard"] = stack.dashboard
    _publish_vars["engine"] = stack.engine
    stack.publish(_publish_vars)

    if stack.wheel_color == "green":
        _wheel = stack.wheel_green
    else:
        _wheel = stack.wheel_blue

    stack.logger.debug("Wheel color is {}".format(_wheel))

    _groups = stack.chassis+" "+_wheel+" "+stack.engine+" "+stack.dashboard

    # version 1 of hostgroup
    stack.add_groups_to_host(groups=_groups,hostname=stack.hostname)

    return stack.get_results()
