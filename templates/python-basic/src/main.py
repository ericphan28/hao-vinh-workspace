"""
Main entry point cho project
Author: [Tên sinh viên]
Date: [Ngày tạo]
"""

def main():
    """
    Hàm chính của chương trình
    """
    print("Hello, World!")
    print("Đây là project đầu tiên của tôi!")
    
    # TODO: Thêm logic chính của project ở đây
    

def example_function(name: str) -> str:
    """
    Ví dụ về một function có parameter và return value
    
    Args:
        name (str): Tên để chào
        
    Returns:
        str: Câu chào hoàn chỉnh
    """
    return f"Xin chào, {name}!"


if __name__ == "__main__":
    # Chạy chương trình chính
    main()
    
    # Ví dụ sử dụng function
    greeting = example_function("Sinh viên")
    print(greeting)
