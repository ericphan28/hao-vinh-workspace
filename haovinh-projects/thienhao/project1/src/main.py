"""
Project 1 - Thiên Hào
Author: Thiên Hào
Date: 27/06/2025
Description: Bài tập cơ bản về Python - Tính toán và xử lý dữ liệu
"""

def calculate_sum(a: int, b: int) -> int:
    """
    Tính tổng của hai số
    
    Args:
        a (int): Số thứ nhất
        b (int): Số thứ hai
        
    Returns:
        int: Tổng của a và b
    """
    return a + b


def calculate_average(numbers: list) -> float:
    """
    Tính trung bình của một danh sách số
    
    Args:
        numbers (list): Danh sách các số
        
    Returns:
        float: Giá trị trung bình
    """
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def find_max_min(numbers: list) -> tuple:
    """
    Tìm giá trị lớn nhất và nhỏ nhất trong danh sách
    
    Args:
        numbers (list): Danh sách các số
        
    Returns:
        tuple: (max_value, min_value)
    """
    if not numbers:
        return None, None
    return max(numbers), min(numbers)


def main():
    """
    Hàm chính của chương trình
    """
    print("=== Project 1 - Thiên Hào ===")
    print("Bài tập: Tính toán cơ bản với Python")
    print("-" * 40)
    
    # Bài tập 1: Tính tổng hai số
    print("1. Tính tổng hai số:")
    num1 = 15
    num2 = 25
    total = calculate_sum(num1, num2)
    print(f"   Tổng của {num1} và {num2} là: {total}")
    
    # Bài tập 2: Tính trung bình
    print("\n2. Tính trung bình:")
    scores = [85, 92, 78, 90, 88]
    avg = calculate_average(scores)
    print(f"   Điểm số: {scores}")
    print(f"   Điểm trung bình: {avg:.2f}")
    
    # Bài tập 3: Tìm max/min
    print("\n3. Tìm giá trị lớn nhất và nhỏ nhất:")
    numbers = [45, 23, 89, 12, 67, 34]
    max_val, min_val = find_max_min(numbers)
    print(f"   Danh sách: {numbers}")
    print(f"   Giá trị lớn nhất: {max_val}")
    print(f"   Giá trị nhỏ nhất: {min_val}")
    
    # TODO: Thêm các bài tập khác
    print("\n4. Bài tập mở rộng:")
    print("   - Tính giai thừa của một số")
    print("   - Kiểm tra số nguyên tố")
    print("   - Sắp xếp danh sách")


if __name__ == "__main__":
    main()
