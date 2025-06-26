"""
Project 1 - Thiên Vinh
Author: Thiên Vinh
Date: 27/06/2025
Description: Bài tập cơ bản về Python - Geometry và String processing
"""

def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Tính diện tích hình chữ nhật
    
    Args:
        width (float): Chiều rộng
        height (float): Chiều cao
        
    Returns:
        float: Diện tích
    """
    return width * height


def calculate_circle_area(radius: float) -> float:
    """
    Tính diện tích hình tròn
    
    Args:
        radius (float): Bán kính
        
    Returns:
        float: Diện tích hình tròn
    """
    import math
    return math.pi * radius ** 2


def count_words(text: str) -> dict:
    """
    Đếm số từ trong văn bản
    
    Args:
        text (str): Văn bản cần đếm
        
    Returns:
        dict: Dictionary chứa thống kê
    """
    words = text.split()
    return {
        'total_words': len(words),
        'total_characters': len(text),
        'total_characters_no_spaces': len(text.replace(' ', ''))
    }


def reverse_string(text: str) -> str:
    """
    Đảo ngược chuỗi
    
    Args:
        text (str): Chuỗi cần đảo ngược
        
    Returns:
        str: Chuỗi đã đảo ngược
    """
    return text[::-1]


def main():
    """
    Hàm chính của chương trình
    """
    print("=== Project 1 - Thiên Vinh ===")
    print("Bài tập: Geometry và String Processing")
    print("-" * 40)
    
    # Bài tập 1: Tính diện tích hình chữ nhật
    print("1. Tính diện tích hình chữ nhật:")
    width = 8.5
    height = 12.0
    rect_area = calculate_rectangle_area(width, height)
    print(f"   Kích thước: {width} x {height}")
    print(f"   Diện tích: {rect_area} đơn vị vuông")
    
    # Bài tập 2: Tính diện tích hình tròn
    print("\n2. Tính diện tích hình tròn:")
    radius = 5.5
    circle_area = calculate_circle_area(radius)
    print(f"   Bán kính: {radius}")
    print(f"   Diện tích: {circle_area:.2f} đơn vị vuông")
    
    # Bài tập 3: Xử lý chuỗi
    print("\n3. Phân tích văn bản:")
    sample_text = "Python là ngôn ngữ lập trình mạnh mẽ và dễ học"
    stats = count_words(sample_text)
    print(f"   Văn bản: '{sample_text}'")
    print(f"   Số từ: {stats['total_words']}")
    print(f"   Số ký tự: {stats['total_characters']}")
    print(f"   Số ký tự (không khoảng trắng): {stats['total_characters_no_spaces']}")
    
    # Bài tập 4: Đảo ngược chuỗi
    print("\n4. Đảo ngược chuỗi:")
    original = "Hello Python"
    reversed_text = reverse_string(original)
    print(f"   Chuỗi gốc: '{original}'")
    print(f"   Chuỗi đảo ngược: '{reversed_text}'")
    
    # TODO: Thêm các bài tập khác
    print("\n5. Bài tập mở rộng:")
    print("   - Tính chu vi các hình học")
    print("   - Kiểm tra palindrome")
    print("   - Đếm tần suất ký tự")


if __name__ == "__main__":
    main()
