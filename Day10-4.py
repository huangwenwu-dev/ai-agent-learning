class Student:
    """学生类 - 完整的成绩管理功能"""
    
    def __init__(self, name: str, scores: list):
        """初始化学生"""
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
    
    def lowest(self) -> int:
        """获取最低分"""
        if len(self.scores) == 0:
            return 0
        return min(self.scores)
    
    def add_score(self, new_score: int) -> None:
        """添加新成绩（带基本校验）"""
        if 0 <= new_score <= 100:
            self.scores.append(new_score)
            print(f"  ✓ {self.name} 添加成绩 {new_score}")
        else:
            print(f"  ✗ {self.name} 添加失败：成绩 {new_score} 不在 0-100 范围")
    
    def get_summary(self) -> dict:
        """获取成绩摘要"""
        return {
            "name": self.name,
            "平均分": round(self.average(), 1),
            "最高分": self.highest(),
            "最低分": self.lowest(),
            "科目数": len(self.scores)
        }
    
    def __str__(self) -> str:
        """自定义字符串表示"""
        return f"{self.name}(平均:{self.average():.1f}, 最高:{self.highest()})"


def print_class_report(students: list):
    """打印班级成绩报告"""
    print("\n" + "=" * 60)
    print("班级成绩报告单")
    print("=" * 60)
    
    # 表头
    print(f"{'姓名':<8} {'平均分':<8} {'最高分':<8} {'最低分':<8} {'科目数':<6}")
    print("-" * 60)
    
    # 打印每个学生的信息
    for stu in students:
        info = stu.get_summary()
        print(f"{info['name']:<8} {info['平均分']:<8} {info['最高分']:<8} {info['最低分']:<8} {info['科目数']:<6}")
    
    print("-" * 60)
    
    # 计算班级整体统计
    all_scores = []
    for stu in students:
        all_scores.extend(stu.scores)
    
    if all_scores:
        class_avg = sum(all_scores) / len(all_scores)
        class_highest = max(all_scores)
        class_lowest = min(all_scores)
        
        print(f"\n班级整体统计:")
        print(f"  总平均分: {class_avg:.1f}")
        print(f"  全校最高分: {class_highest}")
        print(f"  全校最低分: {class_lowest}")
        print(f"  总成绩数: {len(all_scores)}")


# 测试代码
if __name__ == "__main__":
    print("=" * 60)
    print("Day3-4 综合练习：班级成绩管理系统")
    print("=" * 60)
    
    # 创建多个学生实例
    students = [
        Student("张三", [85, 90, 88, 92]),
        Student("李四", [70, 75, 68, 80, 72]),
        Student("王五", [95, 98, 92, 96, 94]),
        Student("赵六", [60, 65, 70]),
        Student("小美", [88, 92, 90, 89, 91, 93])
    ]
    
    # 显示初始成绩单
    print_class_report(students)
    
    # 演示动态添加成绩
    print("\n" + "=" * 60)
    print("动态添加新成绩")
    print("=" * 60)
    
    students[0].add_score(95)   # 张三加 95 分
    students[1].add_score(85)   # 李四加 85 分
    students[2].add_score(99)   # 王五加 99 分
    students[3].add_score(75)   # 赵六加 75 分
    students[4].add_score(94)   # 小美加 94 分
    
    # 测试边界值
    print("\n--- 测试成绩校验 ---")
    students[0].add_score(105)   # 非法：超过100
    students[0].add_score(-5)    # 非法：小于0
    
    # 显示更新后的成绩单
    print_class_report(students)
    
    # 使用 __str__ 方法简单打印
    print("\n" + "=" * 60)
    print("简单格式输出")
    print("=" * 60)
    for stu in students:
        print(f"  {stu}")   # 自动调用 __str__ 方法
    
    print("\n✅ Day3 所有任务完成！")