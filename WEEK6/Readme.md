# 💰 Infrastructure Cost Analysis

## Overview
This report provides a detailed cost estimation for the cloud-native architecture developed during my Cloud Computing Internship. The goal was to design a highly available, globally distributed system while maintaining maximum cost efficiency.

## 📊 Cost Summary
By leveraging the **AWS Free Tier** and choosing high-performance, low-cost services like **HTTP APIs**, the total estimated monthly cost for this entire architecture is:

### **Total: $0.19 / month**

---

## 🏗️ Service Breakdown

| Service | Project | Config Details | Estimated Cost |
| :--- | :--- | :--- | :--- |
| **Amazon S3** | Project 1 | Standard Storage (1GB), 1000 GET requests | $0.00 (Free Tier) |
| **CloudFront** | Project 1 | Global Edge Distribution, 1GB Data Transfer | $0.00 (Free Tier) |
| **AWS Lambda** | Project 2 | 128MB RAM, 10,000 requests, 100ms duration | $0.00 (Free Tier) |
| **API Gateway** | Project 2 | HTTP API, 10,000 requests | $0.19 |

---

## 🔍 Key Insights
- **Free Tier Optimization:** 75% of the services used fall entirely within the "Always Free" or "12-Month Free" tiers.
- **Strategic Service Selection:** I specifically chose **HTTP APIs** over REST APIs for Project 2, as they are nearly 71% cheaper and offer lower latency for serverless workloads.
- **Global Distribution:** Despite the $0.00 price tag, CloudFront provides a globally distributed CDN, proving that high performance does not always require a high budget.



---
*Generated as part of the InternCareerPath Cloud Computing Internship - Week 6.*
