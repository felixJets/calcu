import tkinter
from tkinter import filedialog
from tkinter import font as tkFont
from tkinter import *
import simpleeval
import re
import random


### Encoding
UNICODE_PLUS = 0x002B
UNICODE_MINUS = 0x2212
UNICODE_MULTIPLY = 0x00D7
UNICODE_DIVIDE = 0x00F7
UNICODE_EQUALS = 0x003D
UNICODE_ERASE_TO_THE_LEFT = 0x232B
UNICOD_ARTIST_PALETTE = 0x1F3A8
UNICODE_SLASH = 0x002F
UNICODE_PERCENT = 0x0025
UNICODE_OPEN_BRACKET = 0x0028
UNICODE_CLOSE_BRACKET = 0x0029
UNICODE_SKULL = 0x2620

### Colors
COLOR_FG_NUMBERS = "#ffffff"
COLOR_BG_NUMBERS = "#303030"
COLOR_ORANGE = "#ff8000"
COLOR_WINDOWS_OPERATOR = "#06f9f9"
COLOR_WINDOW = "#000000"
COLOR_BG_MATH_OPERATORS = '#202020'

### Buton position
BUTTONS_STICKY = "nsew"

### Button padding size
BUTTON_SIZE_X = 0
BUTTON_SIZE_Y = 0

### Grid Layout
### Rows
ROW_WINDOW1 = 0
ROW_WINDOW2 = 1
ROW_ORANGE = 2
ROW_PERCENT_BRACKETS = 3
ROW_789 = 4
ROW_456 = 5
ROW_123 = 6
ROW_0 = 7
### Columns
COLUMN_WINDOW1 = 0
COLUMN_WINDOW2 = 0
COLUMN_741 = 0
COLUMN_852 = 1
COLUMN_963 = 2
COLUMN_OPERATORS = 3

### Other global variables
RESET_WINDOWS = False
UPCOMING_SET = False

"""
### Calculator-Layout
___________
| Window1 |
| Window2 |
| X X X ÷ |
| % ( ) x |
| 7 8 9 - |
| 4 5 6 + |
| 1 2 3 = |
| X 0 , = |
|_________|
### 
"""


