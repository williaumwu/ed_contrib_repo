def run(stackargs):

    import json

    # instantiate stack
    stack = newStack(stackargs)

    # Add variables
    stack.parse.add_optional(key="build_dir",default="_random")

    # Add shelloutconfigs
    #stack.add_shelloutconfig('williaumwu:::demo-repo::show_model')

    # Add hostgroups
    stack.add_execgroup("williaumwu:::demo-repo::gunmetal_wheels", "wheels")
    stack.add_execgroup("williaumwu:::demo-repo::ferrari_core", "core")

    # init the stack namespace
    stack.init_variables()
    stack.init_execgroups()
    stack.init_shelloutconfigs()

    stack.set_variable("chrootfiles_dest_dir","/var/tmp/share/{}".format(stack.build_dir))

    env_vars = {"CHROORFILES_DEST_DIR":stack.chrootfiles_dest_dir}
    env_vars["F1_DIR"] = stack.chrootfiles_dest_dir

    inputargs = {"display":True}
    inputargs["env_vars"] = json.dumps(env_vars)
    inputargs["human_description"] = "Creating platform with wheels {}".format(stack.wheels.asset)
    stack.wheels.insert(**inputargs)

    inputargs = {"display":True}
    inputargs["env_vars"] = json.dumps(env_vars)
    inputargs["human_description"] = "Creating platform with core {}".format(stack.core.asset)
    stack.core.insert(**inputargs)

    return stack.get_results()
