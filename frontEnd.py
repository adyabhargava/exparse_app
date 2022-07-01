from tkinter import *

import openpyxl
import pandas as pd
from selenium import webdriver
from tkinter import messagebox
import burger_king
import kfc
import pizza_hut
import dominos
from constants import *
import validators
import mcd
from PIL import ImageTk, Image


class frontEnd:
    """ This class contains the code for the frontend of the program."""

    def create_window(self):
        """ This creates a new window with the required title and dimensions."""
        #Creates an empty window
        self.window = Tk()
        #Gives the correct title to the window
        self.window.title(main_window_title)
        #Makes the window the required size
        self.window.geometry(main_window_dimensions)

    def create_submit_button(self):
        """ Creates a new submit button with the required text, size, position and response.
        Makes sure that when the button is clicked, run_program() runs."""
        #Creates a new submit button with the required text, response command and size.
        self.submit_button = Button(self.window, text = submit_button_text, command = self.run_program, width= submit_button_width)
        #Places the submit button at the correct position
        self.submit_button.place(x=submit_button_x_posn, y=submit_button_y_posn)

    def create_instruction_label(self):
        """Creates a new instructions label with the required text and position: This is the text that says 'Instructions'."""
        #Creates a new label for instructions
        self.instructions_label = Label(self.window, text=instructions_label_text, fg='black', font=instructions_label_font)
        #Places the instructions label at the correct position
        self.instructions_label.place(x=instructions_label_x_posn, y=instructions_label_y_posn)

    def input_gui(self, box_x_posn, box_y_posn, label_text, label_x_posn, label_y_posn):
        """ This creates an entry boxes and its corresponding labels.
        Parameters:
        1) box_x_posn: x-coordinate of the input box. Must be of type int.
        2) box_y_posn: y-coordinate of the input box. Must be of type int
        3) label_text: Text of the label corresponding the box. Must be of String type.
        4) label_x_posn:  x-coordinate of the input label. Must be of type int.
        5) label_y_posn: y-coordinate of the input label. Must be of type int.
        Returns:
        An Entry instance of the corresponding input. Can get value of input from this by calling
        the get method on it."""
        #Creates a new input box and places it at the correct position
        box = Entry(self.window, width=input_box_width, borderwidth=input_box_borderwidth)
        box.place(x=box_x_posn, y=box_y_posn)
        #Creates a new label for the input with the required text and position
        label = Label(self.window, text=label_text, fg='black', font=input_label_font)
        label.place(x=label_x_posn, y=label_y_posn)
        #returns the input box item
        return box

    def create_creator_label(self):
        """ This creates a new label indicating that the creator is Adya B"""
        #Creates a new label for the creator designation
        self.adya = Label(self.window, text=creator_label_text, fg='black', font=creator_label_font)
        #Places the creator label at the required position.
        self.adya.place(x = creator_label_x_posn, y=creator_label_y_posn)

    def create_logo(self):
        """ This creates and embeds the logo on the window screen
        NOTE: It uses the logo image itself, and we need logo image location."""
        #Accesses the logo image location and opens it in Python.
        self.logo_image = Image.open(logo_image_filepath)
        #Resizes image according to requirements.
        self.resized_image = self.logo_image.resize((logo_image_x_size, logo_image_y_size), Image.ANTIALIAS)
        #Creates a PhotoImage object from the resized image.
        self.logo = ImageTk.PhotoImage(self.resized_image)
        #Creates a Logo object and places the image in that.
        self.logo_label = Label(self.window, image=self.logo)
        #Places the image at the correct spot.
        self.logo_label.place(x=logo_x_posn, y=logo_y_posn)

    def create_instructions_button(self):
        """ This creates an instructions button. We can click on this and access the Instructions on using program."""
        #Creates a new Button object with the text.
        self.instructions_button = Button(self.window, text = instructions_button_text, command = self.instructions_link, width= instructions_button_width)
        #Places the submit button at the correct position
        self.instructions_button.place(x=instructions_button_x_posn, y=instructions_button_y_posn)

    def instructions_link(self):
        """ This links the instructions button to the website with instructions."""
        driver = webdriver.Chrome(chromedriver_location)
        driver.get(instructions_button_website)

    def create_website_menu(self, x_posn, y_posn):
        """ This only creates the dropdown menu with all options of websites to scrape."""
        #The blank menu is of String type.
        self.blank_menu = StringVar()
        #Creates a blank menu with a default title.
        self.blank_menu.set(dropdown_menu_default_title)
        #Puts that on the window with the options given in constants.
        self.dropdown_menu= OptionMenu(self.window, self.blank_menu, *orgs_options)
        #Places the menu on the window.
        self.dropdown_menu.place(x=x_posn, y=y_posn)
        #Sets width of the menu box to the default depth.
        self.dropdown_menu.config(width= dropdown_menu_width)

    def create_website_label(self, x_posn, y_posn):
        """ This creates a text that tells the user where to input the website to scrape"""
        #Creates a label object
        label = Label(self.window, text=website_label_text, fg='black', font=input_label_font)
        #Places it where necessary
        label.place(x=x_posn, y=y_posn)

    def create_website_and_label(self, menu_x_posn, menu_y_posn, label_x_posn, label_y_posn):
        """ This creates the website to scrape menu and label text. Calls helper methods to do each of those tasks."""
        self.create_website_menu(menu_x_posn, menu_y_posn)
        self.create_website_label(label_x_posn, label_y_posn)

    def frontend_display(self):
        """ This method creates the full display."""
        #Creates a new empty window
        self.create_window()
        #Puts a submit button on the window using the helper method above
        self.create_submit_button()
        #Puts a instruction label on the window using the helper method above
        self.create_instruction_label()
        #Puts an instructions button using the helper method above
        self.create_instructions_button()
        #Puts the required input boxes and labels on the window using the helper method above
        self.filepath_box = self.input_gui(filepath_box_x_posn, filepath_box_y_posn, filepath_label_text, filepath_label_x_posn, filepath_label_y_posn)
        self.sheetname_box = self.input_gui(sheetname_box_x_posn, sheetname_box_y_posn, sheetname_label_text, sheetname_label_x_posn, sheetname_label_y_posn)
        self.create_website_and_label(website_box_x_posn, website_box_y_posn, website_label_x_posn, website_label_y_posn)
        self.column_extract_box = self.input_gui(column_extractbox_x_posn, column_extractbox_y_posn, column_extractlabel_text, column_extractlabel_x_posn, column_extractlabel_y_posn)
        self.column_insert_box = self.input_gui(column_inputbox_x_posn, column_inputbox_y_posn, column_input_label_text, column_inputlabel_x_posn, column_inputlabel_y_posn)
        #Puts a new creator label on the window using the helper method above
        self.create_creator_label()
        #Puts the logo on the window by using the helper method above.
        self.create_logo()
        #Starting the mainloop
        self.window.mainloop()

    def check_for_number(self, column):
        """ This helper method checks whether any part of the column to input in has a number.
        Parameter column: A string representation of the column the data is to be inputted into.
        Returns: True if there is a number in the column and False if there isn't."""
        has_number = False
        #Checks if any element in column is a number.
        for elem in column:
            if elem.isdigit():
                has_number = True
        return has_number

    def check_for_lowercase(self, column):
        """ This helper method checks whether any part of the column to input is a lowercase letter.
        Parameter column: A string representation of the column the data is to be inputted into.
        Returns: True if there is a lowercase letter in the column and False if there isn't."""
        has_lower = False
        #Checks if any element in column is a lowercase letter.
        for elem in column:
            if elem.islower():
                has_lower = True
        return has_lower

    def valid_column(self, column):
        """ This checks if the column inputted into the box is a valid column:
        1) Ensures that there are no numbers
        2) Ensures that there are no lowercase letters.
        3) Ensures that the input box is not entirely empty.
        Uses helper methods check_for_number() and check_for_lowercase().
        Parameter column: A string representation of the column the data is to be inputted into.
        Sets self.is_valid_column as True if the column input is valid, and False if it is not. Raises ArithmeticError
        if it is an invalid input."""
        #Checks if number in the column (this would give error)
        num = self.check_for_number(column)
        #Checks if lowercase letter in the column (this would give error)
        lower = self.check_for_lowercase(column)
        #Checks if column input is empty (this would give error)
        nothing = column == ""
        #Checks if either of these errors are present. Changes is_valid_column to False if errors present.
        if num or lower or nothing:
            #self.is_valid_column = False
            #raise ArithmeticError
            return False
        #Else, changes is_valid_column to True.
        else:
            #self.is_valid_column = True
            return True

    def create_error_warning(self, error_message):
        """ Creates a new error message box with the required title and message."""
        messagebox.showerror(title = error_title, message= error_message )

    def is_valid_url(self, url):
        """ This method checks whether the inputted url is valid."""
        #validators.url returns True only if the website inputted is valid.
        website_validity = validators.url(url)
        if website_validity!= True:
            return False
            #raise ChildProcessError
        else:
            return True

    def are_websites_valid(self, websites):
        """ This checks if all the websites inputted are valid. Raises ChildProcessError if not.
        Calls helper method is_valid_url(website).
        Parameter: Websites to verify"""
        self.websites_validity = True
        for website in websites:
            this_web_validity = self.is_valid_url(website)
            self.websites_validity = self.websites_validity and this_web_validity
        if not self.websites_validity:
            raise ConnectionRefusedError
        #return self.websites_validity

    def check_if_row_empty(self, column):
        """ This method checks if a given row is empty. It returns True if it is, and False if it is not."""
        ps = openpyxl.load_workbook(self.filepath)
        sheet = ps[self.sheetname]
        #Regulator that checks whether or not row is empty
        check = 0
        #Loops over every row in given column to check whether or not it is empty
        for row in range(2, sheet.max_row + 1):
            value = sheet[column + str(row)].value
            #If it is not empty, adds 1 to check.
            if value!= "":
                check +=1
        #Check is >0 only when there are 1 or more item entries in that column. Otherwise, check is 0/
        # Thus, it returns True only when check is equal to 0.
        if check==0:
            return True
        else:
            return False

    def okay(self):
        self.getInputs()

    def no_org_error(self):
        """Checks that an organization has been inputted, and that element has not been left blank.
        Sets self.org_error to False if there is no error, and True if there is. Raises BufferError
        if there is an error."""
        self.org_error = False
        if self.organization == dropdown_menu_default_title:
            self.org_error = True
            raise BufferError

    def websites_input(self):
        if self.organization == "McDonalds":
            self.websites = mcdonalds
        if self.organization == "KFC":
            self.websites = kfc_website
        if self.organization == "Burger King":
            self.websites =  burger_king
        if self.organization == "Pizza Hut":
            self.websites = pizza_hut
        if self.organization == "Dominos":
            self.websites = dominos

    def error_handling(self):
        """Intercepts and handles all possible errors:
        1) FileNotFoundError: Occurs when invalid filepath.
        2) ValueError: Occurs when invalid sheetname
        3) AttribuetError: Occurs when no column "Name" exists.
        4) ArithmeticError: Occurs when invalid column to add to.
        5) All other errors: If invalid website link."""
        try:
            #Checks for validity of the inputted filepath
            self.wrong_filepath = False
            excelFile = pd.ExcelFile(self.filepath)
            #Checks for validity of the inputted sheetname
            self.wrong_sheetname = False
            data = excelFile.parse(self.sheetname)
            #Checks for the validity of input of the column to extract from and raises ConnectionError if it is not.
            if not self.valid_column(self.column_extract):
                raise ConnectionError()
            #Checks for whether the column inputted is empty or not. If it is empty, this raises a ChildProcessError.
            if self.check_if_row_empty(self.column_extract):
                raise ChildProcessError
            #Checks for the validity of the column to input into and raises InterruptedError if it is not.
            if not self.valid_column(self.column_input):
                raise InterruptedError()
            #Makes sure that an organization has been inputted into the program:
            self.no_org_error()
            #Checks for validity of all the inputted website and raises ChildProcess error if it is not.
            if not self.org_error:
                self.are_websites_valid(self.websites)
        #Handles error regarding invalid filepath input
        except(FileNotFoundError):
            self.wrong_filepath = True
            self.create_error_warning(invalid_filepath_error_message)
        #Handles error regarding invalid sheetname input
        except(ValueError):
            self.wrong_sheetname = True
            self.create_error_warning(invalid_sheetname_error_message)
        except(BufferError):
            self.create_error_warning(invalid_org_error_message)
        #Handles error regarding invalid website address.
        except(ConnectionRefusedError):
            self.create_error_warning(invalid_website_error_message)
        #Handles error regarding invalid column to extract
        except(ConnectionError):
            self.create_error_warning(invalid_column_to_parse)
        #Handles error regarding empty column to extract
        except(ChildProcessError):
            self.create_error_warning(empty_column_to_extract)
        #Handles error regarding invalid column to input into
        except(InterruptedError):
            self.create_error_warning(invalid_column_to_appendTo)

    def getInputs(self):
        """ This method gets the values of the inputs.
        Fields it creates:
        1) self.filepath stores the path to the Excel file to be manipulated.
        2) self.sheetname stores the Sheet name to edit data into.
        3) self.organization gets the name of the organization we need the data from.
        4) self.column_extract gets the mame of the column to extract name of items from.
        5) self.column_input gets the name of the column to enter data into."""
        self.filepath = self.filepath_box.get()
        self.sheetname = self.sheetname_box.get()
        self.organization = self.blank_menu.get()
        self.websites_input()
        self.column_extract = self.column_extract_box.get()
        self.column_input = self.column_insert_box.get()


    def create_info_message(self, box_title, box_message ):
        """ This method notifies the user that the data is being inputted into the required column"""
        messagebox.showinfo(title= box_title, message= box_message)

    #NOTE: YET TO CREATE THIS METHOD!!
    def correct_website_question(self):
        """ This method creates a question messagebox to ask the user to confirm the website"""
        answer = messagebox.askquestion(title= correct_website_title, message= correct_website_message)
        #if answer == "Yes":

    def create_backend_object(self):
        if self.organization == "McDonalds":
            return mcd.mcdonald(self.filepath, self.sheetname, self.websites, self.column_extract, self.column_input)
        if self.organization == "KFC":
            return kfc.kfc_class(self.filepath, self.sheetname, self.websites, self.column_extract, self.column_input)
            #return kfc.kfc(self.filepath, self.sheetname, self.websites, self.column)
        if self.organization == "Burger King":
            return burger_king.burger_king(self.filepath, self.sheetname, self.websites, self.column_extract, self.column_input)
        if self.organization == "Pizza Hut":
            return pizza_hut.pizza_hut(self.filepath, self.sheetname, self.websites, self.column_extract, self.column_input)
        if self.organization == "Dominos":
            return dominos.dominos(self.filepath, self.sheetname, self.websites, self.column_extract, self.column_input)

    def run_program(self):
        """ This uses all the helper methods above to run the program."""
        #Gets the inputs entered into each of the input boxes.
        self.getInputs()
        #Handles all user input errors.
        self.error_handling()
        #Ensures that all necessary data is present before it can be accessed and used in the program.
        #Checks that column to extract from has valid entry
        if not self.wrong_filepath:
            if not self.wrong_sheetname:
                if self.valid_column(self.column_extract):
                    #Checks that column to extract from is not empty
                    if not self.check_if_row_empty(self.column_extract):
                        #Checks that column to input into has valid entry.
                        if self.valid_column(self.column_input):
                            if not self.org_error:
                                self.all_websites_valid = self.websites_validity
                                if self.websites_validity:
                                    self.actual_runner()


    def actual_runner(self):
        runner = self.create_backend_object()
        #Extracts names of all items from the inputted excel sheet,
        runner.extract_from_excel()
        #Notifies the user that the program is running.
        self.create_info_message(run_notif_title, run_notif_message)
        #This extracts all prices and items from a webiste.
        runner.extract_all_prices()
        #put message box asking whether or not to put data into this column
        #Puts the data into an excel sheet.
        runner.put_in_excel()
        #Checks if there are any new items
        new = runner.check_if_new()
        #If there are, then it gives a message box saying there are. If not, does nothing.
        if new:
            self.create_info_message(new_items_title, box_message= new_items_message + self.column_input)
            runner.handle_new_items()
            #runner.action_new_items()
        #NOTE: Notify that there are new items named x x x and x. Ask whether or not to add: Make it yes or no

        #Notifies that the program is done
        self.create_info_message(program_done_title, program_done_message)


    def main(self):
        self.frontend_display()