""" This file stores all the constants used in the program"""

""" Loation of chromedriver"""
chromedriver_location = "/Users/adyab/Desktop/HDFC internship/CS Program/Python Version /lib/chromedriver"

"""These variables are for the main window."""
main_window_title = "Input Data"
main_window_width = "1200"
main_window_height = "770"
main_window_dimensions = main_window_width+"x"+main_window_height+"+30+40"

"""These variables are for the submit button."""
submit_button_text =  "Input"
submit_button_width = 30
submit_button_x_posn = 490
submit_button_y_posn = 650

""" These variables are for the instructions button."""
instructions_button_text =  "Instructions"
instructions_button_website = "https://www.programiz.com/python-programming/file-operation"
instructions_button_width = 20
instructions_button_x_posn = 642
instructions_button_y_posn = 271

"""These variables are for the instructions label."""
instructions_label_text = "Click Here to view Instrutions:"
instructions_label_font = ("Helvetica", 15, 'bold')
instructions_label_x_posn = 405
instructions_label_y_posn = 273

"""These variables are for all input boxes and labels."""
input_box_width = 85
input_box_borderwidth = 5
input_label_font = ("Helvetica", 15)

"""These variables are for the filpath input boxes and labels."""
filepath_box_x_posn = 350
filepath_box_y_posn = 360
filepath_label_text = "Filepath:"
filepath_label_x_posn = 170
filepath_label_y_posn = 363

"""These variables are for the sheetname input boxes and labels."""
sheetname_box_x_posn = 350
sheetname_box_y_posn = 410
sheetname_label_text = "Sheet Name:"
sheetname_label_x_posn = 170
sheetname_label_y_posn = 413

"""These variables are for the input boxes and labels for the column to extract data from."""
column_extractbox_x_posn = 350
column_extractbox_y_posn = 460
column_extractlabel_text = "Column to extract from:"
column_extractlabel_x_posn = 170
column_extractlabel_y_posn = 462

"""These variables are for the columns to input data into."""
column_inputbox_x_posn = 350
column_inputbox_y_posn = 510
column_input_label_text = "Column to input into:"
column_inputlabel_x_posn = 170
column_inputlabel_y_posn = 512

"""These variables are for the website input boxes and labels."""
website_box_x_posn = 350
website_box_y_posn = 560
website_label_text = "Website to scrape:"
website_label_x_posn = 170
website_label_y_posn = 563
orgs_options = [
    "McDonalds",
    "KFC",
    "Burger King",
    "Pizza Hut",
    "Dominos"]
dropdown_menu_width = 85
dropdown_menu_default_title = "Website to Scrape Data from"

"""These variables are for the creator label"""
creator_label_text = "Created by Adya Bhargava, 2022"
creator_label_font = ("Helvetica", 15, 'bold')
creator_label_x_posn = 20
creator_label_y_posn = 733

"""These variables are for the logo."""
logo_image_filepath = "/Users/adyab/Desktop/PriceTrack.png"
logo_image_x_size = 300
logo_image_y_size = 150
logo_x_posn = 460
logo_y_posn = 60

"""These variables are for handling errors."""
error_title = "Error"
invalid_filepath_error_message = "Invalid filepath.\n \nSee instructions for more information."
invalid_sheetname_error_message = "Invalid sheet name.\n \nSee instructions for more information."
invalid_column_to_parse = "Invalid column to extract data from.\n \nSee instructions for more information."
invalid_column_to_appendTo = "Invalid column to input data into.\n \nSee instructions for more information."
invalid_website_error_message = "Invalid website link.\n \nContact the program developer."
invalid_org_error_message = "Please input an organization! \n \nYou can access options in the dropdown menu."
empty_column_to_extract = "The column has no items to search as it is empty. \n \nSee instructions for more information."

""" These variables are for notifying the user what the program is doing"""
correct_website_title = "Confirm Website"
correct_website_message = "Extracting data"
#ABOVE 2 ARE YET TO BE UPDATED.
run_notif_title = "Confirm"
run_notif_message = "The program is running."
program_done_title = "Finished"
program_done_message = "Program completed. The data is in the excel file.\n You can run the program for another dataset or shut the program."
new_items_title = "New Items Available"
new_items_message = "There are new items. Adding names of items to excel file in column "

""" These variables store the websites of each organization."""
mcdonalds = ["https://www.mcdelivery.co.in/home/new-launches", "https://www.mcdelivery.co.in/home/trending"]
"""mcdonalds = ["https://www.mcdelivery.co.in/home/new-launches", "https://www.mcdelivery.co.in/home/trending",
            "https://www.mcdelivery.co.in/home/deals", "https://www.mcdelivery.co.in/home/burgers-wraps",
             "https://www.mcdelivery.co.in/home/gourmet-burgers-and-meals", "https://www.mcdelivery.co.in/home/meals",
             "https://www.mcdelivery.co.in/home/mcsaver-snacks", "https://www.mcdelivery.co.in/home/coffee-and-tea",
             "https://www.mcdelivery.co.in/home/shakes-and-coolers", "https://www.mcdelivery.co.in/home/muffins-and-more",
             "https://www.mcdelivery.co.in/home/beverages", "https://www.mcdelivery.co.in/home/happy-meals",
             "https://www.mcdelivery.co.in/home/sides-dips", "https://www.mcdelivery.co.in/home/desserts",
             "https://www.mcdelivery.co.in/home/sharing-combos", "https://www.mcdelivery.co.in/home/recommended"]"""
#mcdonalds = ["https://www.mcdelivery.co.in/home/new-launches", "https://www.mcdelivery.co.in/home/trending"]
dominos = "https://pizzaonline.dominos.co.in/menu"
#kfc_website = ["https://online.kfc.co.in/menu/chicken-buckets", "https://online.kfc.co.in/menu/new-launch"]
kfc_website = ["https://online.kfc.co.in/menu/chicken-buckets", "https://online.kfc.co.in/menu/new-launch",
               "https://online.kfc.co.in/menu/biryani-buckets", "https://online.kfc.co.in/menu/box-meals",
               "https://online.kfc.co.in/menu/burgers", "https://online.kfc.co.in/menu/stay-home-specials",
               "https://online.kfc.co.in/menu/snacks", "https://online.kfc.co.in/menu/beverages"]
burger_king = "https://www.burgerking.in/product-listing"
pizza_hut = "https://www.pizzahut.co.in/order/deals/"