class Calculator_GUI:
    """Main window of the GUI"""

    def __init__(self, master):
        """
        Init attributes and widgets
        :param master: toplevel widget of Tk which is the main window of the application: tkinter.Tk()
        """

        self.master = master

        ### Fonts
        self.FONT_NUMBERS = tkFont.Font(family='Helvetica', size=30, weight=tkFont.NORMAL)
        self.FONT_SKULL = tkFont.Font(family='Helvetica', size=30, weight=tkFont.NORMAL)
        self.FONT_WINDOW1 = tkFont.Font(family='Helvetica', size=36, weight=tkFont.NORMAL)
        self.FONT_WINDOW2 = tkFont.Font(family='Helvetica', size=16, weight=tkFont.NORMAL)


        ### Dynamically adjust grid cells when resizing the window
        Grid.rowconfigure(self.master, 0, weight=1)
        Grid.rowconfigure(self.master, 1, weight=1)
        Grid.rowconfigure(self.master, 2, weight=1)
        Grid.rowconfigure(self.master, 3, weight=1)
        Grid.rowconfigure(self.master, 4, weight=1)
        Grid.rowconfigure(self.master, 5, weight=1)
        Grid.rowconfigure(self.master, 6, weight=1)
        Grid.rowconfigure(self.master, 7, weight=1)
        Grid.columnconfigure(self.master, 0, weight=1)
        Grid.columnconfigure(self.master, 1, weight=1)
        Grid.columnconfigure(self.master, 2, weight=1)
        Grid.columnconfigure(self.master, 3, weight=1)


        ### Add icon
        p1 = tkinter.PhotoImage(file='icons/icons8-calculator-48.png')
        self.master.iconphoto(False, p1)

        ################################ CREATE BUTTONS ################################

        self.button_quit = tkinter.Button(self.master, text="exit", command=self.master.quit)


        ### Windows as Entry-Widget
        ### justify="right": Places the text on the right side of the windows
        self.window1 = tkinter.Entry(self.master, text="", fg=COLOR_WINDOWS_OPERATOR, bg=COLOR_WINDOW,
                                     font=self.FONT_WINDOW1, justify="right")
        self.window2 = tkinter.Entry(self.master, text="", fg=COLOR_WINDOWS_OPERATOR, bg=COLOR_WINDOW,
                                     font=self.FONT_WINDOW2, justify="right")



        ### Low button row
        ### [+/- 0 .]
        self.button0 = tkinter.Button(self.master, text='0', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('0'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS)
        self.button_ul = tkinter.Button(self.master, text=chr(UNICODE_PLUS) + chr(UNICODE_SLASH) + chr(UNICODE_MINUS),
                                   padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y, command=self.change_sign, fg=COLOR_FG_NUMBERS,
                                   bg=COLOR_BG_NUMBERS, font=self.FONT_NUMBERS)
        self.button_comma = tkinter.Button(self.master, text='.', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                      command=lambda: self.update_windows('.'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                      font=self.FONT_NUMBERS)

        ### Number buttons 1-9
        self.button1 = tkinter.Button(self.master, text='1', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('1'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS)
        self.button2 = tkinter.Button(self.master, text='2', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('2'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS)
        self.button3 = tkinter.Button(self.master, text='3', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('3'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS)
        self.button4 = tkinter.Button(self.master, text='4', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('4'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS)
        self.button5 = tkinter.Button(self.master, text='5', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('5'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS)
        self.button6 = tkinter.Button(self.master, text='6', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('6'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS)
        self.button7 = tkinter.Button(self.master, text='7', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('7'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS, width=8)
        self.button8 = tkinter.Button(self.master, text='8', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('8'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS, width=8)
        self.button9 = tkinter.Button(self.master, text='9', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                 command=lambda: self.update_windows('9'), fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS,
                                 font=self.FONT_NUMBERS, width=8)

        ### Orange buttons
        self.button_color_palette = tkinter.Button(self.master, text=chr(UNICOD_ARTIST_PALETTE), padx=BUTTON_SIZE_X,
                                              pady=BUTTON_SIZE_Y, command=self.change_color, fg=COLOR_ORANGE,
                                              bg=COLOR_BG_NUMBERS, font=self.FONT_NUMBERS)
        self.button_undo = tkinter.Button(self.master, text=chr(UNICODE_ERASE_TO_THE_LEFT), padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                     command=self.undo, fg=COLOR_ORANGE, bg=COLOR_BG_NUMBERS, font=self.FONT_NUMBERS)
        self.button_clear = tkinter.Button(self.master, text='C', padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y, command=self.clear,
                                      fg=COLOR_ORANGE, bg=COLOR_BG_NUMBERS, font=self.FONT_NUMBERS)

        ### Row [% ( )]
        self.button_percent = tkinter.Button(self.master, text=chr(UNICODE_PERCENT), padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                        command=lambda: self.update_windows(chr(UNICODE_PERCENT)), fg=COLOR_FG_NUMBERS,
                                        bg=COLOR_BG_NUMBERS, font=self.FONT_NUMBERS)
        self.button_open_bracket = tkinter.Button(self.master, text=chr(UNICODE_OPEN_BRACKET), padx=BUTTON_SIZE_X,
                                             pady=BUTTON_SIZE_Y,
                                             command=lambda: self.update_windows(chr(UNICODE_OPEN_BRACKET)),
                                             fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS, font=self.FONT_NUMBERS)
        self.button_close_bracket = tkinter.Button(self.master, text=chr(UNICODE_CLOSE_BRACKET), padx=BUTTON_SIZE_X,
                                              pady=BUTTON_SIZE_Y,
                                              command=lambda: self.update_windows(chr(UNICODE_CLOSE_BRACKET)),
                                              fg=COLOR_FG_NUMBERS, bg=COLOR_BG_NUMBERS, font=self.FONT_NUMBERS)

        self.button_divide = tkinter.Button(self.master, text=chr(UNICODE_DIVIDE), padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                       command=lambda: self.update_windows(chr(UNICODE_DIVIDE)), fg=COLOR_WINDOWS_OPERATOR,
                                       bg=COLOR_BG_MATH_OPERATORS, font=self.FONT_NUMBERS, width=8)
        self.button_multiply = tkinter.Button(self.master, text=chr(UNICODE_MULTIPLY), padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                         command=lambda: self.update_windows(chr(UNICODE_MULTIPLY)),
                                         fg=COLOR_WINDOWS_OPERATOR, bg=COLOR_BG_MATH_OPERATORS, font=self.FONT_NUMBERS)
        self.button_minus = tkinter.Button(self.master, text=chr(UNICODE_MINUS), padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                      command=lambda: self.update_windows(chr(UNICODE_MINUS)), fg=COLOR_WINDOWS_OPERATOR,
                                      bg=COLOR_BG_MATH_OPERATORS, font=self.FONT_NUMBERS)
        self.button_plus = tkinter.Button(self.master, text=chr(UNICODE_PLUS), padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                     command=lambda: self.update_windows(chr(UNICODE_PLUS)), fg=COLOR_WINDOWS_OPERATOR,
                                     bg=COLOR_BG_MATH_OPERATORS, font=self.FONT_NUMBERS)
        self.button_equals = tkinter.Button(self.master, text=chr(UNICODE_EQUALS), padx=BUTTON_SIZE_X, pady=BUTTON_SIZE_Y,
                                       command=self.equals, fg=COLOR_WINDOWS_OPERATOR, bg=COLOR_BG_MATH_OPERATORS,
                                       font=self.FONT_NUMBERS)

        ################################ CREATE BUTTONS END  ################################

        ################################ DEFINE GRID LAYOUT  ################################

        ### Windows
        self.window1.grid(row=ROW_WINDOW1, column=COLUMN_741, columnspan=4, sticky=BUTTONS_STICKY)
        self.window2.grid(row=ROW_WINDOW2, column=COLUMN_741, columnspan=4, sticky=BUTTONS_STICKY)

        ###
        self.button_color_palette.grid(row=ROW_ORANGE, column=COLUMN_741, sticky=BUTTONS_STICKY)
        self.button_undo.grid(row=ROW_ORANGE, column=COLUMN_852, sticky=BUTTONS_STICKY)
        self.button_clear.grid(row=ROW_ORANGE, column=COLUMN_963, sticky=BUTTONS_STICKY)
        self.button_percent.grid(row=ROW_PERCENT_BRACKETS, column=COLUMN_741, sticky=BUTTONS_STICKY)
        self.button_open_bracket.grid(row=ROW_PERCENT_BRACKETS, column=COLUMN_852, sticky=BUTTONS_STICKY)
        self.button_close_bracket.grid(row=ROW_PERCENT_BRACKETS, column=COLUMN_963, sticky=BUTTONS_STICKY)

        ###
        self.button_divide.grid(row=ROW_ORANGE, column=COLUMN_OPERATORS, sticky=BUTTONS_STICKY)
        self.button_multiply.grid(row=ROW_PERCENT_BRACKETS, column=COLUMN_OPERATORS, sticky=BUTTONS_STICKY)
        self.button_minus.grid(row=ROW_789, column=COLUMN_OPERATORS, sticky=BUTTONS_STICKY)
        self.button_plus.grid(row=ROW_456, column=COLUMN_OPERATORS, sticky=BUTTONS_STICKY)
        self.button_equals.grid(row=ROW_123, column=COLUMN_OPERATORS, rowspan=2, sticky=BUTTONS_STICKY)

        ###
        self.button_ul.grid(row=ROW_0, column=COLUMN_741, sticky=BUTTONS_STICKY)
        self.button0.grid(row=ROW_0, column=COLUMN_852, sticky=BUTTONS_STICKY)
        self.button_comma.grid(row=ROW_0, column=COLUMN_963, sticky=BUTTONS_STICKY)

        ###
        self.button1.grid(row=ROW_123, column=COLUMN_741, sticky=BUTTONS_STICKY)
        self.button2.grid(row=ROW_123, column=COLUMN_852, sticky=BUTTONS_STICKY)
        self.button3.grid(row=ROW_123, column=COLUMN_963, sticky=BUTTONS_STICKY)
        self.button4.grid(row=ROW_456, column=COLUMN_741, sticky=BUTTONS_STICKY)
        self.button5.grid(row=ROW_456, column=COLUMN_852, sticky=BUTTONS_STICKY)
        self.button6.grid(row=ROW_456, column=COLUMN_963, sticky=BUTTONS_STICKY)
        self.button7.grid(row=ROW_789, column=COLUMN_741, sticky=BUTTONS_STICKY)
        self.button8.grid(row=ROW_789, column=COLUMN_852, sticky=BUTTONS_STICKY)
        self.button9.grid(row=ROW_789, column=COLUMN_963, sticky=BUTTONS_STICKY)

        ################################ DEFINE GRID LAYOUT END  ################################



    def update_window2(self, current_string):
        """
        This function updates the text of self.window2

        Examples: - 1000 -> 1,000
                  - Prevents "1." being transformed to "1.0"

        :param current_string: current string in self.window2
        :return: the updated string with correct formatting
        """

        ### Replace the formatting comma from large numbers
        current_string = current_string.replace(",", "")

        ### Split the string by every charachter, except of word-characters and a dot: [\w.]
        ### Match characters in []
        ### Keep the split characters for later with ()
        res = re.split(r'([^\w.])', current_string)


        ### Update elements if necessary
        current_update = ""

        for element in res:

            ### Check for int
            try:
                num = int(element)
                current_update += f"{num:,}"

            except ValueError:

                ### Check for float
                try:

                    num = float(element)
                    num_updated = f"{num:,}"

                    ### Check if element has trailing zeros, which should not be removed, e.g. "0.00"
                    ### Add zeros, which were removed in the float(element) operation
                    if len(element) != len(num_updated):
                        num_updated += "0" * (len(element) - len(num_updated))

                    current_update += num_updated

                    ### Check if element endswith "."
                    ### if True, remove added "0"
                    if element.endswith("."):
                        current_update = current_update[:-1]

                ### Append all other characters without modification to the new string
                except ValueError:
                    current_update += element


        return current_update


    def evaluate_expression(self, current_string):
        """
        This function evaluates the current expression in self.window2
        :param current_string: current string of self.window2, which should be evaluated
        :return: the result to be displayed in self.window1
        """

        NUMBERS = "0123456789"

        ### If the string endswith "." : Remove "."
        ### Prevents a "1." in self.window2 to be displayed as "1.0" in self.window1
        if current_string.endswith("."):
            current_string = current_string[:-1]

        ### Replace Unicode-characters with regular keyboard characters
        current_string = current_string.replace(chr(UNICODE_PLUS), "+")
        current_string = current_string.replace(chr(UNICODE_MINUS), "-")
        current_string = current_string.replace(chr(UNICODE_DIVIDE), "/")
        current_string = current_string.replace(chr(UNICODE_MULTIPLY), "*")
        current_string = current_string.replace(chr(UNICODE_PERCENT), "*0.01")
        current_string = current_string.replace(chr(UNICODE_OPEN_BRACKET), "(")
        current_string = current_string.replace(chr(UNICODE_CLOSE_BRACKET), ")")
        current_string = current_string.replace(",", "")

        current_string_list = list(current_string)
        indices_open_bracket = [i for i, c in enumerate(current_string_list) if c == "("]

        for index in indices_open_bracket:
            if index > 0 and current_string_list[index-1] in NUMBERS:
                current_string_list.insert(index, "*")

        current_string = "".join(current_string_list)

        ### Evaluate the expression with simpleeval [https://pypi.org/project/simpleeval/]
        result = simpleeval.simple_eval(current_string)

        return result



    def update_windows(self, n):
        """
        Updates self.window1 with the selected characters
        :param n: selected character
        :return: None
        """

        ### Set variables
        global RESET_WINDOWS
        OPERATORS = chr(UNICODE_PLUS) + chr(UNICODE_MINUS) + chr(UNICODE_MULTIPLY) \
                  + chr(UNICODE_DIVIDE) + chr(UNICODE_PERCENT)


        ### Check if the windows should be reset after pressing the equals-button
        if RESET_WINDOWS == True and n not in OPERATORS:

            self.window1.delete(0, tkinter.END)
            self.window2.delete(0, tkinter.END)
            RESET_WINDOWS = False

        else:
            RESET_WINDOWS = False

        ### Get the last inserted character
        try:
            last_inserted_character = self.window2.get()[-1]

        ### No character there yet
        except IndexError:
            last_inserted_character = "NOT AVAILABLE"

        new_operator = n

        ### Handle multiple consecutive math-operators
        if n in OPERATORS and last_inserted_character in OPERATORS:
            new_operator = self.handle_operators(n)


        ### If self.window2 only shows [   0] --> Update screen in case of a new opening bracket
        if new_operator == chr(UNICODE_OPEN_BRACKET) and last_inserted_character == "0" and len(self.window2.get()) == 1:
            self.window2.delete(0, tkinter.END)


        ### Update self.window2
        self.window2.insert(tkinter.INSERT, new_operator)
        current_text = self.window2.get()
        current_update = self.update_window2(current_text)


        self.window2.delete(0, tkinter.END)
        self.window2.insert(0, current_update)

        ### Update self.window1
        current_string = self.window2.get()

        ### Try updating window1
        try:
            result = self.evaluate_expression(current_string)
            result = f"{result:,g}"
            self.window1.delete(0, tkinter.END)
            self.window1.insert(0, result)

        ### If the new expression is invalid --> keep the old result in windwo1
        except SyntaxError:
            pass

        except ZeroDivisionError:
            print("MUSEEE!!!")
            pass

    def clear(self):
        """
        This functions clears both windows when pressing "C" and updates the entries with "0"
        and resets the color-palette button color and the "+/-" button
        :return: None
        """

        self.window1.delete(0, tkinter.END)
        self.window2.delete(0, tkinter.END)

        self.window1.insert(0, "0")
        self.window2.insert(0, "0")

        self.button_ul.configure(text=chr(UNICODE_PLUS)+chr(UNICODE_SLASH)+chr(UNICODE_MINUS), bg=COLOR_BG_NUMBERS, fg=COLOR_FG_NUMBERS)
        self.button_color_palette.configure(fg=COLOR_ORANGE)


    def undo(self):
        """
        This function removes the last character from self.window2
        and reevaluates the new expression and updates self.window1 if necessary
        :return: None
        """

        OPERATORS = chr(UNICODE_PLUS) + chr(UNICODE_MINUS) + chr(UNICODE_MULTIPLY) \
                    + chr(UNICODE_DIVIDE) + chr(UNICODE_PERCENT)

        ### Delete the last character in self.window2
        self.window2.delete(len(self.window2.get())-1)
        current_string = self.window2.get()

        if len(current_string) == 0:
            self.window1.delete(0, tkinter.END)
            self.window1.insert(0, "0")
            self.window2.insert(0, "0")
            return

        ### Update windwo2
        window2_new = self.update_window2(current_string)
        self.window2.delete(0, tkinter.END)
        self.window2.insert(0, window2_new)

        ### Update self.window1
        try:
            result = self.evaluate_expression(current_string)
            result = f"{result:,g}"
            self.window1.delete(0, tkinter.END)
            self.window1.insert(0, result)

        ### The expression could end with a math-operator: e.g. "8+2-"
        except SyntaxError:

            ### Remove the last character and try again
            try:
                current_string = self.window2.get()
                current_string = current_string[:-1]
                result = self.evaluate_expression(current_string)
                result = f"{result:,g}"
                self.window1.delete(0, tkinter.END)
                self.window1.insert(0, result)

            ### The expression could end with two math-operator: e.g. "8+2--"
            except SyntaxError:

                try:
                    current_string = self.window2.get()
                    current_string = current_string[:-2]
                    result = self.evaluate_expression(current_string)
                    result = f"{result:,g}"
                    self.window1.delete(0, tkinter.END)
                    self.window1.insert(0, result)

                except:

                    current_string = self.window2.get()

                    if current_string.count("(") != current_string.count(")"):

                        while current_string[-1] in OPERATORS:
                            current_string = current_string[:-1]

                        current_string = current_string + ")"

                    result = self.evaluate_expression(current_string)
                    result = f"{result:,g}"
                    self.window1.delete(0, tkinter.END)
                    self.window1.insert(0, result)


        except ZeroDivisionError:
            pass


    def equals(self):
        """
        This function updates self.window1 and self.window2 with the result when "=" is pressed
        :return: None
        """
        global RESET_WINDOWS

        ### Check if the windows should be reset afterwards
        math_operators = chr(UNICODE_PLUS) + chr(UNICODE_MINUS) + chr(UNICODE_MULTIPLY) \
                       + chr(UNICODE_DIVIDE) + chr(UNICODE_PERCENT)

        current_string = self.window2.get()

        ### Check if any character is a math-operator
        ### If yes --> RESET_WINDOW resets both windows if the next character is a normal number
        if any(c in current_string for c in math_operators):
            RESET_WINDOWS = True

        ### Update the windows
        try:
            result = self.evaluate_expression(self.window2.get())
            result = f"{result:,g}"
            self.window1.delete(0, tkinter.END)
            self.window1.insert(0, result)
            self.window2.delete(0, tkinter.END)
            self.window2.insert(0, result)

        except SyntaxError:

            try:
                result = self.evaluate_expression(self.window2.get()[:-1])
                result = f"{result:,g}"
                self.window1.delete(0, tkinter.END)
                self.window1.insert(0, result)
                self.window2.delete(0, tkinter.END)
                self.window2.insert(0, result)

            except:
                self.window1.delete(0, tkinter.END)
                self.window1.insert(0, "Error")

        except ZeroDivisionError:
            self.window1.delete(0, tkinter.END)
            self.window1.insert(0, "Error")


    def change_sign(self):
        """
        This function displays warnings when clicking the "+/-"-button
        :return: None
        """
        global UPCOMING_SET

        if UPCOMING_SET == False:
            self.button_ul.configure(text="STOP!", bg="#FF0000", font=self.FONT_WINDOW2)
            UPCOMING_SET = True

        else:
            self.button_ul.configure(text=chr(UNICODE_SKULL), bg=COLOR_BG_NUMBERS, fg="#FFFFFF", font=self.FONT_SKULL)
            UPCOMING_SET = False


    def handle_operators(self, new_operator):
        """
        This function handles all possible consecutive math-operator combinations
        :param new_operator: The new inserted operator
        :return: The new operator which should be displayed
        """

        ### The last two characters could possibly be two operators: e.g. [--]
        try:
            last_operator = self.window2.get()[-1]
            second_last_operator = self.window2.get()[-2]

        except IndexError:
            return

        ################ Case1: Last inserted operator was DIVIDE ################
        if last_operator == chr(UNICODE_DIVIDE):
            ### Case1: New operator is DIVIDE
            ### [÷÷] --> [÷]
            if new_operator == chr(UNICODE_DIVIDE):
                self.window2.delete(len(self.window2.get())-1)
                return chr(UNICODE_DIVIDE)
            ### Case2: New operator is MULTIPLY
            ### [÷x] --> [x]
            elif new_operator == chr(UNICODE_MULTIPLY):
                self.window2.delete(len(self.window2.get())-1)
                return chr(UNICODE_MULTIPLY)
            ### Case3: New operator is PLUS
            ### [÷+] --> [+]
            elif new_operator == chr(UNICODE_PLUS):
                self.window2.delete(len(self.window2.get()) - 1)
                return chr(UNICODE_PLUS)
            ### Case4: New operator is MINUS
            ### [÷-] --> [÷-]
            elif new_operator == chr(UNICODE_MINUS):
                return chr(UNICODE_MINUS)
            ### Case5: New operator is PERCENT
            ### [÷%] --> [÷]
            elif new_operator == chr(UNICODE_PERCENT):
                return ""

        ################ Case2: Last inserted operator was MULTIPLY ################
        elif last_operator == chr(UNICODE_MULTIPLY):
            ### Case1: New operator is DIVIDE
            ### [x÷] --> [÷]
            if new_operator == chr(UNICODE_DIVIDE):
                self.window2.delete(len(self.window2.get())-1)
                return chr(UNICODE_DIVIDE)
            ### Case2: New operator is MULTIPLY
            ### [xx] --> [x]
            elif new_operator == chr(UNICODE_MULTIPLY):
                self.window2.delete(len(self.window2.get())-1)
                return chr(UNICODE_MULTIPLY)
            ### Case3: New operator is PLUS
            ### [x+] --> [+]
            elif new_operator == chr(UNICODE_PLUS):
                self.window2.delete(len(self.window2.get()) - 1)
                return chr(UNICODE_PLUS)
            ### Case4: New operator is MINUS
            ### [x-] --> [x-]
            elif new_operator == chr(UNICODE_MINUS):
                return chr(UNICODE_MINUS)
            ### Case5: New operator is PERCENT
            ### [x%] --> [x]
            elif new_operator == chr(UNICODE_PERCENT):
                return ""

        ################ Case3: Last inserted operator was MINUS ################
        elif last_operator == chr(UNICODE_MINUS):
            ### Case1: New operator is DIVIDE
            if new_operator == chr(UNICODE_DIVIDE):
                ### [--÷] --> [÷]
                ### [x-÷] --> [÷]
                if second_last_operator in chr(UNICODE_MINUS) + chr(UNICODE_MULTIPLY):
                    self.window2.delete(len(self.window2.get()) - 2, tkinter.END)
                    return chr(UNICODE_DIVIDE)
                ### [-÷] --> [÷]
                else:
                    self.window2.delete(len(self.window2.get()) - 1)
                    return chr(UNICODE_DIVIDE)
            ### Case2: New operator is MULTIPLY [-x] --> [x]
            elif new_operator == chr(UNICODE_MULTIPLY):
                ### [--x] --> [x]
                if second_last_operator == chr(UNICODE_MINUS):
                    self.window2.delete(len(self.window2.get()) - 1)
                self.window2.delete(len(self.window2.get()) - 1)
                return chr(UNICODE_MULTIPLY)
            ### Case3: New operator is PLUS
            elif new_operator == chr(UNICODE_PLUS):
                ### [--+] --> [+]
                ### [x-+] --> [+]
                if second_last_operator in chr(UNICODE_MINUS) + chr(UNICODE_MULTIPLY):
                    self.window2.delete(len(self.window2.get()) - 2, tkinter.END)
                    return chr(UNICODE_PLUS)
                ### [-+] --> [+]
                else:
                    self.window2.delete(len(self.window2.get()) - 1)
                    return chr(UNICODE_PLUS)
            ### Case4: New operator is MINUS
            elif new_operator == chr(UNICODE_MINUS):
                ### [---] --> [-]
                ### [+--] --> [-]
                if second_last_operator in chr(UNICODE_MINUS) + chr(UNICODE_PLUS):
                    self.window2.delete(len(self.window2.get())-2, tkinter.END)
                    return chr(UNICODE_MINUS)
                ### [--] --> [--]
                else:
                    return chr(UNICODE_MINUS)
            ### Case5: New operator is PERCENT
            elif new_operator == chr(UNICODE_PERCENT):
                return ""

        ################ Case4: Last inserted operator was PLUS ################
        elif last_operator == chr(UNICODE_PLUS):
            ### Case1: New operator is DIVIDE
            ### [+÷] --> [÷]
            if new_operator == chr(UNICODE_DIVIDE):
                self.window2.delete(len(self.window2.get()) - 1)
                return chr(UNICODE_DIVIDE)
            ### Case2: New operator is MULTIPLY
            ### [+x] --> [x]
            elif new_operator == chr(UNICODE_MULTIPLY):
                self.window2.delete(len(self.window2.get()) - 1)
                return chr(UNICODE_MULTIPLY)
            ### Case3: New operator is PLUS
            ### [+] --> [+]
            elif new_operator == chr(UNICODE_PLUS):
                self.window2.delete(len(self.window2.get()) - 1)
                return chr(UNICODE_PLUS)
            ### Case4: New operator is MINUS
            ### [+-] --> [+-]
            elif new_operator == chr(UNICODE_MINUS):
                return chr(UNICODE_MINUS)
            ### Case5: New operator is PERCENT
            ### [+%] --> [+]
            elif new_operator == chr(UNICODE_PERCENT):
                return ""

        ################ Case5: Last inserted operator was PERCENT ################
        elif last_operator == chr(UNICODE_PERCENT):
            ### Case1: New operator is DIVIDE
            ### [%÷] --> [%÷]
            if new_operator == chr(UNICODE_DIVIDE):
                return chr(UNICODE_DIVIDE)
            ### Case2: New operator is MULTIPLY
            ### [%x] --> [%x]
            elif new_operator == chr(UNICODE_MULTIPLY):
                return chr(UNICODE_MULTIPLY)
            ### Case3: New operator is PLUS
            ### [+] --> [+]
            elif new_operator == chr(UNICODE_PLUS):
                return chr(UNICODE_PLUS)
            ### Case4: New operator is MINUS
            ### [+-] --> [+-]
            elif new_operator == chr(UNICODE_MINUS):
                return chr(UNICODE_MINUS)
            ### Case5: New operator is PERCENT
            ### [+%] --> [+]
            elif new_operator == chr(UNICODE_PERCENT):
                return ""


    def change_color(self):
        """
        This function randomly changes the color of the color-palette
        :return: None
        """

        ### Create random hex color code
        random_color = '#' + "%06x" % random.randint(0, 0xFFFFFF)
        ### Set color
        self.button_color_palette.configure(fg=random_color)




if __name__ == "__main__":


    ### Define root
    root = tkinter.Tk()

    ### Title and eometry
    root.title("CALCU")
    root.geometry("350x650")

    ### Create GUI
    calc = Calculator_GUI(root)

    ### Start with "0" in both windows
    calc.window1.insert(0, "0")
    calc.window2.insert(0, "0")


    ### Start GUI
    root.mainloop()
