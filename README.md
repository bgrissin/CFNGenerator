# CFNGenerator
 AWS CloudFormation Script to generate JSON templates for CloudFormation Stack Creation
 
Wrote a quick Python script that can spin up N instances on AWS. Just need to edit the "Settings" part of the script, run it ( #python cfnTemplateGenerator.py), and upload the .json file it produces on local dir into CloudFormation. You have to have previously created the key pairs, vpc, subnet, and secruity groups.
