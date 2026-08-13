import tkinter

FONT = ("Arial",12)

def convert_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")
    
window = tkinter.Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = tkinter.Entry(width=8, font=FONT)
miles_input.grid(column=1, row=0)

miles_label = tkinter.Label(text= "Miles", font=FONT)
miles_label.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

km_result_label = tkinter.Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)

calculate_button = tkinter.Button(text="Calculate", command=convert_to_km, font=FONT)
calculate_button.grid(column=1, row=2)


window.mainloop()