from tkinter import *
from tkinter import messagebox


###################
# Main window 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
###################s


def function_a():
    print('A')
    return


def function_b():
    print('B')
    return


def fucntion_c():
    print('C')
    return

def function_f():
    print('F')
    return

def function_g():
    print('G')
    return

root = Tk()


###################
# Global variables
###################


# expression string of tkinter type StringVar type for output
expression = StringVar()

# result string of tkinter type StringVar for output
result = StringVar()

# expression string of python type String for internal operations
operation_string = ''

# total(result) of python type String for internal operations
total = ''

# Flag for checking whether previously pressed button was an operation button
flag = False

# Expression to show in the Expression field of python type String
expression_to_show = ''

###################
# Functions
###################


# Getting input from the user using buttons in GUI
def inp(a, is_operation_button_pressed=False):
    global operation_string, expression_to_show, flag, total
    # Checking if there is no leading zero
    if not is_operation_button_pressed and expression_to_show == '0':
        return
    # Checking that there is no leading operation signs except '-'
    if is_operation_button_pressed and expression_to_show == '' and str(a) != '-':
        return
    # Adding negative numbers
    if is_operation_button_pressed and expression_to_show == '' and str(a) == '-':
        operation_string += str(a)
        expression_to_show += str(a)
        expression.set(expression_to_show)
        flag = False
        return
    # Checking that there is no multiple leading operation signs
    if is_operation_button_pressed and expression_to_show == '-':
        flag = True
        return
    # Taking numbers and adding them
    if not is_operation_button_pressed and not flag:
        expression_to_show = expression_to_show + str(a)
        operation_string = operation_string + str(a)
        expression.set(expression_to_show)
        flag = False
        return
    # Adding new operation after pressing '='
    if is_operation_button_pressed and flag \
            and expression_to_show[-1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        expression_to_show = expression_to_show + str(a)
        operation_string = operation_string + str(a)
        expression.set(expression_to_show)
        flag = True
        return
    # Replacing the last operations sign
    # if buttons with operation were pressed multiple times in a row
    if is_operation_button_pressed and flag and str(a) != '-' and expression_to_show != '-':
        operation_string = operation_string[:-1] + str(a)
        expression.set(expression_to_show[:-1] + str(a))
        flag = True
        return
    # Adding the first entered operation sign
    if is_operation_button_pressed and not flag:
        # Counting transitional result
        if any(sign in operation_string[:-1] for sign in ['+', '-', '*', '/']):
            count()
            expression_to_show += str(a)
            operation_string += str(a)
            total = ''
            expression.set(expression_to_show)
            result.set('')
            return
        operation_string += str(a)
        expression_to_show += str(a)
        expression.set(expression_to_show)
        flag = True
        return
    # Adding the first digit of the new number after operation button was pressed
    # Clearing the expression field and printing the first digit of a new number or a '-' sign
    if not is_operation_button_pressed and flag or (is_operation_button_pressed and flag and str(a) == '-'):
        operation_string = operation_string + str(a)
        expression_to_show = str(a)
        expression.set(expression_to_show)
        flag = False
        return


# Counting result and catching errors
def count():
    global operation_string, total, flag, expression_to_show
    try:
        total = int(float(eval(operation_string)))
        if total > 999999:
            write_result_to_file(f'{operation_string} = E')
            clear()
            total = 'E'
            return
        write_result_to_file(f'{operation_string} = {str(total)}')
        expression_to_show = str(total)
        operation_string = str(total)
        result.set(str(total))
        flag = True
    except ZeroDivisionError:
        write_result_to_file(f'{operation_string} = Error. Division by zero')
        clear()
        messagebox.showinfo('Error', "Don't divide by zero")
    except SyntaxError:
        pass
    return


# Deleting all the output in result and expression Entry fields
def clear():
    global operation_string, total, flag, expression_to_show
    operation_string = ''
    expression.set('')
    result.set('')
    total = ''
    expression_to_show = ''
    flag = False
    return


# Writing results to a text file in the project directory
def write_result_to_file(string):
    with open('calc_log.txt', 'a') as file:
        file.write(f'{string}\n')
    return


###################
# GUI
###################


root['bg'] = '#F4FBFB'
root.title('Calculator')
root.geometry('300x400')
root.resizable(width=False, height=False)


# Making output fields with labels for expression and the result
operation_label = Label(text='Expression:', fg='#060D38', bg='#F4FBFB', justify='left', height=2)
result_label = Label(text='Result:', fg='#060D38', bg='#F4FBFB', justify='left', height=2)
operation_output = Entry(textvariable=expression, fg='#060D38', bg='#F4FBFB', justify='right', width=12)
result_output = Entry(textvariable=result, fg='#060D38', bg='#F4FBFB', justify='right', width=12)

# Placing labels and Entry fields inside window grid
operation_label.grid(row=0, column=0, columnspan=2, sticky=W, padx=10, pady=10)
operation_output.grid(row=0, column=2, columnspan=2, sticky=E+W, padx=10, pady=10)
result_label.grid(row=1, column=0, columnspan=2, sticky=W, padx=10, pady=10)
result_output.grid(row=1, column=2, columnspan=2, sticky=E+W, padx=10, pady=10)

# Making and placing all the buttons with assigned functions for getting input form the user
Button(text='1', command=lambda: inp(1), height=2, width=2).grid(row=2, column=0, padx=10, pady=10)
Button(text='2', command=lambda: inp(2), height=2, width=2).grid(row=2, column=1, padx=10, pady=10)
Button(text='3', command=lambda: inp(3), height=2, width=2).grid(row=2, column=2, padx=10, pady=10)
Button(text='4', command=lambda: inp(4), height=2, width=2).grid(row=3, column=0, padx=10, pady=10)
Button(text='5', command=lambda: inp(5), height=2, width=2).grid(row=3, column=1, padx=10, pady=10)
Button(text='6', command=lambda: inp(6), height=2, width=2).grid(row=3, column=2, padx=10, pady=10)
Button(text='7', command=lambda: inp(7), height=2, width=2).grid(row=4, column=0, padx=10, pady=10)
Button(text='8', command=lambda: inp(8), height=2, width=2).grid(row=4, column=1, padx=10, pady=10)
Button(text='9', command=lambda: inp(9), height=2, width=2).grid(row=4, column=2, padx=10, pady=10)
Button(text='0', command=lambda: inp(0), height=2, width=2).grid(row=5, column=1, padx=10, pady=10)
Button(text='-', command=lambda: inp('-', True), height=2, width=2).grid(row=2, column=3, padx=10, pady=10)
Button(text='+', command=lambda: inp('+', True), height=2, width=2).grid(row=3, column=3, padx=10, pady=10)
Button(text='/', command=lambda: inp('/', True), height=2, width=2).grid(row=4, column=3, padx=10, pady=10)
Button(text='*', command=lambda: inp('*', True), height=2, width=2).grid(row=5, column=3, padx=10, pady=10)
Button(text='=', command=lambda: count(), fg='green', height=2, width=2).grid(row=5, column=2, padx=10, pady=10)
Button(text='C', command=lambda: clear(), fg='red', height=2, width=2).grid(row=5, column=0, padx=10, pady=10)

root.mainloop()


# asd
# sdf
