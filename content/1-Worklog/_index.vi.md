---
title: "Nhật ký công việc"
date: 2026-07-30
weight: 1
chapter: false
pre: " <b> 1. </b> "
---

**Trong trang này**, bạn sẽ tìm thấy nhật ký công việc (worklog) chi tiết trong suốt 9 tuần thực tập tại dự án AWS FCAJ (từ 1/6 đến 31/7). Đề tài thực hiện là: Serverless Microservice - Smart QR Attendance API.

Dưới đây là tóm tắt các nhiệm vụ chính đã thực hiện theo từng tuần:

**Tuần 1 (1/6 - 7/6):** [Nhập môn thực tập & chọn đề tài](1.1-week1/)
- Hoàn tất thủ tục thực tập, tìm hiểu nội quy và hướng dẫn
- Tìm nhóm, thảo luận các đề tài tiềm năng
- Nghiên cứu khái niệm kiến trúc AWS Serverless

**Tuần 2 (8/6 - 14/6):** [Thiết lập tài khoản AWS & bài lab cơ bản](1.2-week2/)
- Tạo tài khoản AWS Free Tier và cấu hình AWS Budgets
- Hoàn thành các task kiếm $100 credit: Launch EC2, setup Budget, tạo Lambda web app, tạo Aurora/RDS database
- Tìm hiểu IAM Access Control và cài đặt AWS CLI + CDK
- Cài đặt Kiro IDE, tìm hiểu CloudFormation
- Tham gia sự kiện Meetup (DevOps, Data Analytics, URL Shortener)
- Chốt đề tài: Serverless Microservice - Smart QR Attendance API

**Tuần 3 (15/6 - 21/6):** [Workshop CDK & thiết kế kiến trúc](1.3-week3/)
- Hoàn thành workshop CDK Basic
- Tìm hiểu vẽ kiến trúc AWS trên draw.io
- Bắt đầu workshop CDK nâng cao (Cross-stack references)
- Thiết lập trang báo cáo (Hugo + GitHub Pages)

**Tuần 4 (22/6 - 28/6):** [VPC networking & report site](1.4-week4/)
- Hoàn thành workshop Amazon VPC và AWS Site-to-Site VPN
- Hoàn thành workshop Tối ưu chi phí EC2 với Lambda
- Đẩy trang báo cáo lên GitHub

**Tuần 5 (29/6 - 5/7):** [Phát triển backend Serverless](1.5-week5/)
- Tìm hiểu mô hình Serverless: Lambda + API Gateway + DynamoDB
- Bắt đầu phát triển backend BK-Sync bằng AWS SAM
- Thiết kế schema DynamoDB cho dữ liệu điểm danh
- Tìm hiểu Amazon Cognito cho xác thực người dùng

**Tuần 6 (6/7 - 12/7):** [Tích hợp API & xác thực](1.6-week6/)
- Tích hợp API Gateway với Lambda functions
- Triển khai xác thực người dùng với Amazon Cognito (vai trò Admin, Teacher, Student)
- Cấu hình AWS Secrets Manager để lưu trữ HMAC key
- Tìm hiểu chiến lược tối ưu chi phí và gắn thẻ tài nguyên

**Tuần 7 (13/7 - 19/7):** [Phát triển tính năng backend](1.7-week7/)
- Triển khai pagination cho Admin listUsers API
- Triển khai xem lịch sử điểm danh sinh viên (UC-S04)
- Triển khai tự động đóng session hết hạn (FR-12)
- Tạo pull request để code review

**Tuần 8 (20/7 - 26/7):** [Pipeline kiểm thử & giám sát](1.8-week8/)
- Xây dựng pipeline integration testing tự động cho các tính năng đã triển khai
- Hoàn thành bài lab EC2 cơ bản
- Thiết lập CloudWatch alarms và dashboard giám sát
- Cấu hình SNS alerts cho sức khỏe hệ thống

**Tuần 9 (27/7 - 31/7):** [Hoàn thiện dự án & báo cáo](1.9-week9/)
- Kiểm thử cuối cùng và sửa lỗi cho hệ thống BK-Sync
- Hoàn thiện nội dung trang báo cáo thực tập
- Chuẩn bị slide thuyết trình và quay video demo
- Rà soát và hoàn tất toàn bộ tài liệu