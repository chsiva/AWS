Q1. is it a good idea to place database behind autoscaling group?

Ans.

Q2. Steps to attach rds to the load balancer?

Ans.

Q3. Can we change private IP address? 

    There is no chance of changing a private IP address

Q4. Encrypt EBS Volumes.Do we need to stop EC2 instance?

    IAM KMS encryption key should be available. Take snapshot of the root volume attached to ec2.
    Create a new Encrypted volume from the encrypted snapshot and Detach the existing volume and attach the Encrypted Volume.
