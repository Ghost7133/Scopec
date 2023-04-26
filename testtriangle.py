import tkinter as tk
root = tk.Tk()
root.geometry("400x250")
root.title("Треугольник")

def triangle_type():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())

    if type(a) == float and type(b) == float and type(c) == float:
        if (a>0 and b>0 and c>0) and (a !=0 and b != 0 and c != 0):
            if a+b>c and a+c>b and b+a>c and b+c>a and c+a>b and c+b>a:
                if a == b == c:
                    result_label.config(text = "Треугольник является равносторонним")
                elif a == b or b == c or a == c:
                    result_label.config(text = "Треугольник является равнобедренным")
                else:
                    result_label.config(text = "Треугольник является разносторонним")
            else:
                result_label.config(text = "Сумма двух из чисел больше третьего")
        else:
            result_label.config(text = "Одно из чисел <= 0")
    else:
        result_label.config(text = "Вы ввели не числовое значение")

title_label = tk.Label(root, text="Введите 3 стороны треугольника")
title_label.grid(row=0, column=0, columnspan=2)
a_label = tk.Label(root, text="A:")
a_label.grid(row=1, column=0)
a_entry = tk.Entry(root)
a_entry.grid(row=1, column=1)
b_label = tk.Label(root, text="B:")
b_label.grid(row=2, column=0)
b_entry = tk.Entry(root)
b_entry.grid(row=2, column=1)
c_label = tk.Label(root, text="C:")
c_label.grid(row=3, column=0)
c_entry = tk.Entry(root)
c_entry.grid(row=3, column=1)
check_button = tk.Button(root, text="Проверить", command=triangle_type)
check_button.grid(row=4, column=0, columnspan=2)
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

root.mainloop()