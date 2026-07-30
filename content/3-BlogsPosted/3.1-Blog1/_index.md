---
title: "Blog 1"
date: 2026-07-29
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# [GETTING STARTED WITH AWS SERVERLESS: THE SERVERLESS SERVICES I CHOSE TO BUILD MY WORKSHOP](https://www.facebook.com/share/1DRhj9K5Lu/)

Each service has its own responsibility but is designed to work seamlessly with the others. After understanding how these services interact, I no longer viewed Serverless as a collection of individual technologies, but rather as a modern system design approach in which developers focus on business logic while AWS manages the underlying infrastructure.

Key points to know:

* **AWS Serverless still runs on servers**. Developers do not need to provision or manage the underlying infrastructure; they only need to define the required resources, while AWS automatically provisions and manages the rest.
* **AWS Lambda is the core compute service in most AWS Serverless architectures for implementing business logic**. To improve maintainability and follow best practices, each Lambda function should be designed with a single, well-defined responsibility whenever possible.
* **Amazon API Gateway serves as the entry point for the entire system**. In addition to exposing APIs, it provides features such as JWT-based authorization, CORS configuration, rate limiting, and request logging.
* **Amazon DynamoDB is a NoSQL database service, and its data model should be designed based on access patterns. By that I mean, how the application is expected to query the data in real-world scenarios.
* **Amazon Cognito provides built-in authentication and user management features**. It offers a more secure and reliable approach than hard-coding authentication logic or fixed credentials within the application.

In my opinion, this is one of the main reasons why Serverless has become increasingly popular for modern web and mobile applications. Although it still has limitations, such as cold starts and vendor lock-in, its advantages in scalability, cost efficiency, and rapid development make Serverless an excellent choice for many real-world projects, especially systems with highly variable traffic.

![AWS Serverless services I chose to design the workshop](img/1.jpg)

Posted link: <https://www.facebook.com/share/1DRhj9K5Lu/>