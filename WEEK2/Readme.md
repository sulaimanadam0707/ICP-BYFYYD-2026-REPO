# Project 1: Static Website Hosting & Global Content Delivery

## Architecture Overview
This project outlines the technical architecture for a globally distributed static website hosted on **Amazon Web Services (AWS)**. [span_0](start_span)The design is optimized for high availability, low latency, and follows the "Security First" principle[span_0](end_span) [span_1](start_span)by ensuring no direct public access to the storage origin[span_1](end_span).

## Technical Workflow

1.  **[span_2](start_span)[span_3](start_span)DNS Management (Amazon Route 53):** User requests for the custom domain are resolved via **Amazon Route 53**, which points to the CloudFront distribution[span_2](end_span)[span_3](end_span).
2.  **[span_4](start_span)[span_5](start_span)Edge Acceleration (Amazon CloudFront):** **Amazon CloudFront** acts as the Content Delivery Network (CDN), caching content at Edge Locations worldwide to minimize latency[span_4](end_span)[span_5](end_span).
    * **[span_6](start_span)Cache Hit:** The requested file is served directly from the nearest Edge Location[span_6](end_span).
    * **[span_7](start_span)Cache Miss:** CloudFront securely retrieves the file from the S3 origin[span_7](end_span).
3.  **[span_8](start_span)Secure Encryption (AWS Certificate Manager):** A public SSL/TLS certificate is provisioned via **AWS Certificate Manager (ACM)** and deployed on the CloudFront distribution to enable end-to-end **HTTPS** encryption[span_8](end_span).
4.  **[span_9](start_span)[span_10](start_span)Origin Storage (Amazon S3):** Website assets (HTML, CSS, JS, and images) are stored in an **Amazon S3** bucket configured for static website hosting[span_9](end_span)[span_10](end_span).

## Security Hardening & Best Practices
* **[span_11](start_span)Origin Access Control (OAC):** The S3 bucket is configured with **Block Public Access** enabled[span_11](end_span). [span_12](start_span)Access is restricted exclusively to the CloudFront distribution using an OAC policy, preventing users from bypassing the CDN to access files directly[span_12](end_span).
* **[span_13](start_span)[span_14](start_span)Protocol Policy:** CloudFront is configured to **Redirect HTTP to HTTPS**, ensuring all user traffic is encrypted in transit[span_13](end_span)[span_14](end_span).
* **[span_15](start_span)[span_16](start_span)Least Privilege IAM:** Specific IAM roles have been created to allow only the necessary permissions for deployment and maintenance[span_15](end_span)[span_16](end_span).

## Expected Outcome
[span_17](start_span)[span_18](start_span)A production-ready, highly available static website accessible via a secure custom domain with global performance optimization[span_17](end_span)[span_18](end_span).

---
*[span_19](start_span)Developed as part of the InternCareer Path Self-Learning Internship Program[span_19](end_span).*
