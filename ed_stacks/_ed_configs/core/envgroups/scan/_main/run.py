def run(instructargs):

    stack = newStack(instructargs)

    stack.parse.add_required(key="schedule_id")
    stack.parse.add_required(key="callback_api_base_endpoint")
    stack.parse.add_required(key="callback_token")
    stack.parse.add_required(key="callback_public_key")
    stack.parse.add_required(key="sched_token")
    stack.parse.add_required(key="content")
    stack.parse.add_required(key="encrypt",default=True)
    stack.parse.add_required(key="run_id",default=None)
    stack.parse.add_required(key="group_name",default=None)

    # Init the variables
    stack.init_variables()

    values = {}
    values["schedule_id"] = stack.schedule_id
    values["sched_token"] = stack.sched_token
    values["content"] = stack.content
    if stack.run_id: values["run_id"] = stack.run_id
    if stack.group_name: values["group_name"] = stack.group_name

    default_values = {}
    default_values["http_method"] = "post"
    default_values["api_endpoint"] = "{}/schedule/scans/groups".format(stack.callback_api_base_endpoint)
    default_values["callback"] = stack.callback_token
    default_values["values"] = "{}".format(str(stack.dict2str(values)))

    if stack.encrypt and stack.callback_public_key: 
        default_values["encrypt"] = True
        default_values["public_key"] = stack.callback_public_key

    pargs = "execute restapi"
    order_type = "saas-upload_scan::api"
    role = "ed/api/execute"
    human_description = "Scanning of schedule_id={}, group_name={} callback to SaaS".format(stack.schedule_id,stack.group_name)

    stack.add_jiffy_cli(pargs=pargs,
                        order_type=order_type,
                        default_values=default_values,
                        human_description=human_description,
                        long_description=human_description,
                        display=True,
                        role=role)

    return stack.get_results()











