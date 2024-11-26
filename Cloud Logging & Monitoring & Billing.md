# Cloud Monitoring

- Collect metrices from GCP, AWS and hybrid cloud resources
- Dashboards and Visualizations
- Alerting and Anomaly reporting
- Predefined and custom metrices. For more detailed metrices install monitoring agent.
- By default, the legacy Monitoring agent collects disk, CPU, network, and process metrics. You can configure the agent to monitor third-party applications to get the full list of agent metrics.

# Cloud Logging

- Centralized repository for ingesting System and application logs
- managed Service
- Uses Google-customized FluentD agent
- Retains logs for 30 days
- Stream logs to pub/sub for 3rd party tools
- Analytics with Bigquery
- Logs can be exported for further analysis. Export destinations include:
  - BigQuery
  - Cloud Storage
  - Pub/Sub

    ![image](https://github.com/user-attachments/assets/4656fd68-530a-4f3c-b9ae-824296715918)


# Billing, Budgets and Alerts
- Alerts and budgets are a way to manage your spend after the fact. Billing IAM roles are a way to prevent who can spend in the first place.
- A billing account is therefore attached to an organization and pays for the projects which are attached to it.
- A single billing account can pay for all your projects. Google recommends using a single billing account as far as possible.
- A budget enables you to track your actual Google Cloud costs against your planned costs. After you've set a budget amount, you set budget alert threshold rules that are used to trigger email notifications. Budget alert emails help you stay informed about how your spend is tracking against your budget. You can also use budgets to automate cost control responses.
- A quota restricts how much of a particular shared Google Cloud resource your Google Cloud project can use, including hardware, software, and network components. Most quotas are applied per project, based on resource type and location.
- Why use Quotas and Rate Limits ?
  - Prevent runaway consumption in case of an error or malicious attack
  - Prevent billing spikes or surprises
  - Forces sizing consideration and periodic review
  - Quotas and Rate Limits are hard ceilings. Budgets are guidelines that do not have ceilings. When a quota is exceeded, in most cases, the system immediately blocks access to the relevant Google resource, and the task that you're trying to perform fails.
- There are three categories of Google Cloud quotas:
  - Rate quotas are typically used for limiting the number of requests that you can make to an API or service. Rate quotas reset after a time interval that is specific to the service—for example, the number of API requests per day.
  - Allocation quotas are used to restrict the use of resources that don't have a rate of usage. For   example, the number of VMs used by your project at a given time. Allocation quotas don't reset over time. Instead, they must be explicitly released when you no longer want to use them—for example, by deleting a GKE cluster.
  - Concurrent quotas are used to restrict the total number of concurrent operations in flight at any given time. These are usually long-running operations. For example, Compute Engine uses insert_operations that are expected to last as long as one hour.
- Quota increase requests are a manual process and are not immediate, but some have pre-approval.
- Custom quotas are approximate. The custom quotas feature provides an additional safeguard against excessive spending, but is not designed to strictly limit bytes processed. BigQuery might occasionally run a query that exceeds a quota. Daily quotas reset at midnight Pacific Time. Custom quota is proactive and project specific, so you won't be able to run an 11 TB query if you have a 10 TB quota. 


