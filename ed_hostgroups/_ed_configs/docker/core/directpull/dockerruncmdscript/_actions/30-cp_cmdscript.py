def default():
    
    task = {}
    env_vars = []
    shelloutconfigs = []

    env_vars.append("ed:::ed_test::docker/build")
    shelloutconfigs.append('ed:::ed_test::docker/runs/copy_cmd_script')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, 
                        'shelloutconfigs': shelloutconfigs 
                        }

    return task



