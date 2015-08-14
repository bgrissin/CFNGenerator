# AWS CloudFormation Script to generate JSON templates for CloudFormation Stack Creation
# Author : Nicola Kabar
# Version : 0.1
import json
from datetime import datetime

################ Settings ############################
description= "Description" # Alphanumeric ONLY. Used when generating instance names
owner = "Owner" 
image_id = "ami-17471c27" # AMI ID . Default Ubuntu 14.04 Trusty 
instance_type = "m3.large" # Select from your available instance types
security_groups_ids = ["sg-xxxxxxxx",] #  A list of all security groups that these instance should belong to.
subnet_id = "subnet-xxxxxx" 
key_names = ["user-01","user-02","user-03","user-04"] # List of all the key names that you need to generate instances for. Keys need to be created manually. 
num_per_key = 1 # Number of instances per user
availability_zone = "us-west-2c"  # Based on Subnet AZ
######################################################

template = {
  "AWSTemplateFormatVersion" : "2010-09-09",
  "Resources" : {},
  "Outputs" : {}}
if __name__== "__main__":
  template['Description']=description
  for index,key_name in enumerate(key_names):
    for num in range(0,num_per_key):
      instance_name = description + str(index) + str(num) # Instance name definition
      template["Resources"][instance_name]={}
      template["Resources"][instance_name]["Type"]="AWS::EC2::Instance"
      template["Resources"][instance_name]["Properties"]={}
      template["Resources"][instance_name]["Properties"]["InstanceType"]=instance_type
      template["Resources"][instance_name]["Properties"]["SecurityGroupIds"]=security_groups_ids
      template["Resources"][instance_name]["Properties"]["SubnetId"]=subnet_id
      template["Resources"][instance_name]["Properties"]["KeyName"]=key_name
      template["Resources"][instance_name]["Properties"]["ImageId"]=image_id
      template["Resources"][instance_name]["Properties"]["AvailabilityZone"]= availability_zone
      template["Resources"][instance_name]["Properties"]["Tags"]={}
      template["Resources"][instance_name]["Properties"]["Tags"]=[
            {"Key" : "Name", "Value" : str(owner)+'-'+str(instance_name)},
            {"Key" : "Owner", "Value" : owner }
      ] 

  # JSONizing
  template_json=json.dumps(template,indent=4,sort_keys=True)

  # Writing it to a file on local dir
  with open(description+'-'+ datetime.now().strftime('%Y-%m-%d %H:%M:%S').replace(" ","-") +'.json','w') as f:
    f.write(template_json)



    


  
