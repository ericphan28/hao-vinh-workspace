# Coding Standards - Khóa Học Lập Trình

## 1. Quy Tắc Chung

### Naming Conventions
- **Variables**: `snake_case` (Python), `camelCase` (JavaScript)
- **Functions**: `snake_case` (Python), `camelCase` (JavaScript)
- **Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE`

### Ví Dụ
```python
# Python
student_name = "Nguyen Van A"
MAX_SCORE = 100

def calculate_average(scores):
    return sum(scores) / len(scores)

class StudentManager:
    pass
```

## 2. Code Structure

### Function Design
- Mỗi function chỉ làm 1 việc
- Tên function mô tả rõ chức năng
- Parameter ít hơn 5
- Return type rõ ràng

```python
def validate_email(email: str) -> bool:
    """
    Kiểm tra email có hợp lệ không
    
    Args:
        email (str): Email cần kiểm tra
        
    Returns:
        bool: True nếu email hợp lệ
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
```

### Class Design
- Single Responsibility Principle
- Encapsulation đúng cách
- Clear interface

## 3. Documentation

### Comments
```python
# TODO: Implement error handling
# FIXME: This function has a bug with negative numbers
# NOTE: This is a temporary solution

def complex_calculation(data):
    # Bước 1: Validate input
    if not data:
        return None
    
    # Bước 2: Process data
    result = []
    for item in data:
        # Logic phức tạp cần giải thích
        processed = item * 2 + 1
        result.append(processed)
    
    return result
```

### Docstrings
```python
def process_student_data(students: list, subject: str) -> dict:
    """
    Xử lý dữ liệu điểm số của sinh viên
    
    Args:
        students (list): Danh sách sinh viên
        subject (str): Môn học
        
    Returns:
        dict: Thống kê điểm số
        
    Raises:
        ValueError: Khi subject không hợp lệ
        
    Example:
        >>> students = [{"name": "A", "math": 8}, {"name": "B", "math": 9}]
        >>> process_student_data(students, "math")
        {"average": 8.5, "max": 9, "min": 8}
    """
```

## 4. Error Handling

### Try-Catch Proper
```python
def safe_divide(a: float, b: float) -> float:
    """
    Chia an toàn với error handling
    """
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    except TypeError:
        raise TypeError("Both arguments must be numbers")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return 0.0
```

### Input Validation
```python
def create_student(name: str, age: int, email: str) -> dict:
    """
    Tạo object sinh viên với validation
    """
    # Validate inputs
    if not name or not isinstance(name, str):
        raise ValueError("Name must be a non-empty string")
    
    if not isinstance(age, int) or age < 0 or age > 100:
        raise ValueError("Age must be between 0 and 100")
    
    if not validate_email(email):
        raise ValueError("Invalid email format")
    
    return {
        "name": name.strip().title(),
        "age": age,
        "email": email.lower()
    }
```

## 5. Testing

### Unit Test Structure
```python
import unittest

class TestStudentManager(unittest.TestCase):
    
    def setUp(self):
        """Setup trước mỗi test"""
        self.manager = StudentManager()
    
    def test_add_student_success(self):
        """Test thêm sinh viên thành công"""
        student = {"name": "Test", "age": 20}
        result = self.manager.add_student(student)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.students), 1)
    
    def test_add_student_invalid_age(self):
        """Test thêm sinh viên với tuổi không hợp lệ"""
        student = {"name": "Test", "age": -1}
        with self.assertRaises(ValueError):
            self.manager.add_student(student)
```

## 6. Performance Tips

### Efficient Code
```python
# ❌ Không hiệu quả
result = []
for i in range(1000):
    if i % 2 == 0:
        result.append(i * 2)

# ✅ Hiệu quả hơn
result = [i * 2 for i in range(1000) if i % 2 == 0]

# ✅ Hoặc dùng generator cho data lớn
result = (i * 2 for i in range(1000) if i % 2 == 0)
```

## 7. Code Review Checklist

### Before Submitting
- [ ] Code chạy được không lỗi
- [ ] All tests pass
- [ ] Có comments đầy đủ
- [ ] Tuân thủ naming conventions
- [ ] No hardcoded values
- [ ] Error handling đầy đủ
- [ ] Performance acceptable

### Review Criteria
- **Readability**: Code dễ đọc và hiểu
- **Maintainability**: Dễ sửa đổi và mở rộng
- **Reliability**: Ít bugs, handle edge cases
- **Efficiency**: Performance tốt
- **Security**: Không có security issues
