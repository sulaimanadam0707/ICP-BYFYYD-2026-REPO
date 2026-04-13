# Project 1 Completion: Static Website with CDN

## Status: Successfully Deployed

The static website is now live and globally distributed using **Amazon CloudFront** and **Amazon S3**. All core requirements for Project 1 have been successfully met, including secure HTTPS delivery and infrastructure hardening.

---

## Deployment Details

- **Source Files:**  
  The website is powered by `index.html`, `style.css`, and `script.js`.

- **Origin Storage:**  
  Files are hosted in a private **Amazon S3** bucket with public access blocked.

- **Global Delivery:**  
  An **Amazon CloudFront** distribution is configured to serve content through global edge locations for low latency.

- **Security:**  
  **Origin Access Control (OAC)** is implemented to ensure the S3 bucket is only accessible through CloudFront.

---

## Outcome

- Website is live and accessible globally  
- Secure HTTPS enabled  
- Optimized for performance using CDN  
- Infrastructure follows AWS security best practices
