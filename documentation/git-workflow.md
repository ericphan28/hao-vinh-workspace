# Hướng Dẫn Workflow Git cho Sinh Viên

## 1. Thiết Lập Ban Đầu

### Clone Repository
```bash
git clone [URL_REPOSITORY]
cd haovinh
```

### Tạo Branch Cá Nhân
```bash
# Thiên Hào
git checkout -b thienhao-main

# Thiên Vinh  
git checkout -b thienvinh-main
```

## 2. Workflow Hàng Ngày

### Bắt Đầu Project Mới
1. Copy template phù hợp:
```bash
cp -r templates/python-basic haovinh-projects/thienhao/project-name
```

2. Tạo branch cho project:
```bash
git checkout -b thienhao-project-name
```

### Phát Triển Code
1. **Commit thường xuyên** (mỗi feature nhỏ):
```bash
git add .
git commit -m "feat: add basic calculator functions"
```

2. **Push lên remote**:
```bash
git push origin thienhao-project-name
```

### Code Review Process
1. Tạo Pull Request trên GitHub
2. Assign giảng viên làm reviewer
3. Sửa feedback nếu có
4. Merge sau khi được approve

## 3. Quy Tắc Commit Messages

### Format Chuẩn
```
type(scope): description

[optional body]
```

### Các Type Phổ Biến
- `feat`: Tính năng mới
- `fix`: Sửa lỗi
- `docs`: Cập nhật tài liệu
- `style`: Format code
- `refactor`: Refactor code
- `test`: Thêm tests
- `chore`: Maintenance

### Ví Dụ
```bash
git commit -m "feat(calculator): add multiplication function"
git commit -m "fix(input): handle empty string validation"
git commit -m "docs(readme): update installation instructions"
```

## 4. Best Practices

### DO
- ✅ Commit thường xuyên với messages rõ ràng
- ✅ Test code trước khi commit
- ✅ Review code của nhau
- ✅ Sync với main branch thường xuyên

### DON'T
- ❌ Commit code không chạy được
- ❌ Push directly lên main branch
- ❌ Commit files không liên quan
- ❌ Ignore merge conflicts

## 5. Troubleshooting

### Conflict Resolution
```bash
# Khi có conflicts
git pull origin main
# Sửa conflicts trong editor
git add .
git commit -m "resolve: merge conflicts with main"
```

### Undo Changes
```bash
# Undo commit cuối
git reset --soft HEAD~1

# Undo tất cả changes chưa commit
git restore .
```

## 6. Collaboration

### Code Review Checklist
- [ ] Code chạy được không lỗi
- [ ] Có comments và documentation
- [ ] Tuân thủ coding standards
- [ ] Tests pass
- [ ] README được cập nhật
