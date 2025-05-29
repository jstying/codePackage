class Employee:
    RANKS = ["实习生", "普通员工", "经理", "总监", "CEO"]
    MONEY = [0, 30000, 50000, 100000, 400000]
    WORKTIME = [7, 8, 9, 6, 4]

    """store employee information"""
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.positionLevel = 0
        self.salary = 0
        self.working_time = 7
        

    
    def __str__(self):
        """display employee information"""
        return (
            f"  姓名: {self.name}\n"
            f"  性别: {self.gender}\n"
            f"  年龄: {self.age}\n"
            f"  职位: {self.RANKS[self.positionLevel]}\n"
            f"  工资: {self.salary}元/月\n"
            f"  工作时间: {self.working_time}小时/天\n"
        )
    
    def promote(self):
        """promote employee"""
        if self.positionLevel >= len(self.RANKS) - 1:
            print("已经是最高级别了")
            return
        self.positionLevel += 1
        self.salary = self.MONEY[self.positionLevel]
        self.working_time = self.WORKTIME[self.positionLevel]
        print(f"恭喜你晋升为{self.RANKS[self.positionLevel]}! 现在工资为{self.salary}元/月, 工作时间为{self.working_time}小时/天!")


    def increaseSalary(self, bonus):
        """increase salary"""
        self.salary += bonus
        print(f"恭喜你加薪{bonus}元, 现在工资为{self.salary}元/月!")

    # 比较薪资
    def __lt__(self, other):
        return self.salary < other.salary
    
    # 比较年龄
    def __eq__(self, other):
        return self.age == other.age
    
def parse(filename):
    """从文件读取员工数据"""
    employees = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                    
                # 解析数据
                name, age_str, gender = line.split("|")
                age = int(age_str)
                    
                # 创建员工对象
                emp = Employee(name, gender, age)
                employees.append(emp)
            
        print(f"成功从文件加载 {len(employees)} 名员工")
        return employees
            
    except Exception as e:
        print(f"读取文件失败: {e}")
        return []
            
def interactive_manage(employees):
    """交互式管理员工"""
    if not employees:
        print("没有员工数据可供管理")
        return
        
    for i, emp in enumerate(employees, 1):
        print(f"\n=== 员工 {i}/{len(employees)} ===")
        print(emp)
        
        # 是否晋升
        while True:
            promote_choice = input(f"是否要晋升 {emp.name}? (y/n): ").strip().lower()
            if promote_choice == 'y':
                emp.promote()
                break
            elif promote_choice == 'n':
                print(f"{emp.name} 保持当前职位")
                break
            else:
                print("请输入 y 或 n")
        
        # 是否加薪
        while True:
            salary_choice = input(f"是否要给 {emp.name} 加薪? (y/n): ").strip().lower()
            if salary_choice == 'y':
                while True:
                    try:
                        bonus = int(input("请输入加薪金额: "))
                        if emp.increaseSalary(bonus):
                            break
                    except ValueError:
                        print("请输入有效的数字")
                break
            elif salary_choice == 'n':
                print(f"{emp.name} 保持当前薪资")
                break
            else:
                print("请输入 y 或 n")
        
        print("-" * 40)

    # 显示所有员工最终状态
    print("\n=== 所有员工最终状态 ===")
    for i, emp in enumerate(employees, 1):
        print(f"员工 {i}: {emp.name} ({emp.RANKS[emp.positionLevel]})")
        print(f"  工资: {emp.salary}元/月, 工作时间: {emp.working_time}小时/天")

if __name__ == "__main__":
   listEMP = parse("employees.txt")
   interactive_manage(listEMP)

