def default():

    task = {}
    env_vars = []
    shelloutconfigs = []

    env_vars.append("docker/build")
    env_vars.append("docker/application/flask")
    shelloutconfigs.append('installation/ubuntu/16.04/install-docker')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, 
                        'shelloutconfigs': shelloutconfigs 
                        }
    return task
