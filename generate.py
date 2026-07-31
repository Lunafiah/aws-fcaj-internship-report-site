import os
data = [
    {
        "week": 1,
        "date_range": "1/6 - 7/6",
        "title_en": "Week 1: Onboarding & Topic Selection",
        "title_vi": "Tuần 1: Nhập môn & Chọn đề tài",
        "obj_en": "* Connect and get acquainted with FCAJ members.\n* Understand internship rules and finalize capstone project topic.",
        "obj_vi": "* Kết nối, làm quen với các thành viên FCAJ.\n* Nắm rõ nội quy thực tập và chốt đề tài dự án cuối khóa.",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Get acquainted with FCAJ members<br>- Read internship rules | 06/01/2026 | 06/01/2026 | |
| 3 | - Form project teams | 06/02/2026 | 06/02/2026 | |
| 4 | - Discuss potential capstone project topics | 06/03/2026 | 06/04/2026 | |
| 5 | - Research AWS Serverless architecture concepts | 06/05/2026 | 06/06/2026 | |
| 6 | - Finalize topic: BK-Sync Smart QR Attendance API | 06/07/2026 | 06/07/2026 | |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Làm quen với các thành viên FCAJ<br>- Đọc nội quy thực tập | 01/06/2026 | 01/06/2026 | |
| 3 | - Lập nhóm làm dự án | 02/06/2026 | 02/06/2026 | |
| 4 | - Thảo luận các đề tài tiềm năng | 03/06/2026 | 04/06/2026 | |
| 5 | - Nghiên cứu khái niệm kiến trúc AWS Serverless | 05/06/2026 | 06/06/2026 | |
| 6 | - Chốt đề tài: BK-Sync Smart QR Attendance API | 07/06/2026 | 07/06/2026 | |""",
        "achieve_en": "* Successfully onboarded and joined a project team.\n* Finalized the capstone project topic.",
        "achieve_vi": "* Hoàn tất thủ tục nhập môn và gia nhập nhóm dự án.\n* Chốt thành công đề tài dự án cuối khóa."
    },
    {
        "week": 2,
        "date_range": "8/6 - 14/6",
        "title_en": "Week 2: AWS Account Setup & Basics",
        "title_vi": "Tuần 2: Thiết lập AWS & Cơ bản",
        "obj_en": "* Set up AWS Free Tier account securely.\n* Learn basic AWS services (EC2, Lambda, IAM, Budget).",
        "obj_vi": "* Thiết lập tài khoản AWS Free Tier an toàn.\n* Tìm hiểu các dịch vụ cơ bản (EC2, Lambda, IAM, Budget).",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Create AWS Free Tier account & AWS Budgets | 06/08/2026 | 06/08/2026 | CloudJourney |
| 3 | - Complete $100 tasks: EC2, Lambda web app, RDS | 06/09/2026 | 06/10/2026 | CloudJourney |
| 4 | - Study IAM Access Control & Install AWS CLI | 06/11/2026 | 06/11/2026 | |
| 5 | - Install Kiro IDE & explore CloudFormation | 06/12/2026 | 06/12/2026 | |
| 6 | - Attend FCAJ Meetup event | 06/13/2026 | 06/14/2026 | |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tạo tài khoản AWS Free Tier & cấu hình Budgets | 08/06/2026 | 08/06/2026 | CloudJourney |
| 3 | - Làm task $100: EC2, Lambda web app, RDS | 09/06/2026 | 10/06/2026 | CloudJourney |
| 4 | - Tìm hiểu IAM Access Control & cài đặt AWS CLI | 11/06/2026 | 11/06/2026 | |
| 5 | - Cài Kiro IDE & tìm hiểu CloudFormation | 12/06/2026 | 12/06/2026 | |
| 6 | - Tham gia sự kiện FCAJ Meetup | 13/06/2026 | 14/06/2026 | |""",
        "achieve_en": "* Account secured with Budgets and IAM.\n* Hands-on experience with core AWS services.",
        "achieve_vi": "* Tài khoản được bảo mật với IAM và Budgets.\n* Có kinh nghiệm thực hành với các dịch vụ AWS cốt lõi."
    },
    {
        "week": 3,
        "date_range": "15/6 - 21/6",
        "title_en": "Week 3: CDK Workshop & Architecture",
        "title_vi": "Tuần 3: Workshop CDK & Kiến trúc",
        "obj_en": "* Understand Infrastructure as Code with AWS CDK.\n* Design the backend architecture.",
        "obj_vi": "* Hiểu về Infrastructure as Code với AWS CDK.\n* Thiết kế kiến trúc backend.",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Complete AWS CDK Basic workshop | 06/15/2026 | 06/16/2026 | CloudJourney |
| 3 | - Study architecture diagramming on draw.io | 06/17/2026 | 06/17/2026 | |
| 4 | - Start AWS CDK Advanced (Cross-stack references) | 06/18/2026 | 06/19/2026 | CloudJourney |
| 5 | - Setup Hugo report site locally | 06/20/2026 | 06/21/2026 | |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Hoàn thành workshop AWS CDK Basic | 15/06/2026 | 16/06/2026 | CloudJourney |
| 3 | - Học vẽ kiến trúc trên draw.io | 17/06/2026 | 17/06/2026 | |
| 4 | - Bắt đầu AWS CDK nâng cao | 18/06/2026 | 19/06/2026 | CloudJourney |
| 5 | - Thiết lập trang báo cáo Hugo ở local | 20/06/2026 | 21/06/2026 | |""",
        "achieve_en": "* Mastered AWS CDK basics and cross-stack logic.\n* Successfully mapped out the system architecture.",
        "achieve_vi": "* Nắm vững cơ bản AWS CDK và logic cross-stack.\n* Vẽ thành công kiến trúc hệ thống."
    },
    {
        "week": 4,
        "date_range": "22/6 - 28/6",
        "title_en": "Week 4: Networking & Report Site",
        "title_vi": "Tuần 4: Networking & Trang báo cáo",
        "obj_en": "* Understand VPC and network routing.\n* Deploy the internship report site.",
        "obj_vi": "* Hiểu về VPC và định tuyến mạng.\n* Triển khai trang báo cáo thực tập.",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Amazon VPC and Site-to-Site VPN workshop | 06/22/2026 | 06/24/2026 | CloudJourney |
| 3 | - EC2 Cost Optimization with Lambda workshop | 06/25/2026 | 06/26/2026 | CloudJourney |
| 4 | - Push report site to GitHub and setup Actions | 06/27/2026 | 06/28/2026 | |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Workshop Amazon VPC & Site-to-Site VPN | 22/06/2026 | 24/06/2026 | CloudJourney |
| 3 | - Workshop Tối ưu chi phí EC2 với Lambda | 25/06/2026 | 26/06/2026 | CloudJourney |
| 4 | - Đẩy trang báo cáo lên GitHub & setup Actions | 27/06/2026 | 28/06/2026 | |""",
        "achieve_en": "* Built foundational networking knowledge.\n* Report site is live on GitHub Pages.",
        "achieve_vi": "* Có kiến thức nền tảng về networking.\n* Trang báo cáo đã live trên GitHub Pages."
    },
    {
        "week": 5,
        "date_range": "29/6 - 5/7",
        "title_en": "Week 5: Serverless Backend Development",
        "title_vi": "Tuần 5: Phát triển Serverless Backend",
        "obj_en": "* Implement the core Serverless logic.\n* Design the DynamoDB schema.",
        "obj_vi": "* Triển khai logic Serverless cốt lõi.\n* Thiết kế schema cho DynamoDB.",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Study Lambda + API Gateway patterns | 06/29/2026 | 06/30/2026 | |
| 3 | - Backend dev with AWS SAM (BK-Sync) | 07/01/2026 | 07/02/2026 | |
| 4 | - Design DynamoDB tables for attendance | 07/03/2026 | 07/04/2026 | |
| 5 | - Explore Amazon Cognito fundamentals | 07/05/2026 | 07/05/2026 | |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Học pattern Lambda + API Gateway | 29/06/2026 | 30/06/2026 | |
| 3 | - Code backend với AWS SAM (BK-Sync) | 01/07/2026 | 02/07/2026 | |
| 4 | - Thiết kế table DynamoDB cho điểm danh | 03/07/2026 | 04/07/2026 | |
| 5 | - Tìm hiểu cơ bản về Amazon Cognito | 05/07/2026 | 05/07/2026 | |""",
        "achieve_en": "* Backend foundation built.\n* Database schema optimized for Serverless.",
        "achieve_vi": "* Nền tảng backend được thiết lập.\n* Schema DB được tối ưu cho Serverless."
    },
    {
        "week": 6,
        "date_range": "6/7 - 12/7",
        "title_en": "Week 6: API Integration & Auth",
        "title_vi": "Tuần 6: Tích hợp API & Xác thực",
        "obj_en": "* Secure APIs with authentication.\n* Manage secrets and configurations.",
        "obj_vi": "* Bảo mật API với xác thực.\n* Quản lý key và cấu hình.",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Integrate API Gateway with Lambda | 07/06/2026 | 07/07/2026 | |
| 3 | - Implement Cognito Auth (Admin, Student) | 07/08/2026 | 07/09/2026 | |
| 4 | - Setup AWS Secrets Manager for HMAC key | 07/10/2026 | 07/11/2026 | |
| 5 | - Resource tagging and cost tracking | 07/12/2026 | 07/12/2026 | CloudJourney |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tích hợp API Gateway với Lambda | 06/07/2026 | 07/07/2026 | |
| 3 | - Triển khai xác thực Cognito | 08/07/2026 | 09/07/2026 | |
| 4 | - Cấu hình AWS Secrets Manager lưu HMAC | 10/07/2026 | 11/07/2026 | |
| 5 | - Gắn thẻ tài nguyên & theo dõi chi phí | 12/07/2026 | 12/07/2026 | CloudJourney |""",
        "achieve_en": "* Auth flow working securely.\n* Secrets are encrypted and safely stored.",
        "achieve_vi": "* Luồng xác thực hoạt động an toàn.\n* Key được mã hóa và lưu trữ an toàn."
    },
    {
        "week": 7,
        "date_range": "13/7 - 19/7",
        "title_en": "Week 7: Backend Features",
        "title_vi": "Tuần 7: Tính năng Backend",
        "obj_en": "* Complete advanced backend functionalities.\n* Participate in code reviews.",
        "obj_vi": "* Hoàn thiện các tính năng backend nâng cao.\n* Tham gia code review.",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Implement pagination for listUsers API | 07/13/2026 | 07/14/2026 | |
| 3 | - Get student attendance history (UC-S04) | 07/15/2026 | 07/16/2026 | |
| 4 | - Auto-close expired sessions (FR-12) | 07/17/2026 | 07/18/2026 | |
| 5 | - Submit PRs and review teammates' code | 07/19/2026 | 07/19/2026 | |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Code pagination cho listUsers API | 13/07/2026 | 14/07/2026 | |
| 3 | - Code xem lịch sử điểm danh (UC-S04) | 15/07/2026 | 16/07/2026 | |
| 4 | - Code tự đóng session hết hạn (FR-12) | 17/07/2026 | 18/07/2026 | |
| 5 | - Tạo PR và review code của đồng đội | 19/07/2026 | 19/07/2026 | |""",
        "achieve_en": "* Core backend features completed.\n* Codebase improved through peer reviews.",
        "achieve_vi": "* Hoàn thành các tính năng backend cốt lõi.\n* Codebase được cải thiện qua peer review."
    },
    {
        "week": 8,
        "date_range": "20/7 - 26/7",
        "title_en": "Week 8: Testing & Monitoring",
        "title_vi": "Tuần 8: Kiểm thử & Giám sát",
        "obj_en": "* Automate testing pipelines.\n* Monitor system health.",
        "obj_vi": "* Tự động hóa pipeline kiểm thử.\n* Giám sát sức khỏe hệ thống.",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Build Integration Testing pipeline | 07/20/2026 | 07/22/2026 | |
| 3 | - Complete EC2 fundamentals lab | 07/23/2026 | 07/23/2026 | CloudJourney |
| 4 | - Setup CloudWatch alarms & dashboards | 07/24/2026 | 07/25/2026 | |
| 5 | - Configure SNS alerts | 07/26/2026 | 07/26/2026 | |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Xây dựng Integration Testing pipeline | 20/07/2026 | 22/07/2026 | |
| 3 | - Hoàn thành lab EC2 cơ bản | 23/07/2026 | 23/07/2026 | CloudJourney |
| 4 | - Cấu hình CloudWatch alarms & dashboards | 24/07/2026 | 25/07/2026 | |
| 5 | - Cấu hình SNS alerts | 26/07/2026 | 26/07/2026 | |""",
        "achieve_en": "* CI/CD automated tests running.\n* Monitoring and alerting active.",
        "achieve_vi": "* Chạy thành công test CI/CD tự động.\n* Giám sát và cảnh báo hoạt động tốt."
    },
    {
        "week": 9,
        "date_range": "27/7 - 31/7",
        "title_en": "Week 9: Project Finalization",
        "title_vi": "Tuần 9: Hoàn thiện dự án",
        "obj_en": "* Complete all testing and bug fixes.\n* Finish the internship report and demo.",
        "obj_vi": "* Hoàn tất kiểm thử và sửa lỗi.\n* Hoàn thành báo cáo thực tập và demo.",
        "table_en": """| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 2 | - Final testing and bug fixes | 07/27/2026 | 07/28/2026 | |
| 3 | - Complete internship report site content | 07/29/2026 | 07/29/2026 | |
| 4 | - Prepare presentation slides | 07/30/2026 | 07/30/2026 | |
| 5 | - Record demo video and wrap-up | 07/31/2026 | 07/31/2026 | |""",
        "table_vi": """| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Kiểm thử cuối cùng và sửa lỗi | 27/07/2026 | 28/07/2026 | |
| 3 | - Hoàn thiện nội dung trang báo cáo | 29/07/2026 | 29/07/2026 | |
| 4 | - Chuẩn bị slide thuyết trình | 30/07/2026 | 30/07/2026 | |
| 5 | - Quay video demo và tổng kết | 31/07/2026 | 31/07/2026 | |""",
        "achieve_en": "* Project fully functional.\n* Documentation and presentation ready.",
        "achieve_vi": "* Dự án hoạt động trơn tru.\n* Tài liệu và thuyết trình đã sẵn sàng."
    }
]
base_dir = r"c:\Users\Lunafiah\Desktop\Study\TTNT\aws-fcaj-internship-report-site\content\1-Worklog"
for w in data:
    folder_name = f"1.{w['week']}-Week{w['week']}"
    folder_path = os.path.join(base_dir, folder_name)
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
    en_content = f"""---
title: "{w['title_en']}"
date: 2026-07-30
weight: 1
chapter: false
pre: " <b> 1.{w['week']}. </b> "
---
### Week {w['week']} Objectives:
{w['obj_en']}
### Tasks to be carried out this week:
{w['table_en']}
### Week {w['week']} Achievements:
{w['achieve_en']}
"""
    vi_content = f"""---
title: "{w['title_vi']}"
date: 2026-07-30
weight: 1
chapter: false
pre: " <b> 1.{w['week']}. </b> "
---
### Mục tiêu tuần {w['week']}:
{w['obj_vi']}
### Các công việc cần triển khai trong tuần này:
{w['table_vi']}
### Kết quả đạt được tuần {w['week']}:
{w['achieve_vi']}
"""
    with open(os.path.join(folder_path, "_index.md"), "w", encoding="utf-8") as f:
        f.write(en_content)
        
    with open(os.path.join(folder_path, "_index.vi.md"), "w", encoding="utf-8") as f:
        f.write(vi_content)
        
print("Successfully generated all worklog files.")
