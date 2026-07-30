---
title: "Blog 2"
date: 2026-07-29
weight: 1
chapter: false
pre: " <b> 3.2. </b> "
---

# [AWS SAM LÀ GÌ? TẠI SAO AWS SAM KHÔNG ĐƯỢC XEM LÀ MỘT DỊCH VỤ SERVERLESS CỦA AWS?](https://www.facebook.com/share/1DRhj9K5Lu/)

Trước khi bắt đầu dự án, mình thường nghĩ việc triển khai hạ tầng chỉ là bước cuối cùng sau khi hoàn thành mã nguồn. Tuy nhiên, quá trình sử dụng AWS SAM giúp mình nhận ra rằng thiết kế hạ tầng và phát triển ứng dụng nên diễn ra song song. Việc mô tả toàn bộ hệ thống bằng `template.yaml` không chỉ giúp triển khai nhanh hơn mà còn mang lại nhiều lợi ích như dễ bảo trì, dễ chia sẻ, dễ kiểm soát phiên bản và dễ tích hợp vào quy trình CI/CD. Đây cũng là nền tảng để xây dựng các hệ thống có khả năng mở rộng trong môi trường thực tế.

Bên cạnh đó, mình hiểu rằng AWS SAM không phải là một dịch vụ thay thế Lambda hay API Gateway. Thay vào đó, nó giống như một "kiến trúc sư" giúp mô tả cách các dịch vụ Serverless được kết nối với nhau trước khi AWS CloudFormation tiến hành xây dựng toàn bộ hệ thống.

Các điểm chính cần nắm:

* **Nên áp dụng phương pháp "Infrastructure as Code (IaC)"**, trong đó toàn bộ hạ tầng được mô tả bằng mã nguồn thay vì cấu hình thủ công trên giao diện quản lý. Cách tiếp cận này giúp hạ tầng được quản lý nhất quán, dễ bảo trì, dễ chia sẻ và dễ đồng bộ giữa các môi trường triển khai.
* **AWS SAM là một framework hỗ trợ phát triển và triển khai ứng dụng Serverless theo phương pháp IaC**. Framework này cho phép mô tả và quản lý hạ tầng bằng mã nguồn tương tự như cách quản lý mã nguồn của ứng dụng.
* **AWS SAM** cung cấp bốn lệnh cơ bản thường được sử dụng trong quá trình phát triển và triển khai ứng dụng: `sam init`, `sam build`, `sam local`, và `sam deploy`.
* **File `template.yaml` là thành phần quan trọng nhất của một dự án AWS SAM**, vì nó mô tả toàn bộ tài nguyên AWS và mối quan hệ giữa các thành phần trong hệ thống, từ đó phản ánh kiến trúc của ứng dụng một cách rõ ràng và đầy đủ.
* **AWS SAM chỉ hỗ trợ xây dựng và triển khai hạ tầng cũng như ứng dụng Serverless**. Framework này không lưu trữ dữ liệu, không thực thi nghiệp vụ (business logic) và cũng không thay thế các dịch vụ Serverless như AWS Lambda hay Amazon API Gateway.

Đối với người mới học AWS, theo mình, hiểu được vai trò của AWS SAM sẽ giúp hiểu rõ hơn cách AWS tổ chức và triển khai một ứng dụng Serverless hoàn chỉnh thay vì chỉ tập trung vào từng dịch vụ riêng lẻ.

![Hình minh hoạ tóm gọn câu trả lời của bài đăng](img/2.jpg)

Posted link: <https://www.facebook.com/share/1DRhj9K5Lu/>