def run(instructargs):

    vpc_label = instructargs.get("vpc_label","vpc")
    vpc_peer = instructargs.get("vpc_peer","jiffy")
    sg_web_label = instructargs.get("sg_web_label","web")
    sg_bastion_label = instructargs.get("sg_bastion_label","bastion")
    sg_db_label = instructargs.get("sg_db_label","database")
    #####################################
    instructions = InstructionHelper(instructargs)
    #####################################
    vpc = "{}-{}".format(instructions.cluster,vpc_label)
    sg_web = "{}-{}".format(instructions.cluster,sg_web_label)
    sg_bastion = "{}-{}".format(instructions.cluster,sg_bastion_label)
    sg_db = "{}-{}".format(instructions.cluster,sg_db_label)
    instructions.unset_parallel()
    #####################################
    pargs = "ec2 vpc create"
    order_type = "create-cloudvpc::api"
    role = "cloud/network"

    default_values = {}
    default_values["region"] = "us-east-1"
    human_description = "Creates VPC {}".format(vpc)

    instructions.add_jiffy_cli(pargs=pargs,
                               order_type=order_type,
                               default_values=default_values,
                               human_description=human_description,
                               display=True,
                               role=role)
    ##############################################
    labels = {}
    labels[sg_db_label] = {"subnet_type":"public"}
    labels["bastion"] = {"subnet_type":"public"}
    labels["web"] = {"subnet_type":"public"}
    ##############################################
    snets = []

    for lkey,lvalue in labels.iteritems():

        snets.append("%s:%s" % (lkey,lvalue["subnet_type"]))

    subnets = " ".join(snets)

    pargs = "ec2 subnet batchadd"
    order_type = "create-cloudsubnet::api"
    role = "cloud/network"

    human_description = "Creates subnets for vpc"
    long_description = "Creates subnets in batches on ec2 for vpc"

    input_args = { "subnets":subnets,
                   "add_cluster_name":True,
                   "add_instance_name":True }

    instructions.add_jiffy_cli(pargs=pargs,
                               order_type=order_type,
                               role=role,
                               required_keys=[ "subnets" ],
                               human_description=human_description,
                               long_description=long_description,
                               display=True,
                               jkwargs=input_args)
    ##############################################
    instructions.set_parallel()
    #####################################
    if vpc_peer:
        pargs = "ec2 vpc peering"
        order_type = "peer-cloudvpc::api"
        role = "cloud/network"

        default_values = {"bidirectional":True}
        default_values["src_vpc"] = vpc_peer
        if vpc_label: default_values["dst_label"] = vpc_label
        human_description = "Creates VPC peering"

        instructions.add_jiffy_cli(pargs=pargs,
                                   order_type=order_type,
                                   role=role,
                                   human_description=human_description,
                                   display=True,
                                   default_values=default_values)
    ##############################################
    required_keys=[ "sg_label", "rules" ]

    base_args = { "add_cluster_name":True,
                  "add_instance_name":True }

    pargs = "ec2 security group create"
    order_type = "create-cloudsg::api"
    role = "cloud/network"
    #____________________________________________
    input_args = base_args.copy()
    input_args["sg_label"] = sg_db_label
    input_args["rules"] = "gary:::public::firewall/web \
                           gary:::public::firewall/ssh_sgs \
                           gary:::public::firewall/%s" % "database_2tier"

    human_description = "Creates security group = {}".format(sg_db_label)
    long_description = "Creates security group with label={}".format(sg_db_label)
    instructions.add_jiffy_cli(pargs=pargs,
                               order_type=order_type,
                               role=role,
                               human_description=human_description,
                               long_description=long_description,
                               display=True,
                               required_keys=required_keys,
                               jkwargs=input_args)
    #____________________________________________
    input_args = base_args.copy()
    input_args["sg_label"] = "bastion"
    input_args["rules"] = "gary:::public::firewall/web \
                           gary:::public::firewall/bastion" 

    human_description = "Creates security group = {}".format("bastion")
    long_description = "Creates security group with label={}".format("bastion")
    instructions.add_jiffy_cli(pargs=pargs,
                               order_type=order_type,
                               role=role,
                               human_description=human_description,
                               long_description=long_description,
                               display=True,
                               required_keys=required_keys,
                               jkwargs=input_args)

    #____________________________________________
    input_args = base_args.copy()
    input_args["sg_label"] = "web"
    input_args["rules"] = "gary:::public::firewall/web_public \
                           gary:::public::firewall/web_secure_public \
                           gary:::public::firewall/ssh_sgs \
                           gary:::public::firewall/ssh_local_10 \
                           gary:::public::firewall/ssh_local_172 \
                           gary:::public::firewall/ssh/public/default \
                           gary:::public::firewall/ssh/public/dockerguest \
                           gary:::public::firewall/http/public/dockerguest" 

    human_description = "Creates security group = {}".format("web")
    long_description = "Creates security group with label={}".format("web")
    instructions.add_jiffy_cli(pargs=pargs,
                               order_type=order_type,
                               role=role,
                               human_description=human_description,
                               long_description=long_description,
                               display=True,
                               required_keys=required_keys,
                               jkwargs=input_args)

    ###############################################
    instructions.unset_parallel()
    #####################################
    input_args = { "queue_host":"instance","max_wt":"self"} 
    instructions.wait_all_instance(**input_args)
    ###############################################
    pargs = "ec2 security group activate"
    order_type = "activate-cloudsg::api"
    role = "cloud/network"
    human_description = "Activates the security groups"

    instructions.add_jiffy_cli(pargs=pargs,
                               order_type=order_type,
                               human_description=human_description,
                               display=True,
                               role=role)
    ##############################################
    # Publish the variables
    values = {}
    values["vpc"] = vpc
    values["vpc_peer"] = vpc_peer
    values["sg_web"] = sg_web
    values["sg_bastion"] = sg_bastion
    values["sg_db"] = sg_db
    instructions.add_pipeline_metadata(values,publish=True)
    # Pass on additional variables as part of the 
    # infraststructure base
    instructions.set_parallel()
    values["sg_db_label"] = sg_db_label
    values["sg_web_label"] = sg_web_label
    values["sg_bastion_label"] = sg_bastion_label
    values["vpc_label"] = vpc_label
    instructions.add_pipeline_metadata(values,mkey="infrastructure")

    ###############################################
    ## Testing
    ###############################################
    ##content = "name=homer\nsurname=smith"
    #content = {"name":"tom", "surname":"sawyer"}
    #group_name = "Test/Sample"
    #instructions.add_group_envs(content=content,group_name=group_name)
    ###############################################

    ##############################################
    return instructions.get_results()
    ##############################################

def example():

    '''
    '''
