class Student:
    """学生类 - 支持添加新成绩"""
    
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
        """计算平均分"""
        if len(self.scores) == 0:
            return 0.0
        return sum(self.scores) / len(self.scores)
    
    def highest(self) -> int:
        """获取最高分"""
        if len(self.scores) == 0:
            return 0
        return max(self.scores)
    
    def add_score(self, new_score: int) -> None:
        """
        添加一个新成绩
        
        参数:
            new_score: 新成绩（整数）
        """
        self.scores.append(new_score)
        print(f"已添加成绩: {new_score}")
    
    def show_info(self) -> None:
        """显示学生完整信息"""
        print(f"姓名: {self.name}")
        print(f"成绩: {self.scores}")
        print(f"平均分: {self.average():.1f}")
        print(f"最高分: {self.highest()}")
        print("-" * 30)


# 测试代码
if __name__ == "__main__":
    print("=" * 40)
    print("Day3-3 测试：动态添加成绩")
    print("=" * 40)
    
    # 创建学生实例
    stu = Student("王芳", [85, 90, 78])
    
    print("=== 初始信息 ===")
    stu.show_info()
    
    print("\n=== 添加新成绩 ===")
    stu.add_score(95)
    stu.add_score(88)
    
    print("\n=== 更新后的信息 ===")
    stu.show_info()
    
    # 演示多次添加的效果
    print("\n=== 连续添加成绩演示 ===")
    stu2 = Student("赵雷", [70, 75])
    stu2.show_info()
    
    for score in [80, 85, 90, 95]:
        stu2.add_score(score)
    
    print("\n最终信息:")
    stu2.show_info()