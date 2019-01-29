def default():
    
    task = {}
    env_vars = []
    shelloutconfigs = []

    env_vars.append("ed:::ed_test::docker/build")
    shelloutconfigs.append('ed:::ed_test::docker/run_dockerfile')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, 
                        'shelloutconfigs': shelloutconfigs 
                        }

    return task
