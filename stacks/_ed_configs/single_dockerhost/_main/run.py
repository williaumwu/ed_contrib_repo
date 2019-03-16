def run(instructargs):

    stack = newStack(instructargs)

    # Add required variables
    stack.parse.add_required(key="os_version",default="16.04")
    stack.parse.add_required(key="hostname",default="{}-{}".format(instructargs["cluster"],"docker_host"))
    stack.parse.add_required(key="key",default="first_ssh_key")
    stack.parse.add_required(key="sg_label",default="web")
    stack.parse.add_required(key="sg",default="sg_web")
    stack.parse.add_required(key="ELASTICDEV_ACCESS_GROUP")

    # Add substacks
    stack.add_substack("ed:::ed_test::ec2_ubuntu_server")
    stack.add_substack("ed:::ed_test::init_dockerhost_dns")
    stack.add_substack("ed:::ed_test::init_dockerhost_ed_host")

    # init the stack namespace
    stack.init_variables()
    stack.init_substacks()

    # access group should be local and private
    stack.set_variable("access_group","local:::private::{}".format(stack.ELASTICDEV_ACCESS_GROUP))

    # Create Docker Host
    optional_keys = ["queue_name",
                     "vpc",
                     "user",
                     "timeout",
                     "security_group",
                     "region"]

    default_values = {}
    default_values["size"] = "t2.medium"
    default_values["disksize"] = 100
    default_values["hostname"] = stack.hostname
    default_values["key"] = stack.key
    default_values["image_ref"] = "github_13456777:::public::ubuntu.{}-docker".format(stack.os_version)
    default_values["ip_key"] = "private_ip"
    default_values["tags"] = "docker_host docker container single_host {} {} {}".format(stack.hostname,stack.os_version,"dev")
    default_values["sg"] = stack.sg
    default_values["sg_label"] = stack.sg_label

    human_description = "Initiates a Docker Server on Ec2"
    
    inputargs = {"default_values":default_values,
                 "optional_keys":optional_keys}
    
    inputargs["automation_phase"] = "initialize_infrastructure"
    inputargs["human_description"] = human_description
    inputargs["display"] = True
    inputargs["display_hash"] = stack.get_hash_object(inputargs)

    stack.ec2_ubuntu_server.insert(**inputargs)

    # Create the a single host without a deploy
    required_keys = [ "soa" ]
    inputargs = {"default_values":default_values,
                 "required_keys":required_keys,
                 "optional_keys":optional_keys}

    inputargs["automation_phase"] = "initialize_infrastructure"
    inputargs["human_description"] = "Singlehost finalization of DockerHost: {}".format(stack.hostname)
    inputargs["display"] = True
    inputargs["display_hash"] = stack.get_hash_object(inputargs)
    stack.init_dockerhost_dns.insert(**inputargs)

    # Wait for hosts to finish all of its orders
    stack.wait_hosts_tag(tags=stack.hostname)

    # Pass the infrastructure variables
    stack.add_stack_args_to_run({"docker_host":stack.hostname},mkey="infrastructure")
    stack.publish({"docker_host":stack.hostname})

    # Finalize configuration of Docker host

    default_values = {}
    default_values["hostname"] = stack.hostname
    default_values["access_group"] = stack.access_group

    inputargs = {"default_values":default_values}
    inputargs["automation_phase"] = "initialize_infrastructure"
    inputargs["human_description"] = 'Add base docker_guest on "{}"'.format(stack.hostname)
    inputargs["display"] = True
    inputargs["display_hash"] = stack.get_hash_object(inputargs)
    stack.init_dockerhost_ed_host.insert(**inputargs)

    # Return results
    return stack.get_results(instructargs.get("destroy_instance"))


















































































