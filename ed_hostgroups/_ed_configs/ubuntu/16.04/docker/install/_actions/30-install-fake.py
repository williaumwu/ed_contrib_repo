def default():

    task = {}
    env_vars = []
    shelloutconfigs = []

    shelloutconfigs.append('cluster_vars/create_kube_configmap')

    task['method'] = 'shelloutconfig'
    task['metadata'] = {'env_vars': env_vars, \
                       'shelloutconfigs': shelloutconfigs \
                       }

    return task
