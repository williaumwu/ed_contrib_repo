def run(stackargs):

    # instantiate authoring stack
    stack = newStack(stackargs)

    stack.parse.add_required(key="security_group_ids")
    stack.parse.add_required(key="subnet_id")
    stack.parse.add_required(key="key_name")
    stack.parse.add_required(key="server_name_base",default="ed-tf-ansible-eg")
    stack.parse.add_required(key="instance_type",default="t3.micro")
    stack.parse.add_required(key="server_count",default="2")
    stack.parse.add_required(key="root_size",default="20")

    stack.parse.add_optional(key="docker_terraform_exec_env",default="elasticdev/terraform-run-env")
    stack.parse.add_optional(key="docker_ansible_exec_env",default="elasticdev/ansible-run-env")
    stack.parse.add_optional(key="aws_default_region",default="eu-west-1")

    # add substacks
    stack.add_substack('williaumwu:::create_ec2_instances')
    stack.add_substack('williaumwu:::install_nginx_to_servers')

    # Initialize 
    stack.init_variables()
    stack.init_substacks()

    # create ec2 instances
    default_values = {"security_group_ids":stack.security_group_ids}
    default_values["subnet_id"] = stack.subnet_id
    default_values["key_name"] = stack.key_name
    default_values["server_name_base"] = stack.server_name_base
    default_values["instance_type"] = stack.instance_type
    default_values["server_count"] = stack.server_count
    default_values["root_size"] = stack.root_size
    default_values["aws_default_region"] = stack.aws_default_region
    # note, the key for substack is "docker_exec_env" rather than "docker_terraform_exec_env"
    default_values["docker_exec_env"] = stack.docker_terraform_exec_env

    # install nginx to ec2 instances
    default_values = {"server_name_base":stack.server_name_base}
    default_values["server_count"] = stack.server_count

    inputargs = {"default_values":default_values}
    inputargs["automation_phase"] = "infrastructure"
    inputargs["human_description"] = 'Install Nginx on ec2 {}, num {}'.format(stack.server_name_base,stack.server_count)
    stack.install_nginx_to_servers.insert(display=True,**inputargs)

    return stack.get_results()
