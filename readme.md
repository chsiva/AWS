# use case of lambda what you have done in the lambda.

promotion of data environment. So there is a service called a catalog service. Data is the data and data. So my role was writing a lambda and this is the same thing you know, we have an event triggered , So UI will  create some data in the folder. So it is like handling the data, it's not even large. So lambda, primarily get that data and figure whenever there is a UI activity that happened in the past or in the folder, it will navigate to s3. Anything that is happening between the Ec2  box and S3 bucket and from there, as soon as they sync, it will trigger and move that into other environments.

Q: Okay, so I have a very huge volume of data and I'm doing some processing on the data before moving, but it's taking more than like 30 minutes, half an hour to do the processing. So how I can do with the lambda 

So you have to paralyzed lambdas (multiple API lambda functions) and other lambdas them Right. So you can paralyze it that you've been doing
if you want to have lambdas, just like acting as a word causes like getting some information, you want to have data, like 1000/10,000 files, and you want 1000 files to be processed.  Please say if you want one lambda doing one after the other, then it will take lot of time. So if u set up timeout in 15 minutes and within this time i will paralyze that and   where  i will add 10 more lamdas So it'll be like 5000. 






#IAM (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html)



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
    
 # Cloud Formation
     Yes, I have used like cloud formation templates before for provisioning services like EC to s3, I am
    
