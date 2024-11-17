# Cloud Monitoring

- Collect metrices from GCP, AWS and hybrid cloud resources
- Dashboards and Visualizations
- Alerting and Anomaly reporting
- Predefined and custom metrices. For more detailed metrices install monitoring agent.
- By default, the legacy Monitoring agent collects disk, CPU, network, and process metrics. You can configure the agent to monitor third-party applications to get the full list of agent metrics.

# Cloud Logging

- Centralized repository for ingesting logs
- System and application logs
- managed Service
- Uses Google-customized FluentD agent
- Retains logs for 30 days
- Stream logs to pub/sub for 3rd party tools
- Analytics with Bigquery
- Logs can be exported for further analysis. Export destinations include:
  - BigQuery
  - Cloud Storage
  - Pub/Sub
