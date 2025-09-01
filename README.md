# AWS-S3-Archiver-Pipeline-with-Generative-AI
This pipeline **automates the process of archiving every day files into structured month/year folders on AWS S3** allowing for clarity and thus easy access to recent data.
A Generative AI model powered by **DeepSeek** is integrated to produce on the last day of the month an **automated report based on the current month's content**, bringing insight for internal use. The report is then delivered to a desired email address.

The pipeline is fully containerized using Docker for easy deployment, portability, and environment consistency.

A Github CI-CD pipeline has been integrated to automatically install dependencies, check syntas, amd run the project on every push to the main branch.

