def run(instructargs):

    stack = newStack(instructargs)

    # Add required variables
    stack.parse.add_required(key="hostname")
    stack.parse.add_required(key="soa")

    # Add hostgroups
    stack.add_hostgroups('gary:::public::Ubuntu/Docker/Hourly/Cleanup local:::private::Accounts/SSH_Access','groups')

    # init the stack namespace
    stack.init_variables()
    stack.init_hostgroups()

    resource_info = stack.get_resource(name=stack.hostname,
                                       resource_type="server",must_exists=True)[0]

    # Add dockhost to run to deploy key
    values = {"docker_host":stack.hostname}
    stack.add_stack_args_to_run(values,mkey="deploy")

    # Add dockhost to run
    values["public_ip"] = public_ip = resource_info["public_ip"]
    values["private_ip"] = resource_info["private_ip"]
    if resource_info.get("public_dns_name"): values["public_dns_name"] = resource_info["public_dns_name"]
    stack.publish(values)

    # Set the endpoint 
    endpoint = resource_info.get("endpoint","www")

    # Assign groups
    stack.assoc_groups_to_host(stack.groups,hostname=stack.hostname)

    # Add DNS endpoints
    pargs = "dns add record"
    order_type = "dns_domain::api"
    role = "dns/modify"
    
    default_values = {}
    default_values["soa"] = stack.soa
    default_values["type"] = "A"
    default_values["target"] = public_ip
    default_values["name"] = endpoint

    human_description='Add DNS A record endpoint "{}.{}" target "{}"'.format(endpoint,stack.soa,public_ip)

    # Add dns record with builtin
    stack.insert_builtin_cmd(pargs,
                             order_type=order_type,
                             default_values=default_values,
                             human_description=human_description,
                             role=role)

    return stack.get_results(instructargs.get("destroy_instance"))

def example():

    print '''
    '''


















