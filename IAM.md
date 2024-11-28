# IAM

  ![image](https://github.com/user-attachments/assets/6fe32403-ce6b-497c-982a-ad40593ac1f0)

- With Identity Access Management, you first identify the caller to the API. The caller could be identified as a human, a computer, or an application. Once identified, the caller is known as a member. Members are assigned one or more roles.
- Inheritance Model
  - Organization
    - Root node for all Google Cloud resources
    - Each Google Workspace or Cloud Identity account (domain) is associated with exactly one organization
    - It allows the enforcement of organization-wide security and governance policies
  - Folders
    - Grouping mechanism that facilitates security governance by acting as a policy inheritance point for IAM and Organization policies
  - Projects
    - Basic level of Google Cloud organization and a logical grouping of resources
    - In Google Cloud, every request and resource must be assigned to a project
    - Doesn't correspond to a particular Google Cloud geographic region
    - Each project is assigned a billing account

> ### G Suite and Cloud Identity
- G Suite user is a member of an organization's G Suite domain
- Cloud Identity is like G Suite domain but without access to G suite services

> ### Google Group
- Collection of Identities
- Useful for assigning roles to multiple users
- Identities in group acquire roles assigned to the group and loses when removed from group

> ## Principals
- Projects have principals (or members) who can make requests, create resources, etc.
- Principals can be identified by their:
  - Google account
  - Service account
  - Google group
  - G Suite domain
- There are also two special identifiers:
  - allAuthenticatedUsers
  - allUsers

> ## Roles
- Everything in Google Cloud is done by requesting an action identified by a web service endpoint
  - Principals are not assigned permissions to perform an action
  - Permissions are added to roles which principals are assigned to
- Roles encapsulate a set of permissions
  - Google defines the roles and grants permissions that would be required for someone working in that role
- Types of Roles

    ![image](https://user-images.githubusercontent.com/19702456/222914943-ce2666bf-cd5b-4db0-a075-62d0f2bf081a.png)
    - Basic Roles: Are project-wide roles
      - Project viewer can see everything in a project
      - Project editor can change everything in a project
      - Project owner has all rights of editor and can add principals

    - Predefined Roles
      - Google defines these roles and assigns what it thinks are sensible permissions for principals working in that role
      - Principals can be assigned any number of roles
      - One role can’t remove permissions granted by another role ○ For example, if you make someone a project owner and a storage viewer, they have read-write access to storage
    - Custom Roles
      - Custom roles are ones that you can define.
      - Custom roles provide very fine-grained control over what principals can do. 
- Basic roles include thousands of permissions across all Google Cloud services. In production environments, do not grant basic roles unless there is no alternative. Instead, grant the most limited predefined roles or custom roles that meet your needs.

> ## Deny Policies
- With deny policies, you can define deny rules that prevent certain principals from using certain permissions, regardless of the roles they're granted.
- Only a subset of roles can be denied


--------

- Roles are collection of permissions. When you assign a member to a role, you are permitting them to invoke all the API functions granted by that role. One can assign Role to identity, but Can not assign permission directly. So, permissions are assigned to identities via roles.
- The binding of an identity to an IAM role is called an IAM policy. IAM policies can be applied at the Organization, Folder, and Project levels. For certain Google Cloud solutions, they can be applied at the Resource level as well.
  
- Service Account is identity for Compute engine. Max 10 keys per Service Account and Max 100 Service Account per project.
- Roles are attached to identities; policies are attached to resources.

![image](https://user-images.githubusercontent.com/19702456/222914917-7c47e20e-2520-493c-adb9-4ac360901a94.png)



A policy is set on a resource and each policy contains a set of roles and role members.  resources inherit policies from parents so a policy can be set on a resource for example a service and another policy can be set on a parent such as a project that contains that service. The final policy is the union of the parent policy and the resource policy. In case of conflict, if the parent policy is less restrictive it overrides a more restrictive resource policy. 

![image](https://user-images.githubusercontent.com/19702456/222905653-00cbff0f-1444-44f9-9eee-9b47bc93f32b.png)

- roles associated with the account: `gcloud projects get-iam-policy $PROJECT --format='table(bindings.role)' --flatten="bindings[].members" --filter="bindings.members:$USER_EMAIL"`
 
- Add the Dataflow Admin role to the user account: `gcloud projects add-iam-policy-binding $PROJECT --member=user:$USER_EMAIL --role=roles/dataflow.admin`

