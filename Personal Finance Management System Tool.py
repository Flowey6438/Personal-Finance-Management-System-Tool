import json
from datetime import datetime

DATA_FILE = "finances.json"

def load_finances():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"income": [], "expense": []}

def save_finances(finances):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(finances, file, indent=4)

def add_income(finances, amount, description):
    income_entry = {
        "amount": amount,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    finances["income"].append(income_entry)
    print(f"收入记录已添加：{description}，金额：{amount}元")

def add_expense(finances, amount, description):
    expense_entry = {
        "amount": amount,
        "description": description,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    finances["expense"].append(expense_entry)
    print(f"支出记录已添加：{description}，金额：{amount}元")

def view_finances(finances):
    print("\n所有财务记录：")
    print("收入记录：")
    for entry in finances["income"]:
        print(f"日期：{entry['date']} | 描述：{entry['description']} | 金额：{entry['amount']}元")
    
    print("\n支出记录：")
    for entry in finances["expense"]:
        print(f"日期：{entry['date']} | 描述：{entry['description']} | 金额：{entry['amount']}元")

def view_report(finances):
    total_income = sum(entry['amount'] for entry in finances["income"])
    total_expense = sum(entry['amount'] for entry in finances["expense"])
    net_balance = total_income - total_expense

    print("\n财务报表：")
    print(f"总收入：{total_income}元")
    print(f"总支出：{total_expense}元")
    print(f"净收入：{net_balance}元")

if __name__ == "__main__":
    finances = load_finances()
    print("欢迎使用个人财务管理系统！")

    while True:
        print("\n请选择一个操作：")
        print("1. 添加收入")
        print("2. 添加支出")
        print("3. 查看所有财务记录")
        print("4. 查看财务报表")
        print("5. 退出")

        choice = input("请输入选项（1/2/3/4/5）：")

        if choice == "1":
            amount = float(input("请输入收入金额："))
            description = input("请输入收入描述：")
            add_income(finances, amount, description)
            save_finances(finances)
        elif choice == "2":
            amount = float(input("请输入支出金额："))
            description = input("请输入支出描述：")
            add_expense(finances, amount, description)
            save_finances(finances)
        elif choice == "3":
            view_finances(finances)
        elif choice == "4":
            view_report(finances)
        elif choice == "5":
            print("感谢使用个人财务管理系统，再见！")
            break
        else:
            print("无效选项，请重新选择。")
