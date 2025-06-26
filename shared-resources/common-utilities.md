# Shared Resources - Tài Nguyên Dùng Chung

## Thư Viện Utilities

### 1. Input Validation
```python
def validate_positive_integer(value):
    """Kiểm tra số nguyên dương"""
    try:
        num = int(value)
        return num > 0
    except ValueError:
        return False

def validate_email(email):
    """Kiểm tra email hợp lệ"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

### 2. File Operations
```python
import json
import csv

def read_json_file(filepath):
    """Đọc file JSON"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {filepath} không tồn tại")
        return None

def write_json_file(data, filepath):
    """Ghi file JSON"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def read_csv_file(filepath):
    """Đọc file CSV"""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data
```

### 3. Data Processing
```python
def calculate_statistics(numbers):
    """Tính toán thống kê cơ bản"""
    if not numbers:
        return None
    
    return {
        'count': len(numbers),
        'sum': sum(numbers),
        'average': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }

def sort_dict_by_value(data, reverse=False):
    """Sắp xếp dictionary theo value"""
    return dict(sorted(data.items(), key=lambda x: x[1], reverse=reverse))
```

## Constants
```python
# Thông tin chung
SCHOOL_NAME = "Trường Đại Học ABC"
COURSE_NAME = "Lập Trình Cơ Bản"

# Cấu hình
MAX_STUDENTS = 50
DEFAULT_ENCODING = 'utf-8'
DATE_FORMAT = '%Y-%m-%d'

# Messages
SUCCESS_MSG = "Thành công!"
ERROR_MSG = "Có lỗi xảy ra!"
```

## Code Snippets Library

### 1. Menu System
```python
def display_menu(options):
    """Hiển thị menu lựa chọn"""
    print("\n" + "="*40)
    print("MENU CHÍNH")
    print("="*40)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    print("0. Thoát")
    print("="*40)

def get_user_choice(max_option):
    """Lấy lựa chọn từ user"""
    while True:
        try:
            choice = int(input("Nhập lựa chọn của bạn: "))
            if 0 <= choice <= max_option:
                return choice
            else:
                print(f"Vui lòng nhập số từ 0 đến {max_option}")
        except ValueError:
            print("Vui lòng nhập một số nguyên!")
```

### 2. Progress Bar
```python
def show_progress(current, total, prefix="", suffix="", length=50):
    """Hiển thị thanh tiến trình"""
    percent = ("{0:.1f}").format(100 * (current / float(total)))
    filled_length = int(length * current // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    if current == total:
        print()
```

### 3. Table Display
```python
def display_table(data, headers):
    """Hiển thị dữ liệu dạng bảng"""
    if not data:
        print("Không có dữ liệu để hiển thị")
        return
    
    # Tính độ rộng cột
    col_widths = []
    for header in headers:
        max_width = len(header)
        for row in data:
            if header in row:
                max_width = max(max_width, len(str(row[header])))
        col_widths.append(max_width + 2)
    
    # In header
    header_row = "|".join(header.center(width) for header, width in zip(headers, col_widths))
    print(header_row)
    print("-" * len(header_row))
    
    # In data
    for row in data:
        data_row = "|".join(str(row.get(header, "")).center(width) for header, width in zip(headers, col_widths))
        print(data_row)
```

## Best Practices Examples

### Error Handling Pattern
```python
def safe_operation(func, *args, **kwargs):
    """Wrapper an toàn cho operations"""
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(f"Lỗi: {e}")
        return None

# Sử dụng
result = safe_operation(int, user_input)
if result is not None:
    print(f"Kết quả: {result}")
```

### Logging Pattern
```python
import logging
from datetime import datetime

def setup_logger(name, log_file='app.log'):
    """Thiết lập logger"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    handler = logging.FileHandler(log_file, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

# Sử dụng
logger = setup_logger('student_app')
logger.info('Ứng dụng bắt đầu')
```
