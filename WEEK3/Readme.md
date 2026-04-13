Project 1: Static Website Hosting & Global Content Delivery
Architecture Overview
This project demonstrates the deployment of a globally distributed static website using Amazon Web Services (AWS).
The architecture is designed for high availability, low latency, and follows a security-first approach by preventing direct public access to the storage origin.
Technical Workflow
1. DNS Management (Amazon Route 53)
User requests to the custom domain are resolved using Amazon Route 53, which routes traffic to the CloudFront distribution.
2. Edge Acceleration (Amazon CloudFront)
Amazon CloudFront acts as a Content Delivery Network (CDN), caching content at edge locations worldwide to improve performance.
Cache Hit: Content is served directly from the nearest edge location.
Cache Miss: CloudFront retrieves content securely from the S3 origin.
3. Secure Encryption (AWS Certificate Manager)
An SSL/TLS certificate is provisioned using AWS Certificate Manager (ACM) and attached to CloudFront to enable secure HTTPS connections.
4. Origin Storage (Amazon S3)
All website assets (HTML, CSS, JavaScript, images) are stored in an Amazon S3 bucket configured for static website hosting.
Security Hardening & Best Practices
Origin Access Control (OAC):
The S3 bucket has Block Public Access enabled. Access is restricted to CloudFront only, preventing direct access to files.
Protocol Policy:
HTTP requests are automatically redirected to HTTPS to ensure secure communication.
Least Privilege IAM:
IAM roles are configured with minimal permissions required for deployment and maintenance.
Expected Outcome
A production-ready static website that is:
Secure (HTTPS enforced)
Highly available
Optimized for global performance
Accessible via a custom domain
Acknowledgment
Developed as part of the InternCareer Path Self-Learning Internship Program.
