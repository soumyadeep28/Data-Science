
import time
from time import sleep
import boto3
client = boto3.client('sns','us-east-1')
client.publish(PhoneNumber='+919062683440', Message='Sent from python')




'''
the task which we have performed to send the msg via AWS 

install awscli using
 pip install awscli

install boto3
 pip install boto3

enter details (in AWS colsole create IAM for creating SNS full access access)
AWS Access Key ID [None]: AKIA45QXFDBNCAN3EBIA
AWS Secret Access Key [None]: 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
Default region name [None]: us-east-1
Default output format [None]:


'''