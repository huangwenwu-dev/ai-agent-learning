class Student:
    # ... 其他方法 ...
    @staticmethod
    def is_valid_score(score):
        return isinstance(score, int) and 0 <= score <= 100

    @classmethod
    def from_string(cls, data_str):
        name, scores_str = data_str.split(":")
        scores = list(map(int, scores_str.split(",")))
        return cls(name, scores)

# 测试
if __name__ == "__main__":
    print(Student.is_valid_score(85))   # True
    print(Student.is_valid_score(105))  # False

    s = Student.from_string("王芳:88,92,79")
    print(s.name, s.scores)