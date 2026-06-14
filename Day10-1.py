class Student:
    """学生类 - 包含姓名和成绩列表"""
    
    def __init__(self, name: str, scores: list):
        """
        初始化学生实例
        
        参数:
            name: 学生姓名
            scores: 成绩列表（例如 [85, 92, 78]）
        """
        self.name = name      # 实例属性：姓名
        self.scores = scores  # 实例属性：成绩列表


# 测试代码（只在直接运行时执行）
if __name__ == "__main__":
    print("=" * 40)
    print("Day3-1 测试：创建学生实例")
    print("=" * 40)
    
    # 创建第一个学生实例
    stu1 = Student("小明", [85, 92, 78])
    print(f"学生1: {stu1.name}")
    print(f"成绩: {stu1.scores}")
    print()
    
    # 创建第二个学生实例
    stu2 = Student("小红", [90, 88, 95, 87])
    print(f"学生2: {stu2.name}")
    print(f"成绩: {stu2.scores}")
    print()
    
    # 验证不同的实例有不同的属性值
    print("验证：不同实例的属性相互独立")
    print(f"stu1.name = {stu1.name}")
    print(f"stu2.name = {stu2.name}")
    print(f"stu1.scores = {stu1.scores}")
    print(f"stu2.scores = {stu2.scores}")