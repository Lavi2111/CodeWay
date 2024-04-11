'''
   A simple GUI calculator using Python's Tkinter library.
   By: Rajat Gupta
       https://www.linkedin.com/in/rajat-gupta-4aab0324b/
       https://github.com/Lavi2111/CodeWay/tree/main/Task2_Calculator
'''
import tkinter as tk

# global var
calculation = ""

def add_to_calculation(symbol):
    global calculation

    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation)) #dont get used to it!!

        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

# root
root = tk.Tk()
root.title('Calculator by Rajat Gupta')
root.geometry("293x275")
root.minsize(293,275)
root.maxsize(293,275)
root.config(bg="grey")

# result
text_result = tk.Text(root,height=2,width=16,font=("Arial",24),fg="grey",bg="black")
text_result.grid(columnspan=5)

# buttons
btn_1 = tk.Button(root,text=f"{1}",command=lambda: add_to_calculation(1),width=5,font=("Arial",14))
btn_1.grid(row=2,column=1)
btn_2 = tk.Button(root,text=f"{2}",command=lambda: add_to_calculation(2),width=5,font=("Arial",14))
btn_2.grid(row=2,column=2)
btn_3 = tk.Button(root,text=f"{3}",command=lambda: add_to_calculation(3),width=5,font=("Arial",14))
btn_3.grid(row=2,column=3)
btn_4 = tk.Button(root,text=f"{4}",command=lambda: add_to_calculation(4),width=5,font=("Arial",14))
btn_4.grid(row=3,column=1)
btn_5 = tk.Button(root,text=f"{5}",command=lambda: add_to_calculation(5),width=5,font=("Arial",14))
btn_5.grid(row=3,column=2)
btn_6 = tk.Button(root,text=f"{6}",command=lambda: add_to_calculation(6),width=5,font=("Arial",14))
btn_6.grid(row=3,column=3)
btn_7 = tk.Button(root,text=f"{7}",command=lambda: add_to_calculation(7),width=5,font=("Arial",14))
btn_7.grid(row=4,column=1)
btn_8 = tk.Button(root,text=f"{8}",command=lambda: add_to_calculation(8),width=5,font=("Arial",14))
btn_8.grid(row=4,column=2)
btn_9 = tk.Button(root,text=f"{9}",command=lambda: add_to_calculation(9),width=5,font=("Arial",14))
btn_9.grid(row=4,column=3)
btn_0 = tk.Button(root,text=f"{0}",command=lambda: add_to_calculation(0),width=5,font=("Arial",14))
btn_0.grid(row=5,column=2)

btn_plus = tk.Button(root,text="+",command=lambda: add_to_calculation("+"),width=5,font=("Arial",14))
btn_plus.grid(row=2,column=4)
btn_minus = tk.Button(root,text="-",command=lambda: add_to_calculation("-"),width=5,font=("Arial",14))
btn_minus.grid(row=3,column=4)
btn_div = tk.Button(root,text="/",command=lambda: add_to_calculation("/"),width=5,font=("Arial",14))
btn_div.grid(row=4,column=4)
btn_mul = tk.Button(root,text="*",command=lambda: add_to_calculation("*"),width=5,font=("Arial",14))
btn_mul.grid(row=5,column=4)
btn_openp = tk.Button(root,text="(",command=lambda: add_to_calculation("("),width=5,font=("Arial",14))
btn_openp.grid(row=5,column=1)
btn_closep = tk.Button(root,text=")",command=lambda: add_to_calculation(")"),width=5,font=("Arial",14))
btn_closep.grid(row=5,column=3)

btn_clear = tk.Button(root,text="C",command= clear_field,width=12,font=("Arial",14),highlightcolor="red", bg="red", fg="white")
btn_clear.grid(row=6,column=1,columnspan=2)
btn_equal = tk.Button(root,text="=",command=evaluate_calculation,width=12,font=("Arial",14),highlightcolor="green", bg="green", fg="white")
btn_equal.grid(row=6,column=3,columnspan=2)

# execution of root
root.mainloop()
