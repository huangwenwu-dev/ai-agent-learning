class Student:
    """学生类 - 包含姓名、成绩及相关计算方法"""
    
    def __init__(self, name: str, scores: list):
        """
        初始化学生实例
        
        参数:
            name: 学生姓名
            scores: 成绩列表
        """
        self.name = name
        self.scores = scores
    
    def average(self) -> float:
        """
        计算平均分
        
        返回:
            平均分（浮点数）
        """
        if len(self.scores) == 0:
            return 0.0
        return sum(self.scores) / len(self.scores)
    
    def highest(self) -> int:
        """
        获取最高分
        
        返回:
            最高分（整数）
        """
        if len(self.scores) == 0:
            return 0
        return max(self.scores)


# 测试代码
if __name__ == "__main__":
    print("=" * 40)
    print("Day3-2 测试：平均分和最高分计算")
    print("=" * 40)
    
    # 创建学生实例
    stu = Student("李华", [88, 76, 95])
    
    print(f"学生姓名: {stu.name}")
    print(f"成绩列表: {stu.scores}")
    print(f"平均分: {stu.average():.1f}")
    print(f"最高分: {stu.highest()}")
    print()
    
    # 测试更多场景
    print("--- 更多测试 ---")
    stu2 = Student("张伟", [60, 75, 80, 90, 100])
    print(f"{stu2.name} 的平均分: {stu2.average():.1f}")
    print(f"{stu2.name} 的最高分: {stu2.highest()}")
    print()
    
    # 测试空成绩列表
    stu3 = Student("测试学生", [])
    print(f"空成绩列表的平均分: {stu3.average()}")
    print(f"空成绩列表的最高分: {stu3.highest()}")