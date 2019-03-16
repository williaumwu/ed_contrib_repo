def default():

    task = {}
    env_vars = []
    shelloutconfigs = []

    shelloutconfigs.append('installation/ubuntu/install-docker-compose')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, \
                       'shelloutconfigs': shelloutconfigs \
                       }

    return task














































