def default():
    
    task = {}
    env_vars = []
    shelloutconfigs = []
    shelloutconfigs.append('ed:::ed_test::run_threelayer/pre_scripts')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars,
                        'shelloutconfigs': shelloutconfigs
                        }

    return task
