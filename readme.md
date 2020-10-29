Q1. is it a good idea to place database behind autoscaling group?

Ans.

Q2. Steps to attach rds to the load balancer?
       1-If you mean having only one RDS instance, there is no point in load balancing requests in front of it. If you mean having more than one RDS instance, it does not make much sense as well to load balance requests, because your database servers will most likely have different data in a given point of time. The only exception that I can see to this rule is if you have read-only RDS instances. In this case, you can probably benefit of having ELB(s) in front of them. If your application is write-intensive, you should stick with a larger RDS instance or move to a noSQL database. Don't try to load balance requests to a read/write DMBS, because you will have to deal with synchronization and a lot of other (non-trivial) aspects by yourself.

Q3. Can we change private IP address? 

    There is no chance of changing a private IP address

Q4. Encrypt EBS Volumes.Do we need to stop EC2 instance?

    IAM KMS encryption key should be available. Take snapshot of the root volume attached to ec2.
    Create a new Encrypted volume from the encrypted snapshot and Detach the existing volume and attach the Encrypted Volume.
