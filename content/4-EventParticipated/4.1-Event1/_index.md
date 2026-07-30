---
title: “FCAJ meetup day 2026”
date: 2026-06-13
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Summary Report: “FCAJ meetup day 2026”

### Event Objectives
- Share practical insights into the real-world responsibilities and mindset of a DevOps Engineer[cite: 1].
- Guide the design and architecture of a scalable URL shortening service on AWS[cite: 2].
- Outline the roadmap from student curiosity to becoming an AWS Partner and engaging with the community[cite: 3].
- Share practical career advice for Data Analytics Engineers and insights into Multinational Corporation (MNC) culture[cite: 4].

### Speakers
- **Trong H. Truong** – DevOps Engineer @ Endava Vietnam[cite: 1]
- **Đinh Trung Kiên** – Lead developer at startup[cite: 2]
- **Nguyễn Minh Thọ** – Student[cite: 2]
- **Danh Hoàng Hiếu Nghị** – AI Engineer, AWS Community Builder, AWS Student Builder Group Leader[cite: 3]
- **Đạt Phạm** – Data Analytics Engineer[cite: 4]
- **Cường Nguyễn** – Process Engineer[cite: 4]

### Key Highlights

#### What a DevOps Engineer Really Does
- The scope of DevOps depends heavily on context, such as company size, team structure, and product complexity[cite: 1].
- Real-world tasks extend beyond CI/CD pipelines to involve 24/7 on-call rotation, incident handling, troubleshooting, access support, and cost investigation[cite: 1].
- Strong emphasis is placed on fundamentals like Linux, networking basics, and programming languages rather than just learning specific tools[cite: 1].

#### Scalable URL Shortener Architecture on AWS
- Simple URL shorteners face drawbacks such as vulnerability, read latency, and single points of failure[cite: 2].
- The proposed scalable architecture utilizes Amazon CloudFront, WAF, Route 53, Amazon ECS (SpringBoot), DynamoDB, and Amazon ElastiCache (Redis)[cite: 2].
- A Key Generation Service (KGS) pre-computes short codes and pushes them to a Redis queue to ensure that creation requests are instant and collision-free[cite: 2].
- The read path implements a cache-aside pattern where reads are served from the in-memory cache first, minimizing database stress and keeping latency low[cite: 2].

#### Career Development and MNC Culture
- A career growth model for engineers spans five stages: Follower, Learner, Problem Solver, System Thinker, and Super Star[cite: 4].
- Data Analytics Engineers must equip themselves with critical thinking, communication, data storytelling, and problem-solving skills[cite: 4].
- Multinational Corporations (MNCs) maintain a "No-Blame Post-Mortem" culture in tech, focusing on root causes to fix systems rather than blaming individuals[cite: 4].
- The journey to becoming an AWS Partner involves an 8-step process starting from student curiosity, moving through hands-on labs, school projects, and ultimately sharing back with the community[cite: 3].

### Key Takeaways

#### Design Mindset
- **Separation of Concerns:** Read and write paths should be handled independently, optimized for their own traffic patterns rather than sharing a single bottleneck[cite: 2].
- **Defense at the Edge:** Security and caching should be pushed as close to the user as possible so threats do not reach the core system[cite: 2].
- **System Thinking:** Focus on optimizing the long-term system rather than just fixing minor tasks[cite: 1].

#### Career Strategy
- **Learn Fundamentals:** Tools change, but fundamentals stay[cite: 1].
- **Ask "Why" Before "How":** Understand the root cause of problems rather than just copying commands[cite: 1].
- **Adopt the "Đúng Việc" Philosophy:** Balance being a good human (Fulfillment), a purposeful professional, and a responsible citizen leaving a legacy for the community[cite: 4].

### Applying to Work
- **Implement Pre-computation:** Generate data ahead of time (like the Key Generation Service) to reduce processing time during user requests[cite: 2].
- **Apply the Cache-aside Pattern:** Optimize read-heavy services by implementing Redis caching before querying the main database[cite: 2].
- **Practice Data Storytelling:** Transform dry numbers into meaningful narratives to drive actionable business decisions[cite: 4].
- **Engage with Communities:** Participate in AWS Study Groups and Community Builder programs to continuously learn and share knowledge[cite: 3].

### Event Experience

Attending the **FCAJ Meetup Day 2026** was extremely valuable, providing a comprehensive view of modern AWS architecture, real-world DevOps, and career progression. Key experiences included:

#### Learning from highly skilled speakers
- Experts shared the unglamorous but critical realities of being a DevOps Engineer, emphasizing the importance of communication and collaboration[cite: 1].
- Gained practical knowledge on designing scalable cloud architectures using AWS services like DynamoDB and ElastiCache[cite: 2].

#### Hands-on technical exposure
- Understood how to solve URL collision and latency issues using a Key Generation Service and Redis queues[cite: 2].
- Learned the importance of defense at the edge to prevent threats from reaching the core system[cite: 2].

#### Career and Culture Insights
- Discovered the 5-stage career roadmap from Follower to Super Star[cite: 4].
- Learned about the MNC hiring process and the importance of a "No-Blame" and "Caring & Inclusive" culture for continuous improvement[cite: 4].
- Was inspired by the 8-step journey to becoming an AWS Partner and the value of community contribution[cite: 3].

#### Some event photos
![Photo 1](images/event1_1.jpg)
![Photo 2](images/event1_2.jpg)
> Overall, the event not only provided technical knowledge on AWS architectures but also helped me reshape my thinking about career development, system thinking, and multinational corporate culture.