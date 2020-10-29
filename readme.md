Q1. is it a good idea to place database behind autoscaling group?

Ans.

Q2. Steps to attach rds to the load balancer?
    https://www.infosysblogs.com/cloud/2019/06/rds_-_scaling_and_load_balanci_1.html

Q3. Can we change private IP address? 

    There is no chance of changing a private IP address

Q4. Encrypt EBS Volumes.Do we need to stop EC2 instance?

    IAM KMS encryption key should be available. Take snapshot of the root volume attached to ec2.
    Create a new Encrypted volume from the encrypted snapshot and Detach the existing volume and attach the Encrypted Volume.
    
Q5. Purpose of Autoscaling group? horizontal vs vertical scaling? 
    https://stackoverflow.com/questions/33067241/how-exactly-does-auto-scaling-in-aws-work

    
    Autoscaling uses horizontal scaling (adding more instances) and not vertical scaling (increasing CPU/memory allotment)
    In order to successfully use auto scaling, you need to design your application using the principle of shared nothing architecture. 
    No persistent data can be stored on the instance itself. Instead you would store it on S3, or other instances not part of autoscaling group.
    
Q6: S3 permissions on bucket itself?
   
    Amazon S3 labels the permissions for a bucket as follows:

    1. Public – Everyone has access to one or more of the following: List objects, Write objects, Read and write permissions.

    2. Objects can be public – The bucket is not public, but anyone with the appropriate permissions can grant public access to objects.

    3. Buckets and objects not public – The bucket and objects do not have any public access.

    4. Only authorized users of this account – Access is isolated to IAM users and roles in this account and AWS service principals because there is a policy that          grants public access.
    
