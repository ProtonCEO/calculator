import os

HISTORY_FILE = "history.txt"

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_to_history(entry):
    with open(HISTORY_FILE, "a") as f:
        f.write(entry + "\n")

def show_history():
    history = load_history()
    if not history:
        print("📜 No history yet.")
    else:
        print("\n📜 Calculation History:")
        for h in history:
            print(h)
    print()

while True:
    print("🧮 Terminal Calculator")
    print("[1] New calculation")
    print("[2] View history")
    print("[3] Quit")
    choice = input("Choose an option: ").strip()

    if choice == "1":
        expr = input("Enter expression: ").strip()
        try:
            result = eval(expr, {"__builtins__": {}})
            print(f"✅ Result: {result}\n")
            save_to_history(f"{expr} = {result}")
        except:
            print("❌ Invalid expression.\n")
    elif choice == "2":
        show_history()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("❌ Invalid choice. Pick 1–3.\n")
 
