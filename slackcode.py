import requests
import json

slack_hook= 'https://hooks.slack.com/services/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'

def send_to_slack(event,context):
    
    region=event['region']
    instance_id=event['detail']['instance-id']
    state = event['detail']['state']
    slack_msg={'text':f'the ec2 instance {instance_id} in {region} region got {state}'}
    resp = requests.post(slack_hook,data=json.dumps(slack_msg))
    return resp.text
