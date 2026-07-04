# Multi-Cloud Cloud Resume Challenge API Backend

This repository forms part of a dual-cloud portfolio architecture demonstrating cross-platform engineering competency across Google Cloud Platform (GCP) and Microsoft Azure.

## 🏗️ Architectural Blueprint

The backend is built as a lightweight, containerised Python microservice that interacts with a serverless NoSQL data layer to track and increment real-time visitor metrics.

* **Frontend:** Vanilla HTML5, CSS3, and JavaScript (Async/Await Fetch API)
* **API Backend Layer:** Python Flask Containerised via Docker 
* **Hosting Compute Environment:** Google Cloud Run (GCP Track) / Azure Container Apps (Azure Track)
* **Database Layer:** Google Cloud Firestore (Native Mode) / Azure Cosmos DB for NoSQL (Serverless)
* **Deployment Region:** London Datacenters (europe-west2 / uksouth)

## ⚡ Key Engineering Takeaways

* **Multi-Cloud Parity:** Designed identical application logic capable of running interchangeably across different cloud provider ecosystems.
* **Serverless Cost-Efficiency:** Leveraged true serverless compute and NoSQL database tiers to maintain a zero-cost idle footprint.
* **Infrastructure as Code (IaC) & Automation:** Managed, provisioned, and cleaned deployment assets via PowerShell 7 using the Google Cloud CLI and Azure CLI toolsets.
# Your frontend live here
