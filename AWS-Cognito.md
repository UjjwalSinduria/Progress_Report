- [x] <ins>**Amazon Cognito**</ins>:
    *   It is a service which is fully managed by the AWS that simplifies user authentication, authorization and manage user crendentials
        for web and mobile applications.
    *   It allows you to add secure SignUp, SignIn and access control for our application.
    *   Amazon cognito is particular suitable for developers who want to offload the complexity of building a secure and scalable identity
        system.

- [x] <ins>**Security Measures provided by cognito**</ins>
    *   UserData is encrypted and Transmitted securily over the internet using SSL/TSL protocol.
        *   **SSL**: Secure Socket Layer
        *   **TSL**: Transport Security Layer
    *   MFA's(Multi-factor authentications)
    *   Account Recovery
    *   Password Reset

- [x] **IAM is also a way of authenticating users, so why do we need cognito?**
    *   If your application primarly deals with user authentication and management. Cognito handles the user-related aspects of an
        application such as:
        *   User Registration
        *   Sign In
        *   Sign Up
        *   MFA
    *   IAM is used for setting and managing permissions for various AWS Resources. Basically its ensuring your application backend 
        components have necessary permissions to function securily.

- [x] <ins>**key components of AWS cognito are:**</ins>
    *   <ins>**UserPool**</ins> :
        *   Basically it is a user directory, we can imagine it as a register which contains all the user crendentials like userName
            , Password, emails etc.
        *   It Manages many thing:
            *   Phone no by sending verification code
            *   Handling forgotten password
            *   Changing Existing password
            *   It supports MFA and captcha also
                *   Captcha(Completely automated public turing test to tell and humans apart):
                    *   It makes more difficult for scammers to use automated bots to register fake accounts.
                    *   Handles Spam Comments
                    *   Handles Online Polling
                    *   Handles Ticket Scaling and many more
            *   It also provide password policies and token based authorization.
                *   **Password Policies**: Refers to the set of Rules that a user must follows while creating or upadting a password.
                    *   Minimum Length
                    *   Use of alphanumeric characters
                    *   Use of UpperCase and LowerCase
            *   Supports Identity Federation:
                *   Combine userpool with 3rd party authentication services such as Google, amazon, facebook, apple etc.

    *   <ins>**Identity Pool**</ins>:
        *   Allows you to grant your user to access aws services by providing temporary aws credentials.
            *   Eg: Getting authenticated by one of Identity provider and you will get the authorization token from the provider which
                we can can send to the cognito Identity Pool. The Identity Pool will verify the token and issue the user temperary AWS
                crendentials which you can use to access the desired resources.
    *   <ins>**Sync**</ins>:
        *   It allows us to sync user data accross the multiple devices.    
            
    
