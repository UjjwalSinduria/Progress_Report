**Amazon VPC 3 Tier Architecture**
https://docs.aws.amazon.com/pdfs/whitepapers/latest/serverless-multi-tier-architectures-api-gateway-lambda/serverless-multi-tier-architectures-api-gateway-lambda.pdf#three-tier-architecture-overview

https://medium.com/@aaloktrivedi/building-a-3-tier-web-application-architecture-with-aws-eb5981613e30


- [x] Amazon vpc(virtual private cloud) 3-tier architecture is a blueprint pattern that divides application components into three layers
    , each and ever layer is hosted in a separate subnet with in a vpc

- [x] When building a cloud based application, architecture is as important as application
      Architecture in the sence how much our application is scalabe, how its available and how much secure it is.
    * Scalability
    * Availability
    * Security

- [x] **why do we need 3 tier?**
    * 3 tier architecture increases the scalabilty, availability and security by spreading the application into multiple AZs and spreading
        it into 3 layers, each three layers are independent of each other and does perform different task to each other.
    * If an Az does down for some reason, the application has the ability to automatically scale resources to another AZ.

- [x] **3 Layers or 3 tier** (Each tier has its own security gropups that only allows the inbound/outbound traffic needed to perform      specific tasks.)
    * **Web/Presentation Tier:-** It basically contains the user facing elements of the application, such as web servers and the interface/frontend of the application.
    * **Application Tier:-** It contains the backend and application source code which is needed to process data and run the functions.
    * **Data Tier:-** It contains and manages the application data.(Basically where the databases are stored)
    * ![alt text](image.png)

- [x] Creating the base environment upon which our 3 tier application architecture will be built.
    * A VPC
    * 2 Public subnets in two differnet AZs(Web tier)
    * 2 Private subnets in two differnet AZs(Application tier)
    * 2 Private subnets in two differnet AZs(Database tier)
    * 1 Public route table that connects the public subnets to an internet gateway.
    * 1 Private route table that will connect the Application Tier private subnets and NAT gateway  
    * ![alt text](image-1.png)

