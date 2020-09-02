# Lambda Function to Force Tags
This lambda function will check your instances when they are started and in a "running" state to see if they have the required tags.

If they do not have the required tags then the function will shut them down.

## Usage
You need to setup EventBridge within AWS to execute this function when an EC2 instance has a state change.

### More Info
You can find more information [here](https://aaron.vansledright.com/check-ec2-instance-tags-on-launch/)