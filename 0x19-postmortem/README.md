# Project: Postmortem

## Postmortem Report: Apache Outage on Docker Container

### Issue Summary
#### Duration of Outage:
* Start: 2024-04-22 14:00 UTC
* End: 2024-04-22 14:45 UTC

#### Impact:
* The Apache service on our Docker container was down.
* Users experienced an inability to access the web service, receiving an "Empty reply from server" error when querying the root of the service.
* Approximately 100% of users attempting to access the service were affected during the outage.

#### Root Cause:
Apache was not started in the Docker container upon initialization.


### Timeline
* 14:00 UTC: Issue detected via user complaint indicating "Empty reply from server" error.
* 14:05 UTC: Monitoring alerts confirmed the web service was down.
* 14:10 UTC: Initial investigation began. The Docker container was checked to ensure it was running.
* 14:15 UTC: Docker container status confirmed as running; however, the service was not responding.
* 14:20 UTC: Assumed network misconfiguration within the Docker container.
* 14:25 UTC: Network settings and firewall rules within the container were verified as correct.
* 14:30 UTC: Escalated to the infrastructure team for deeper inspection.
* 14:35 UTC: Infrastructure team discovered Apache service was not started.
* 14:40 UTC: Apache service was manually started within the Docker container.
* 14:45 UTC: Issue resolved. Apache service was up and running, confirmed by successful curl request returning "Hello Holberton".


### Root Cause and Resolution
#### Root Cause:
The root cause of the outage was due to the Apache web server not being started automatically when the Docker container was initialized.
This was likely due to the container image not including the necessary startup command for Apache.

#### Resolution:
To resolve the issue, the Apache service was manually started within the Docker container using the command service apache2 start.
A script was added to ensure Apache starts automatically when the container is initialized. 

The following command was included in the Docker container configuration:
```bash
Copy code
#!/usr/bin/env bash
# Start Apache service
service apache2 start
```

### Corrective and Preventative Measures
#### Improvements/Fixes:
Enhance container initialization scripts to ensure all necessary services start automatically.
Implement more robust monitoring and alerting for service status within Docker containers.
Conduct a review of all container images to verify that essential services are configured to start on initialization.

#### Tasks to Address the Issue:
1. Patch Docker Image:
Modify the Dockerfile to include the command to start Apache automatically.
```dockerfile
Copy code
FROM ubuntu:latest
RUN apt-get update && apt-get install -y apache2
CMD ["apachectl", "-D", "FOREGROUND"]
```

2. Add Monitoring:
Implement monitoring for Apache service within Docker containers to alert if the service is not running.
Example: Use Nagios or a similar tool to check the status of Apache periodically.

3. Test and Validate:
Conduct thorough testing of the updated Docker image to ensure Apache starts correctly on initialization.
Simulate outages to validate monitoring and alerting mechanisms are working as expected.

4. Documentation Update:
Update the internal documentation to include the steps required to start Apache within the container.
Document the process for adding necessary startup commands in Docker images.

By implementing these measures, we aim to prevent future outages and ensure the reliability of our web services hosted in Docker containers.
