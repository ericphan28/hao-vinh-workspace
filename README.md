# Hệ Thống Quản Lý Projects - Khóa Học Lập Trình

## Tổng Quan
Workspace này được thiết kế để quản lý projects của 2 sinh viên trong khóa học lập trình.

## Cấu Trúc Thư Mục

```
haovinh/
├── student-projects/          # Projects của từng sinh viên
│   ├── student1/             # Thư mục projects của sinh viên 1
│   └── student2/             # Thư mục projects của sinh viên 2
├── shared-resources/         # Tài nguyên dùng chung
├── templates/               # Templates cho projects mới
├── documentation/           # Tài liệu hướng dẫn
├── evaluation/             # Đánh giá và chấm điểm
└── .github/               # Cấu hình GitHub và Copilot
```

## Hướng Dẫn Sử Dụng

### Cho Giảng Viên:
1. **Tạo Project Mới**: Sử dụng templates trong thư mục `templates/`
2. **Theo Dõi Tiến Độ**: Kiểm tra commits và pull requests
3. **Đánh Giá**: Sử dụng rubrics trong `evaluation/`

### Cho Sinh Viên:
1. **Bắt Đầu Project**: Copy template từ `templates/`
2. **Phát Triển**: Code trong thư mục cá nhân
3. **Chia Sẻ**: Sử dụng `shared-resources/` cho code dùng chung

## Workflow Git
- `main`: Code ổn định, đã được review
- `development`: Integration và testing
- `student1-*`: Branches của sinh viên 1
- `student2-*`: Branches của sinh viên 2

## Tools & Extensions Khuyến Nghị
- Git Graph
- Live Share
- Code Spell Checker
- Prettier
- GitLens

## Liên Hệ
- Giảng viên: [Tên của bạn]
- Email: [Email của bạn]
