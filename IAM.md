## IAM
> ### Overview
- Roles are collection of permissions. One can assign Role to identity, but Can not assign permission directly. So, permissions are assigned to identities via roles.
- Service Account is identity for Compute engine. Max 10 keys per Service Account and Max 100 Service Account per project.
- Roles are attached to identities; policies are attached to resources.

![image](https://user-images.githubusercontent.com/19702456/222914917-7c47e20e-2520-493c-adb9-4ac360901a94.png)

![image](https://user-images.githubusercontent.com/19702456/222914943-ce2666bf-cd5b-4db0-a075-62d0f2bf081a.png)

A policy is set on a resource and each policy contains a set of roles and role members.  resources inherit policies from parents so a policy can be set on a resource for example a service and another policy can be set on a parent such as a project that contains that service. The final policy is the union of the parent policy and the resource policy. In case of conflict, if the parent policy is less restrictive it overrides a more restrictive resource policy. 

![image](https://user-images.githubusercontent.com/19702456/222905653-00cbff0f-1444-44f9-9eee-9b47bc93f32b.png)

- roles associated with the account: `gcloud projects get-iam-policy $PROJECT --format='table(bindings.role)' --flatten="bindings[].members" --filter="bindings.members:$USER_EMAIL"`
 
- Add the Dataflow Admin role to the user account: `gcloud projects add-iam-policy-binding $PROJECT --member=user:$USER_EMAIL --role=roles/dataflow.admin`

> ### G Suite and Cloud Identity
- G Suite user is a member of an organization's G Suite domain
- Cloud Identity is like G Suite domain but without access to G suite services

> ### Google Group
- Collection of Identities
- Useful for assigning roles to multiple users
- Identities in group acquire roles assigned to the group and loses when removed from group
