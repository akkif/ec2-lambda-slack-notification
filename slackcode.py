import requests
import json

slack_hook= 'S L A C K  W E B  H O O K  U R L'

def send_to_slack(event,context):
    
    region=event['region']
    instance_id=event['detail']['instance-id']
    state = event['detail']['state']
    slack_msg={'text':f'the ec2 instance {instance_id} in {region} region got {state}'}
    resp = requests.post(slack_hook,data=json.dumps(slack_msg))
    return resp.text
