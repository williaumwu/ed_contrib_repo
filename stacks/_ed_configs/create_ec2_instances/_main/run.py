def run(stackargs):

    import json

    # instantiate authoring stack
    stack = newStack(stackargs)

    stack.parse.add_required(key="security_group_ids")
    stack.parse.add_required(key="subnet_id")
    stack.parse.add_required(key="key_name")
    stack.parse.add_required(key="server_name_base",default="ed-tf-ansible-eg")
    stack.parse.add_required(key="instance_type",default="t3.micro")
    stack.parse.add_required(key="server_count",default="2")
    stack.parse.add_required(key="root_size",default="20")

    stack.parse.add_optional(key="docker_exec_env",default="elasticdev/terraform-run-env")
    stack.parse.add_optional(key="aws_default_region",default="eu-west-1")
    stack.parse.add_optional(key="stateful_id",default="_random")

    # Add execgroup
    stack.add_execgroup("williaumwu:::terraform-ansible-example::ec2_instances")

    # Initialize 
    stack.init_variables()
    stack.init_execgroups()

    # Execute execgroup
    env_vars = {"TF_VAR_aws_default_region":stack.aws_default_region}
    env_vars["AWS_DEFAULT_REGION"] = stack.aws_default_region
    env_vars["TF_VAR_security_group_ids"] = stack.security_group_ids
    env_vars["TF_VAR_subnet_id"] = stack.subnet_id
    env_vars["TF_VAR_key_name"] = stack.key_name
    env_vars["TF_VAR_server_name_base"] = stack.server_name_base
    env_vars["TF_VAR_instance_type"] = stack.instance_type
    env_vars["TF_VAR_server_count"] = stack.server_count
    env_vars["TF_VAR_root_size"] = stack.root_size
    env_vars["STATEFUL_ID"] = stack.stateful_id

    #env_vars["resource_type".upper()] = stack.resource_type
    #env_vars["RESOURCE_TAGS"] = "{},{},{}".format(stack.resource_type, stack.rds_name, stack.aws_default_region)

    env_vars["docker_exec_env".upper()] = stack.docker_exec_env
    env_vars["METHOD"] = "create"
    env_vars["CLOBBER"] = True
    env_vars["use_docker".upper()] = True

    docker_env_fields_keys = env_vars.keys()
    docker_env_fields_keys.append("AWS_ACCESS_KEY_ID")
    docker_env_fields_keys.append("AWS_SECRET_ACCESS_KEY")
    docker_env_fields_keys.remove("METHOD")

    env_vars["DOCKER_ENV_FIELDS"] = ",".join(docker_env_fields_keys)

    inputargs = {"display":True}
    inputargs["env_vars"] = json.dumps(env_vars)
    inputargs["name"] = stack.rds_name
    inputargs["stateful_id"] = stack.stateful_id
    inputargs["human_description"] = "Creating RDS {}".format(stack.rds_name)
    stack.ec2_instances.insert(**inputargs)

    return stack.get_results()

