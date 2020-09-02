import json
import boto3

def lambda_handler(event, context):
    detail = event['detail']
    ids = detail['instance-id']
    eventname = detail['state']
    ec2 = boto3.resource('ec2')
    
    while eventname == 'Running':
        print(ids)       
    #Check to see if backup tag is added to the instance
        tag_to_check = 'Backup'
        instance = ec2.Instance(ids)
        for tag in instance.tags:
            if tag_to_check not in [t['Key'] for t in instance.tags]:
                instance.stop()
                print("Stopping Instance: ", instance)
    #Get instance state to break the infinite loop
                state = instance.state['Name']          
                if state == "shutting-down":
                    print("instance is shutting-down")
                    break
                elif state == "stopped":
                    print("Instance is already stopped")
                    break
                elif state == "stopping":
                    print("instance is stopping")
                    break
        break
            