import random
import tkinter as tk
from tkinter import ttk

def pension() -> str:
    rng = random.SystemRandom()
    group = rng.choice(range(1, 6))
    numbers = rng.choices(range(10), k=6)
    return f"{group}조  {''.join(map(str, numbers))}"

def lotto() -> str:
    numbers = sorted(random.SystemRandom().sample(range(1, 46), 6))
    return "  ".join(f"{n:2d}" for n in numbers)

def main() -> None:
    root = tk.Tk()
    root.title("복권 번호 생성기")
    root.geometry("320x180")

    result = tk.StringVar(value="버튼을 누르세요")

    ttk.Label(root, textvariable=result, font=("TkFixedFont", 18)).pack(pady=20)
    ttk.Button(root, text="로또", command=lambda: result.set(lotto())).pack(fill="x", padx=40, pady=4)
    ttk.Button(root, text="연금복권", command=lambda: result.set(pension())).pack(fill="x", padx=40, pady=4)

    root.mainloop()

if __name__ == '__main__':
    main()
