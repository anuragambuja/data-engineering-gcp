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
   
      <img src="https://user-images.githubusercontent.com/19702456/222905653-00cbff0f-1444-44f9-9eee-9b47bc93f32b.png" width="600" height="350" >

> ## G Suite and Cloud Identity
- G Suite user is a member of an organization's G Suite domain
- Cloud Identity is like G Suite domain but without access to G suite services

> ## Google Group
- Collection of Identities
- Useful for assigning roles to multiple users
- Identities in group acquire roles assigned to the group and loses when removed from group

> ## Principals
- Projects have principals (or members) who can make requests, create resources, etc.
- Principals can be identified by their:
  - Google account
  - Service account
  - Google group
  - Google Workspace Account
  - Cloud Identity Account
- There are also two special identifiers:
  - allAuthenticatedUsers
  - allUsers

> ## Roles
- Everything in Google Cloud is done by requesting an action identified by a web service endpoint
  - Principals are not assigned permissions to perform an action
  - Permissions are added to roles which principals are assigned to

- Types of Roles
    - Basic / Primitive Roles: Are project-wide roles
      - Viewer can see everything in a project
      - Editor can change everything in a project
      - Owner has all rights of editor and can add principals.
      - Billing administrator control the billing for a project but not be able to change the resources in the project.

    - Predefined Roles
      - Google defines these roles and assigns what it thinks are sensible permissions for principals working in that role
      - Principals can be assigned any number of roles
      - One role can’t remove permissions granted by another role ○ For example, if you make someone a project owner and a storage viewer, they have read-write access to storage
    
    - Custom Roles
      - Custom roles are ones that you can define.
      - Custom roles provide very fine-grained control over what principals can do.
      - custom roles can only be applied to either the project level or organization level. They can’t be applied to the folder level.
- In production environments, do not grant basic roles unless there is no alternative. Instead, grant the most limited predefined roles or custom roles that meet your needs.

> ## Deny Policies
- A policy is set on a resource and each policy contains a set of roles and role members. IAM policies can be applied at the Organization, Folder, and Project levels. For certain Google Cloud solutions, they can be applied at the Resource level as well. Resources inherit policies from parents so a policy can be set on a resource for example a service and another policy can be set on a parent such as a project that contains that service. The final policy is the union of the parent policy and the resource policy. In case of conflict, if the parent policy is less restrictive it overrides a more restrictive resource policy. 
- With deny policies, you can define deny rules that prevent certain principals from using certain permissions, regardless of the roles they're granted.
- Only a subset of roles can be denied
- Roles are attached to identities; policies are attached to resources.


