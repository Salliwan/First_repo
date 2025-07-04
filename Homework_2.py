from pathlib import Path

data = ['Alex Korp,3000', 'Nikita Borisenko,2000', 'Sitarama Raju,1000']
with open('Work/employee_data.txt', 'w', encoding='utf-8') as file:
    for line in data:
        file.write(f'{line}\n')

path = Path('Work/employee_data.txt')


def total_salary(path):
    try:
        salaries = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                salaries.append(int(salary))
            total = sum(salaries)
            average = int(total / len(salaries))
            print(
                f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

    except Exception as e:
        print(f'{e} with file')


total_salary(path)
