def run(instructargs):

    #####################################
    instructargs["add_cluster"] = False
    instructargs["add_instance"] = False
    stack = newStack(instructargs)
    #####################################

    stack.parse.add_required(key="size",default="t2.micro")
    stack.parse.add_required(key="disksize",default=50)
    stack.parse.add_required(key="image",default=instructargs.get("image"))
    stack.parse.add_required(key="image_ref",default="github_13456777:::public::ubuntu.16.04-chef_solo")
    stack.parse.add_required(key="timeout",default=600)
    stack.parse.add_required(key="security_group",default="default")
    stack.parse.add_required(key="region",default="us-west-1")
    stack.parse.add_required(key="vpc_label",default='vpc')
    stack.parse.add_required(key="user",default='ubuntu')
    stack.parse.add_required(key="ip_key",default='private_ip')

    stack.parse.add_required(key="placement",default='_None')
    stack.parse.add_required(key="vpc",default='_None')
    stack.parse.add_required(key="sg",default='_None')
    stack.parse.add_required(key="sg_label",default='_None')
    stack.parse.add_required(key="tags",default='_None')
    stack.parse.add_required(key="comment",default='_None')

    # Initialize Variables in stack
    stack.init_variables()

    # Create server
    default_values = {}
    default_values["size"] = stack.size
    default_values["disksize"] = stack.disksize
    default_values["image"] = stack.image
    default_values["image_ref"] = stack.image_ref
    default_values["timeout"] = stack.timeout
    default_values["security_group"] = stack.security_group
    default_values["region"] = stack.region
    default_values["vpc_label"] = stack.vpc_label
    default_values["placement"] = stack.placement
    default_values["vpc"] = stack.vpc
    default_values["sg"] = stack.sg
    default_values["sg_label"] = stack.sg_label
    default_values["tags"] = stack.tags
    default_values["comment"] = stack.comment

    substack = stack.new_substack("gary:::public::Cloud/Ec2/server")
    substack.required_keys = [ "hostname", "key" ]
    substack.human_description = "Instruction: Creates a Server on Ec2"
    substack.display = True
    substack.default_values = default_values
    stack.commit_substack()

    # Bootstrap server
    default_values = {}
    default_values["ip_key"] = stack.ip_key
    default_values["user"] = stack.user
    default_values["tags"] = stack.tags
    required_keys = [ "hostname", "key" ]

    human_description = "Bootstraps host to Jiffy database"

    stack.create_substack("gary:::public::Core/Host/Ubuntu/add_host",
                          required_keys=required_keys,
                          human_description=human_description,
                          long_description=human_description,
                          display=None,
                          default_values=default_values)

    # Return results
    return stack.get_results()

def example():

    print '''


    #CLI

    jiffy orders add instruction name=Cloud/Ec2/OS/ubuntu cluster=nevada instance=valiant \\
    arguments="hostname=test_machine key=sf region=us-east-1 tags=test"

    #Within a VPC asigned to a cluster and instance

    jiffy orders add instruction name=Cloud/Ec2/OS/ubuntu cluster=nevada instance=valiant \\
    arguments="hostname=nevada-reno-web-1 disksize=15 sg_label=web key=sf tags=web"

    #Available Arguments:

    1) Required

    hostname
    key

    2) Defaults

    cluster = cluster of parent order 
    instance = instance of parent order
    user = ubuntu
    size = t1.micro
    image = ami-d05e75b8
    timeout = 600
    security_group = default
    region = us-east-1
    ip_key = private_ip
    user = ubuntu
    disksize = None
    placement = None
    vpc = None
    vpc_label = 'vpc'
    sg = None
    sg_label = None
    security_group = 'default'
    tags = None
    comments = None
    '''
