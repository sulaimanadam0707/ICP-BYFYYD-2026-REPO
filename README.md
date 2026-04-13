#  AWS Cloud Computing Portfolio
### Sulaiman Adam | Cloud Computing Intern @ InternCareerPath
This repository contains the end-to-end documentation, architecture diagrams, and cost analysis for two major cloud projects completed during my AWS internship.
##  Project 1: Globally Distributed Static Website
**Goal:** Host a secure, high-performance portfolio website using a serverless architecture.
 * **Services:** Amazon S3, AWS CloudFront.
 * **Key Achievement:** Implemented **Origin Access Control (OAC)** to restrict S3 bucket access, ensuring the site is only accessible via the CloudFront CDN for enhanced security and lower latency.
##  Project 2: Serverless API Integration
**Goal:** Build a dynamic backend to handle requests and return real-time data.
 * **Services:** AWS Lambda, Amazon API Gateway (HTTP API).
 * **Key Achievement:** Developed a Python-based Lambda function and integrated it with an HTTP API, enabling a serverless communication bridge between the frontend and backend.
##  Lessons Learned & Challenges
### 1. The CORS Struggle (Project 2)
**Challenge:** Initially, my frontend couldn't communicate with the API due to "Cross-Origin Resource Sharing" (CORS) errors.
**Lesson:** I learned how to configure API Gateway headers to allow specific origins. This taught me the importance of security handshake protocols in web architecture.
### 2. S3 Security vs. Accessibility
**Challenge:** Making a website public often leads to security vulnerabilities.
**Lesson:** I mastered the use of **CloudFront OAC**. I learned that you should never keep an S3 bucket "public" if you can serve the content through a CDN. It’s safer and faster.
### 3. Cost-Conscious Engineering
**Challenge:** Estimating cloud costs for a "Free Tier" project.
**Lesson:** Using the **AWS Pricing Calculator** taught me that small architectural choices (like choosing **HTTP APIs** over REST APIs) can save significant costs at scale. My entire setup costs only **$0.19/month**.
## 📈 Final Cost Analysis
 * **Total Monthly Estimate:** $0.19
 * **Detailed Report:** View Week 6 Cost Analysis for a CSV file.
## 🛠️ Skills Demonstrated
 * **Cloud Architecture:** Designing multi-service workflows.
 * **Security:** IAM Policies, Bucket Policies, and OAC.
 * **Networking:** DNS management and CDN caching.
 * **DevOps:** Documentation and Version Control via GitHub.
