def default():
    
    return action()


def action():

    task = {}
    env_vars = []
    shelloutconfigs = []

    shelloutconfigs.append('installation/ubuntu/16.04/install-docker')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, \
                       'shelloutconfigs': shelloutconfigs \
                       }

    return task

