class Employee:
    def __init__(self, name, position, salary):
        """Ініціалізуємо співробітника з ім'ям, посадою та заробітною платою."""
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        """Повертає строкове представлення співробітника."""
        return f"{self.name} - {self.position}, Зарплата: {self.salary} грн"

class Department:
    def __init__(self, department_name):
        """Ініціалізуємо відділ з іменем та порожнім списком співробітників."""
        self.department_name = department_name
        self.employees = []

    def add_employee(self, employee):
        """Додаємо співробітника до відділу."""
        self.employees.append(employee)

    def remove_employee(self, employee):
        """Видаляємо співробітника з відділу."""
        if employee in self.employees:
            self.employees.remove(employee)
        else:
            print(f"Співробітник {employee.name} не знайдений у відділі.")

    def total_salary(self):
        """Підраховуємо загальну заробітну плату співробітників відділу."""
        total = sum(employee.salary for employee in self.employees)
        return total

    def show_employees(self):
        """Виводимо список співробітників відділу."""
        if not self.employees:
            print("Відділ порожній.")
        else:
            print(f"Список співробітників відділу {self.department_name}:")
            for employee in self.employees:
                print(employee)

employee1 = Employee("Іван Петров", "Менеджер", 25000)
employee2 = Employee("Марія Іванова", "Бухгалтер", 22000)
employee3 = Employee("Олексій Коваленко", "Програміст", 35000)
it_department = Department("IT Відділ")
it_department.add_employee(employee1)
it_department.add_employee(employee2)
it_department.add_employee(employee3)
it_department.show_employees()
print(f"Загальна заробітна плата відділу: {it_department.total_salary()} грн")
it_department.remove_employee(employee2)
it_department.show_employees()
print(f"Загальна заробітна плата після видалення: {it_department.total_salary()} грн")