##  Architecture Overview

This project implements a serverless API using AWS cloud services.

### 🔹 Workflow

1. The user sends an HTTP request from a browser  
2. The request is received by API Gateway  
3. API Gateway routes the request to the appropriate endpoint (`/hello` or `/time`)  
4. The request triggers an AWS Lambda function  
5. The Lambda function processes the request and generates a response  
6. The response is returned to the user through API Gateway  

---

### 🔹 Architecture Flow

User → API Gateway → AWS Lambda → Response

---

### 🔹 Key Components

- **API Gateway**: Handles HTTP requests and routing  
- **AWS Lambda**: Executes backend logic without servers  
- **Endpoints**:
  - `/hello` → Returns a greeting message  
  - `/time` → Returns current server time  

---

### 🔹 Summary

This serverless architecture removes the need for server management. It is scalable, cost-effective, and efficient for handling API requests.
