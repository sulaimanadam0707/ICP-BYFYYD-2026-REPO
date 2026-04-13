# Project 1: Static Website Hosting & Global Content Delivery

## Architecture Overview

This project outlines the technical architecture for a globally distributed static website hosted on **Amazon Web Services (AWS)**. The design is optimized for **high availability**, **low latency**, and follows a **security-first approach** by ensuring no direct public access to the storage origin.

---

## Technical Workflow

### 1. DNS Management (Amazon Route 53)
User requests for the custom domain are resolved via **Amazon Route 53**, which points to the CloudFront distribution.

### 2. Edge Acceleration (Amazon CloudFront)
**Amazon CloudFront** acts as the Content Delivery Network (CDN), caching content at edge locations worldwide to minimize latency.

- **Cache Hit:** The requested file is served directly from the nearest edge location.
- **Cache Miss:** CloudFront securely retrieves the file from the S3 origin.

### 3. Secure Encryption (AWS Certificate Manager)
A public SSL/TLS certificate is provisioned via **AWS Certificate Manager (ACM)** and deployed on CloudFront to enable **HTTPS** encryption.

### 4. Origin Storage (Amazon S3)
Website assets (HTML, CSS, JavaScript, and images) are stored in an **Amazon S3** bucket configured for static website hosting.

---

## Security Hardening & Best Practices

- **Origin Access Control (OAC):**  
  The S3 bucket has **Block Public Access** enabled. Access is restricted only to CloudFront, preventing direct access to files.

- **Protocol Policy:**  
  CloudFront is configured to **redirect HTTP to HTTPS**, ensuring all traffic is encrypted.

- **Least Privilege IAM:**  
  IAM roles are configured with only the necessary permissions for deployment and maintenance.

---

## Expected Outcome

A **production-ready static website** that is:
- Highly available  
- Secure (HTTPS enabled)  
- Globally optimized for performance  
- Accessible via a custom domain  

---

## Acknowledgment

Developed as part of the **InternCareer Path Self-Learning Internship Program**.
