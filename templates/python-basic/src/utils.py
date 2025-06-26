"""
Utility functions dùng chung cho project
"""

def validate_input(value, input_type=str):
    """
    Kiểm tra tính hợp lệ của input
    
    Args:
        value: Giá trị cần kiểm tra
        input_type: Kiểu dữ liệu mong muốn
        
    Returns:
        bool: True nếu hợp lệ
    """
    try:
        input_type(value)
        return True
    except (ValueError, TypeError):
        return False


def format_output(data):
    """
    Format dữ liệu để hiển thị đẹp
    
    Args:
        data: Dữ liệu cần format
        
    Returns:
        str: Chuỗi đã được format
    """
    if isinstance(data, list):
        return "\n".join(str(item) for item in data)
    return str(data)


def log_message(message, level="INFO"):
    """
    Ghi log message với timestamp
    
    Args:
        message (str): Nội dung log
        level (str): Mức độ log (INFO, WARNING, ERROR)
    """
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {level}: {message}")
