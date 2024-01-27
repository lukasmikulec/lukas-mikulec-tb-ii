# importing libraries used in the app
import tkinter as tk # for creating the gui window
import customtkinter as ctk # for upgrading the gui design to a modern look
import pandas as pd # for storing user data in dataframes
from tkinter import messagebox # for displaying desktop messages
import tkintermapview as tkmap # for map display
import geocoder # to get the user location based on user IP address for the map widget
from datetime import datetime # for generating unique activity identifiers when creating new activities
from PIL import Image # for dealing with images in CTk Image
import webbrowser as wb # for opening phone numbers on WhatsApp through URL link

# create the GUI window
window = ctk.CTk()

# name the GUI window
window.title("Activities 2.0")

# define the width and height of the app
width, height = 350, 650

# set the GUI window size
window.geometry(f"{width}x{height}")
# set the GUI minimum window size
window.minsize(width,height)

# define pathways for images used within functions (must be defined outside of functions to be displayed)
sun_icon = ctk.CTkImage(light_image=Image.open("images/sun_outline.png"),
                        dark_image=Image.open("images/sun_outline_dark.png"), size=(50, 50))
plus_icon = ctk.CTkImage(light_image=Image.open("images/plus.png"),
                         dark_image=Image.open("images/plus_dark.png"), size=(20, 20))
activities_taskbar_icon_outline = ctk.CTkImage(light_image=Image.open("images/sun_outline.png"),
                                               dark_image=Image.open("images/sun_outline_dark.png"), size=(20, 20))
activities_taskbar_icon = ctk.CTkImage(light_image=Image.open("images/sun.png"),
                                       dark_image=Image.open("images/sun_dark.png"), size=(20, 20))
map_taskbar_icon_outline = ctk.CTkImage(light_image=Image.open("images/map_outline.png"),
                                        dark_image=Image.open("images/map_outline_dark.png"), size=(16, 16))
map_taskbar_icon = ctk.CTkImage(light_image=Image.open("images/map.png"),
                                dark_image=Image.open("images/map_dark.png"), size=(16, 16))
connections_taskbar_icon_outline = ctk.CTkImage(light_image=Image.open("images/phone_card_outline.png"),
                                                dark_image=Image.open("images/phone_card_outline_dark.png"), size=(16, 16))
connections_taskbar_icon = ctk.CTkImage(light_image=Image.open("images/phone_card.png"),
                                        dark_image=Image.open("images/phone_card_dark.png"), size=(16, 16))
settings_taskbar_icon_outline = ctk.CTkImage(light_image=Image.open("images/settings_outline.png"),
                                             dark_image=Image.open("images/settings_outline_dark.png"), size=(16, 16))
settings_taskbar_icon = ctk.CTkImage(light_image=Image.open("images/settings.png"),
                                     dark_image=Image.open("images/settings_dark.png"), size=(16, 16))
arrow_left_icon = ctk.CTkImage(light_image=Image.open("images/arrow_left.png"),
                               dark_image=Image.open("images/arrow_left_dark.png"), size=(16, 16))
bin_icon = ctk.CTkImage(light_image=Image.open("images/delete.png"),
                        dark_image=Image.open("images/delete_dark.png"), size=(16, 16))
whatsapp_icon = ctk.CTkImage(Image.open("images/whatsapp.png"), size=(25, 25))

guitar_icon = tk.PhotoImage(file="images/guitar.png")
cinema_icon = tk.PhotoImage(file="images/cinema.png")
cooking_icon = tk.PhotoImage(file="images/cooking.png")
writing_icon = tk.PhotoImage(file="images/writing.png")
homework_icon = tk.PhotoImage(file="images/homework.png")
dance_icon = tk.PhotoImage(file="images/dance.png")

playing_guitar_image = ctk.CTkImage(Image.open("images/playing_guitar.jpg"), size=(350, 100))
going_to_cinema_image = ctk.CTkImage(Image.open("images/going_to_cinema.jpg"), size=(350, 100))
cooking_image = ctk.CTkImage(Image.open("images/cooking.jpg"), size=(350, 100))
creative_writing_image = ctk.CTkImage(Image.open("images/creative_writing.jpg"), size=(350, 100))
doing_school_work_together_image = ctk.CTkImage(Image.open("images/doing_school_work_together.jpg"), size=(350, 100))
social_dancing_image = ctk.CTkImage(Image.open("images/social_dancing.jpg"), size=(350, 100))

playing_guitar_square_image = ctk.CTkImage(Image.open("images/playing_guitar_box.jpg"), size=(100, 100))
going_to_cinema_square_image = ctk.CTkImage(Image.open("images/going_to_cinema_box.jpg"), size=(100, 100))
cooking_square_image = ctk.CTkImage(Image.open("images/cooking_box.jpg"), size=(100, 100))
creative_writing_square_image = ctk.CTkImage(Image.open("images/creative_writing_box.jpg"), size=(100, 100))
doing_school_work_together_square_image = ctk.CTkImage(Image.open("images/doing_school_work_together_box.jpg"), size=(100, 100))
social_dancing_square_image = ctk.CTkImage(Image.open("images/social_dancing_box.jpg"), size=(100, 100))

# define color palette
background_color = ("#ded9e0","#121212")
standard_button_color = ("#4F378B", "#c38fff")
standard_button_hover_color = "#6945c4"
standard_button_text_color = ("#ebebeb", "#0d0911")
standard_label_text_color = ("#4F378B","#e2e2e2")
box_color = ("#fef7ff", "#1e1e1e")
box_selected_color = ("#e8def7", "#2e2e2e")
box_hover_color = ("#a193a3", "#383838")
card_color = ("#fef7ff", "#2e2e2e")
delete_color = ("#d11a2a")

# define fonts styles
heading_1 = ("Roboto", 20)
heading_2 = ("Roboto", 18)
heading_3_bold = ("Roboto Black", 16)
heading_4 = ("Roboto", 14)
heading_4_medium = ("Roboto Medium", 14)
normal_text = ("Roboto", 12)

# load the current database of users (used in login and registration functions)
usernames = list(pd.read_csv("data/users_data.csv").username)

# define a function which will simply clean the previous page's widgets
def destroy_previous_widgets():
    # for every active widget of the window
    for i in window.winfo_children():
        # destroy the widget
        i.destroy()

# define a function which will display the bottom navigation bar based on which page is currently viewed
def bottom_navigation_bar(current_page_frame, number_of_rows):
    # if the current page frame is Activities (home page), then load the variable containing the home page frame
    if current_page_frame == "home_page_frame":
        page_frame = home_page_frame
    # if the current page frame is Map page, then load the variable containing the Map page frame
    elif current_page_frame == "map_page_frame":
        page_frame = map_page_frame
    # if the current page frame is Connections page, then load the variable containing the Connections page frame
    elif current_page_frame == "connections_page_frame":
        page_frame = connections_page_frame
    # if the current page frame is Settings page, then load the variable containing the Settings page frame
    elif current_page_frame == "settings_page_frame":
        page_frame = settings_page_frame

    # create and place the Activities (homepage) button to the grid structure based on the current page's number of rows
    activities_button = ctk.CTkButton(page_frame,
                                      text="Activities",
                                      text_color=standard_label_text_color,
                                      image=activities_taskbar_icon_outline,
                                      fg_color=box_color,
                                      hover_color=box_hover_color,
                                      command=home_page,
                                      width=10,
                                      compound="top")
    activities_button.grid(row=number_of_rows, column=0, sticky=tk.NSEW)

    # create and place the Map button to the grid structure based on the current page's number of rows
    map_button = ctk.CTkButton(page_frame,
                               text="Map",
                               text_color=standard_label_text_color,
                               image=map_taskbar_icon_outline,
                               fg_color=box_color,
                               hover_color=box_hover_color,
                               command=map_page,
                               width=10,
                               compound="top")
    map_button.grid(row=number_of_rows, column=1, sticky=tk.NSEW)

    # create and place the Connections button to the grid structure based on the current page's number of rows
    connections_button = ctk.CTkButton(page_frame,
                                       text="Connections",
                                       text_color=standard_label_text_color,
                                       image=connections_taskbar_icon_outline,
                                       fg_color=box_color,
                                       hover_color=box_hover_color,
                                       command=connections_page,
                                       width=10,
                                       compound="top")
    connections_button.grid(row=number_of_rows, column=2, sticky=tk.NSEW)

    # create and place the Settings button to the grid structure based on the current page's number of rows
    settings_button = ctk.CTkButton(page_frame,
                                    text="Settings",
                                    text_color=standard_label_text_color,
                                    image=settings_taskbar_icon_outline,
                                    fg_color=box_color,
                                    hover_color=box_hover_color,
                                    command=settings_page_account,
                                    width=10,
                                    compound="top")
    settings_button.grid(row=number_of_rows, column=3, sticky=tk.NSEW)

    # if the current page is Activities (home page)
    if current_page_frame == "home_page_frame":
        # highlight the Activities button and disable the command to go to this page and hover effect (redundant)
        activities_button.configure(image=activities_taskbar_icon,
                                    fg_color=box_selected_color,
                                    hover="disabled",
                                    command=None)
    # if the current page is Map
    elif current_page_frame == "map_page_frame":
        # highlight the Map button and disable the command to go to this page and hover effect (redundant)
        map_button.configure(image=map_taskbar_icon,
                             fg_color=box_selected_color,
                             hover="disabled",
                             command=None)
    # if the current page is Connections
    elif current_page_frame == "connections_page_frame":
        # highlight the Connections button and disable the command to go to this page and hover effect (redundant)
        connections_button.configure(image=connections_taskbar_icon,
                                     fg_color=box_selected_color,
                                     hover="disabled",
                                     command=None)
    # if the current page is Settings
    elif current_page_frame == "settings_page_frame":
        # highlight the Settings button and disable the command to go to this page and hover effect (redundant)
        settings_button.configure(image=settings_taskbar_icon,
                                  fg_color=box_selected_color,
                                  hover="disabled",
                                  command=None)

# define the "App settings and info" tab of the Settings page
def settings_page_app():
    # make the frame available for the function bottom_navigation_bar
    # (to display the bottom navigation bar on this page)
    global settings_page_frame

    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the Settings page
    settings_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the Settings page frame to the window
    settings_page_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the home page
    for i in range(20):
        settings_page_frame.rowconfigure(i, weight=1)
    for i in range(4):
        settings_page_frame.columnconfigure(i, weight=1)

    # display the bottom_navigation_bar by passing the home page_frame
    # and same number of rows as defined in the grid structure
    bottom_navigation_bar("settings_page_frame", 20)

    # define and place the heading to the grid
    upper_bar = ctk.CTkLabel(settings_page_frame, text=" Your settings",
                             text_color=standard_label_text_color,
                             font=heading_4,
                             image=settings_taskbar_icon_outline,
                             fg_color=box_color,
                             height=50,
                             compound="left")
    upper_bar.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

    # account settings button
    account_settings_button = ctk.CTkButton(settings_page_frame,
                                            text="Account settings",
                                            text_color=standard_label_text_color,
                                            hover_color=box_hover_color,
                                            fg_color=box_color,
                                            command=settings_page_account)
    account_settings_button.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

    # app settings button
    app_settings_button = ctk.CTkButton(settings_page_frame,
                                        text="App settings and info",
                                        text_color=standard_label_text_color,
                                        fg_color=box_selected_color,
                                        hover_color=box_hover_color,
                                        hover="disabled",
                                        command=None)
    app_settings_button.grid(row=1, column=2, columnspan=2, sticky=tk.NSEW)

    # read the csv file with user data to work with the dark mode information
    user_database = pd.read_csv("data/users_data.csv")
    # set usernames as the index
    user_database.set_index("username", inplace=True)

    # when the user clicks on the dark mode toggle
    def switch_dark_mode():
        # if the toggle is enabled
        if switch_dark_mode_variable.get() == "Yes":
            # write down to the user's data that they enabled dark mode
            user_database.loc[current_username, "dark_mode"] = "Yes"
            # update the csv file
            user_database.to_csv('data/users_data.csv')
            # set the appearance mode to dark mode
            ctk.set_appearance_mode("dark")
        # if the toggle is disabled
        else:
            # write down to the user's data that they disabled dark mode
            user_database.loc[current_username, "dark_mode"] = "No"
            # update the csv file
            user_database.to_csv('data/users_data.csv')
            # set the appearance mode to light mode
            ctk.set_appearance_mode("light")

    switch_dark_mode_variable = ctk.StringVar(value=user_database.loc[current_username, "dark_mode"])
    switch_dark_mode_toggle = ctk.CTkSwitch(settings_page_frame,
                                            text="Dark mode",
                                            progress_color=standard_button_color,
                                            variable=switch_dark_mode_variable,
                                            onvalue="Yes",
                                            offvalue="No",
                                            command=switch_dark_mode)
    switch_dark_mode_toggle.grid(row=4, column=1, columnspan=2)

# define a function which will update the user data after user changes them
# on the Settings page, Account section and saves changes
def update_settings():
    # check if the user inputted at least one information to change
    if ((len(activity1_change_value.get()) == 0 and len(activity2_change_value.get()) == 0
         and len(looking_for_change_value) == 0 and len(password_change_entry.get()) == 0)):
        # if not, remind them they have to fill something to change the settings
        tk.messagebox.showwarning("Warning", "Please fill at least one field to update your settings.")
    # if they changed at least one information, save those changes to the csv file
    else:
        # read the csv file with user data
        user_database = pd.read_csv("data/users_data.csv")
        # set usernames as the index
        user_database.set_index("username", inplace=True)

        # if the user did not change their first preferred activity
        if len(activity1_change_value.get()) == 0:
            # skip the update of this parameter
            pass
        # if the user changed their first preferred activity
        else:
            # check if this activity is not already selected
            if (activity1_change_value.get() == user_database.loc[current_username, "activity1"]
                    or activity1_change_value.get() == user_database.loc[current_username, "activity2"]):
                # if yes, remind user to select new activity type
                tk.messagebox.showwarning("Warning", "Activity you wanted to enter for the first "
                                                     "preference is already selected. To make a change, select "
                                                     "a new one (which is not in your first or "
                                                     "second preference already).")
            # if no
            else:
                # change the activity1 preference in the row of the current user
                user_database.loc[current_username, "activity1"] = activity1_change_value.get()
                # update the csv file
                user_database.to_csv('data/users_data.csv')
                # inform the user that changes were saved
                tk.messagebox.showinfo("Success", "Your changes were saved.")
                # reload the settings page with new settings
                settings_page_account()

        # if the user did not change their second preferred activity
        if len(activity2_change_value.get()) == 0:
            pass
        # if the user changed their second preferred activity
        else:
            # check if this activity is not already selected
            if (activity2_change_value.get() == user_database.loc[current_username, "activity1"]
                    or activity1_change_value.get() == user_database.loc[current_username, "activity2"]):
                # if yes, remind user to select new activity type
                tk.messagebox.showwarning("Warning","Activity you wanted to enter for the second preference "
                                                    "is already selected. To make a change, select a new one "
                                                    "(which is not in your first or second preference already).")
            # if no
            else:
                # change the activity2 preference in the row of the current user
                user_database.loc[current_username, "activity2"] = activity2_change_value.get()
                # update the csv file
                user_database.to_csv('data/users_data.csv')
                # inform the user that changes were saved
                tk.messagebox.showinfo("Success", "Your changes were saved.")
                # reload the settings page with new settings
                settings_page_account()

        # if the user did not change their preference regarding individual/group
        if len(looking_for_change_value) == 0:
            pass
        # if the user changed their preference regarding individual/group
        else:
            # change the individual/group preference in the row of the current user
            user_database.loc[current_username, "looking_for"] = looking_for_change_value
            # update the csv file
            user_database.to_csv('data/users_data.csv')
            # inform the user that changes were saved
            tk.messagebox.showinfo("Success", "Your changes were saved.")
            # reload the settings page with new settings
            settings_page_account()

        # if the user did not change their password
        if len(password_change_entry.get()) == 0:
            pass
        # if the user changed their password
        else:
            # define numbers for checking the new password's strength
            numbers = "0123456789"
            # define what counts as special characters for checking the password strength
            special_characters = "!@#$%^&*()-+?_=,<>/"

            # if the new password is shorter than 6 characters
            if len(password_change_entry.get()) < 6:
                # display desktop warning that it must be longer
                tk.messagebox.showwarning("Warning",
                                          "Password must be at least 6 characters long.")
            # if the new password has at least 6 characters
            else:
                # check if the new password contains at least one number
                if any(c in numbers for c in password_change_entry.get()):
                    # if so, check if the new password contains at least one special character
                    if any(c in special_characters for c in password_change_entry.get()):
                        # change the password in the row of the current user
                        user_database.loc[current_username, "password"] = password_change_entry.get()
                        # update the csv file
                        user_database.to_csv('data/users_data.csv')
                        # inform the user that changes were saved
                        tk.messagebox.showinfo("Success", "Your changes were saved.")
                        # reload the settings page with new settings
                        settings_page_account()
                    # if the password does not contain at least one special character, remind the user
                    else:
                        # display desktop warning
                        tk.messagebox.showwarning("Warning",
                                                  "Username must contain at least one special character.")
                # if the password does not contain at least one number, remind the user
                else:
                    # display desktop warning
                    tk.messagebox.showwarning("Warning",
                                              "Username must contain at least one number.")


# define the "Account settings" tab of the Settings page
def settings_page_account():
    # make the frame available for the function bottom_navigation_bar (to display the bottom navigation bar on this page)
    # make variables available for the function update_settings
    global settings_page_frame, activity1_change_value, activity2_change_value, looking_for_change_value,\
        password_change_entry, looking_for_change_checkbox_value, switch_dark_mode_variable

    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the Settings page
    settings_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the Settings page
    settings_page_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the Settings page
    for i in range(20):
        settings_page_frame.rowconfigure(i, weight=1)
    for i in range(4):
        settings_page_frame.columnconfigure(i, weight=1)

    # display the bottom navigation bar by passing the Settings page frame and same number of rows
    # as defined in the grid structure
    bottom_navigation_bar("settings_page_frame",20)

    # define and place the heading to the grid
    upper_bar = ctk.CTkLabel(settings_page_frame,
                             text=" Your settings",
                             text_color=standard_label_text_color,
                             font=heading_4,
                             image=settings_taskbar_icon_outline,
                             fg_color=box_color,
                             height=50,
                             compound="left")
    upper_bar.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

    # account settings button
    account_settings_button = ctk.CTkButton(settings_page_frame,
                                            text="Account settings",
                                            text_color=standard_label_text_color,
                                            fg_color=box_selected_color,
                                            hover_color=box_hover_color,
                                            hover="disabled",
                                            command=None)
    account_settings_button.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)

    # app settings button
    app_settings_button = ctk.CTkButton(settings_page_frame,
                                        text="App settings and info",
                                        text_color=standard_label_text_color,
                                        fg_color=box_color,
                                        hover_color=box_hover_color,
                                        command=settings_page_app)
    app_settings_button.grid(row=1, column=2, columnspan=2, sticky=tk.NSEW)

    # read the csv file with user data to show current settings of activities
    # preferences and in looking for individual/group
    user_database = pd.read_csv("data/users_data.csv")
    # set usernames as the index
    user_database.set_index("username", inplace=True)

    # description explaining the page's functionality
    settings_page_description = ctk.CTkLabel(settings_page_frame,
                                             text="Here you can change your settings.\nOnly fill those fields you "
                                                  "want to change\nand click Save changes.",
                                             text_color=standard_label_text_color,
                                             font=heading_4,
                                             fg_color=background_color)
    settings_page_description.grid(row=4, column=0, columnspan=4)

    # place label and dropdown for new preferred activity 1
    activity1_change_label = ctk.CTkLabel(settings_page_frame,
                                          text=f"What is your new first preferred activity?\nCurrent activity: "
                                               f"{user_database.loc[current_username, "activity1"]}",
                                          text_color=standard_label_text_color,
                                          font=normal_text,
                                          fg_color=background_color)
    activity1_change_label.grid(row=5, column=0, columnspan=4)
    # variable which will store the selection of new activity 1
    activity1_change_value = tk.StringVar()
    activity1_change_dropdown = ctk.CTkComboBox(settings_page_frame,
                                                values=["Playing guitar", "Going to cinema", "Cooking", "Creative writing",
                                                        "Doing school work together", "Social dancing"],
                                                font=normal_text,
                                                dropdown_font=normal_text,
                                                justify="center",
                                                variable=activity1_change_value,
                                                state="readonly",
                                                width=200)
    activity1_change_dropdown.grid(row=6, column=0, columnspan=4)

    # place label and dropdown for new preferred activity 2
    activity2_change_label = ctk.CTkLabel(settings_page_frame,
                                          text=f"What is your new second preferred activity?\nCurrent activity: "
                                               f"{user_database.loc[current_username, "activity2"]}",
                                          text_color=standard_label_text_color,
                                          font=normal_text,
                                          fg_color=background_color)
    activity2_change_label.grid(row=7, column=0, columnspan=4)
    # variable which will store the selection of new activity 2
    activity2_change_value = tk.StringVar()
    activity2_change_dropdown = ctk.CTkComboBox(settings_page_frame,
                                                values=["Playing guitar", "Going to cinema", "Cooking",
                                                        "Creative writing", "Doing school work together", "Social dancing"],
                                                font=normal_text,
                                                dropdown_font=normal_text,
                                                justify="center",
                                                variable=activity2_change_value,
                                                state="readonly",
                                                width=200)
    activity2_change_dropdown.grid(row=8, column=0, columnspan=4)

    # assign no value to individual/group preference variable if the user did not interact with the checkbox at all
    # this just ensures that the checkbox will be treated as not checked by default
    looking_for_change_value = ""

    # when a checkbox in the individual/group preference is clicked
    def user_group_preference():
        global looking_for_change_checkbox_value, looking_for_change_value
        # if the user checked they are looking for group now
        if looking_for_change_checkbox_value.get() == "checked group":
            # write it down for later
            looking_for_change_value = "Group of people"
        # if the user did not check they are looking for group now
        elif looking_for_change_checkbox_value.get() == "unchecked group":
            # write it down for later
            looking_for_change_value = ""
        # if the user checked they are looking for individual now
        elif looking_for_change_checkbox_value.get() == "checked individual":
            # write it down for later
            looking_for_change_value = "Another person"
        # if the user did not check they are looking for individual now
        else:
            # write it down for later
            looking_for_change_value = ""

    # if the user's current preference is another person
    if user_database.loc[current_username, "looking_for"] == "Another person":
        # place label and dropdown asking if the user is looking for a group of people now
        looking_for_change_label = ctk.CTkLabel(settings_page_frame,
                                         text="Are you now looking for a group of people?",
                                         text_color=standard_label_text_color, fg_color=background_color,
                                                font=normal_text)
        looking_for_change_label.grid(row=9, column=0, columnspan=4)
        # variable which will store the value of the checkbox, the default value is unchecked
        looking_for_change_checkbox_value = ctk.StringVar(value="unchecked group")
        # checkbox for whether the user is looking for a group now
        checkbox_looking_for_group = ctk.CTkCheckBox(settings_page_frame,
                                                     text="Yes, I am looking for a group now.",
                                                     fg_color=standard_button_color,
                                                     hover_color=standard_button_hover_color,
                                                     variable=looking_for_change_checkbox_value,
                                                     onvalue="checked group",
                                                     offvalue="unchecked group",
                                                     command=user_group_preference)
        checkbox_looking_for_group.grid(row=10, column=0, columnspan=4)
    # if the user's current preference is a group of people
    elif user_database.loc[current_username, "looking_for"] == "Group of people":
        # place label and dropdown asking if the user is looking for an individual now
        looking_for_change_label = ctk.CTkLabel(settings_page_frame,
                                                text="Are you now looking for another person?",
                                                text_color=standard_label_text_color,
                                                font=normal_text,
                                                fg_color=background_color)
        looking_for_change_label.grid(row=9, column=0, columnspan=4)
        # variable which will store the value of the checkbox, the default value is unchecked
        looking_for_change_checkbox_value = ctk.StringVar(value="unchecked individual")
        # checkbox for whether the user iss looking for another person now
        checkbox_looking_for_individual = ctk.CTkCheckBox(settings_page_frame,
                                                          text="Yes, I am looking for another person now.",
                                                          fg_color=standard_button_color,
                                                          hover_color=standard_button_hover_color,
                                                          variable=looking_for_change_checkbox_value,
                                                          onvalue="checked individual",
                                                          offvalue="unchecked individual",
                                                          command=user_group_preference)
        checkbox_looking_for_individual.grid(row=10, column=0, columnspan=4)

    # place label and entry box for password change
    password_change_label = ctk.CTkLabel(settings_page_frame,
                                         text="What should be your new password?",
                                         text_color=standard_label_text_color,
                                         font=normal_text,
                                         fg_color=background_color)
    password_change_label.grid(row=11, column=0, columnspan=4)

    # description detailing the password requirements
    password_requirements = ctk.CTkLabel(settings_page_frame,
                                         text="A password must be at least 6 characters long\nand contain 1 number "
                                              "and 1 special character.",
                                         text_color=standard_label_text_color,
                                         font=normal_text,
                                         fg_color=background_color)
    password_requirements.grid(row=12, column=0, columnspan=4)

    # define a label which will store the user's new password
    password_change_entry = tk.StringVar()
    password_change_entry_box = ctk.CTkEntry(settings_page_frame,
                                             textvariable=password_change_entry,
                                             show="*", # "show" will hide the characters and display only asterisk
                                             width=250)
    password_change_entry_box.grid(row=13, column=0, columnspan=4)

    # save changes button
    save_changes_button = ctk.CTkButton(settings_page_frame,
                                        text="Save changes",
                                        text_color=standard_button_text_color,
                                        fg_color=standard_button_color,
                                        hover_color=standard_button_hover_color,
                                        command=update_settings)
    save_changes_button.grid(row=15, column=0, columnspan=4)

    # log out button
    log_out_button = ctk.CTkButton(settings_page_frame,
                                   text="Log out",
                                   text_color=standard_label_text_color,
                                   hover_color=box_hover_color,
                                   fg_color=box_color,
                                   command=welcome_page)
    log_out_button.grid(row=17, column=0, columnspan=4)

# define a function for adding activity contact to Connections page
def add_connection(unique_activity_identifier, source_page):
    # read the csv file with user data
    user_database = pd.read_csv("data/users_data.csv")
    # set usernames as the index
    user_database.set_index("username", inplace=True)

    # load the current Connections of the user
    current_user_connections = user_database.loc[current_username, "connections"]
    # turn the string variable into a list one (it has to be stored as string in Dataframe due to its architecture)
    current_user_connections = eval(current_user_connections)

    # if there are more than three connection saved already
    if len(current_user_connections) > 3:
        # display desktop warning and say that four is the maximum number of connections that can be saved and that one
        # has to be removed
        tk.messagebox.showwarning("Warning", "You cannot have more than 4 connections saved at the same "
                                             "time. To add this one, please remove one first.")
    # if there are at most three connections saved, save this connection
    else:
        # append the activity user wants to add to Connection page to the list
        current_user_connections.append(unique_activity_identifier)
        # turn the list back to a string to store it in a Dataframe and assign it to the user's row
        user_database.loc[current_username, "connections"] = str(current_user_connections)
        # update the csv file with the new connections list
        user_database.to_csv('data/users_data.csv')

        # if the user clicked on an add connection button on Activity details page coming from home, reload that page
        if source_page == "show_activity_details_home":
            # reload the activity details page to update the add/remove connection button
            show_activity_details(unique_activity_identifier, "home page")
        # if the user clicked on an add connection button on Activity details page coming from map, reload that page
        elif source_page == "show_activity_details_map":
            # reload the activity details page to update the add/remove connection button
            show_activity_details(unique_activity_identifier, "map page")

# define a function for removing activity contact from Connections page
def remove_connection(unique_activity_identifier, source_page, activity_name, activity_people):
    # ask user to confirm the removal of the connection
    delete = tk.messagebox.askokcancel(title="Delete connection?", message=f"Do you really want to remove "
                                                                           f"{activity_name} with {activity_people} "
                                                                           f"from your connections? You can always add "
                                                                           f"it later.")

    # if the user confirms the removal of the connection
    if delete == True:
        # read the csv file with user data
        user_database = pd.read_csv("data/users_data.csv")
        # set usernames as the index
        user_database.set_index("username", inplace=True)

        # load the current Connections of the user
        current_user_connections = user_database.loc[current_username, "connections"]
        # turn the string variable into a list one (it has to be stored as string in Dataframe due to its architecture)
        current_user_connections = eval(current_user_connections)
        # remove the activity the user wants to remove from the user's connections
        # (because the user clicked remove connection)
        current_user_connections.remove(unique_activity_identifier)
        # turn the list back to a string to store it in a Dataframe and assign it to the user's row
        user_database.loc[current_username, "connections"] = str(current_user_connections)
        # update the csv file with the new connections list
        user_database.to_csv('data/users_data.csv')

        # if the user clicked on a remove connection button on Activity details page coming from home, reload that page
        if source_page == "show_activity_details_home":
            # reload the activity details page to update the add/remove connection button
            show_activity_details(unique_activity_identifier, "home page")
        # if the user clicked on a remove connection button on Activity details page coming from map, reload that page
        elif source_page == "show_activity_details_map":
            # reload the activity details page to update the add/remove connection button
            show_activity_details(unique_activity_identifier, "map page")
        # if the user clicked on a remove button on Connection page
        else:
            # reload Connections page
            connections_page()
    # if the user does not confirm the removal of the connection
    else:
        # do nothing
        pass

# define a function which creates a connection box that is displayed on the Connections page
def display_connection(connection_nr):
    # define a function which will open WhatsApp of the contact
    def open_contact_on_whatsapp(phone_number):
        # remove the plus and spaces from the phone number (to get a format which WhatsApp URL link uses)
        phone_number = phone_number.replace(" ","")
        phone_number = phone_number.replace("+", "")
        # open the URL which will redirect to WhatsApp
        wb.open(f"https://wa.me/{phone_number}")

    # read the csv file with user data
    user_database = pd.read_csv("data/users_data.csv")
    # set usernames as the index
    user_database.set_index("username", inplace=True)

    # read the csv file with activity data
    activities_database = pd.read_csv("data/activities_data.csv")
    # set unique activity identifiers as the index
    activities_database.set_index("unique_activity_identifier", inplace=True)

    # load the current Connections of the user
    current_user_connections = user_database.loc[current_username, "connections"]
    # turn the string variable into a list one (it has to be stored as string in Dataframe due to its architecture)
    current_user_connections = eval(current_user_connections)

    # get the unique activity identifier of the activity
    unique_activity_identifier_activity = current_user_connections[connection_nr-1]
    # based on that identifier, get the activity's name
    activity_name = activities_database.loc[unique_activity_identifier_activity, "activity_name"]
    # based on that identifier, get the activity's people
    activity_people = activities_database.loc[unique_activity_identifier_activity, "names"]
    # based on that identifier, get the activity's contact details
    activity_contact = activities_database.loc[unique_activity_identifier_activity, "contact"]
    # based on that identifier, get the activity's type
    activity_type = activities_database.loc[unique_activity_identifier_activity, "activity_type"]

    # create a frame for the connection box
    activity_frame = ctk.CTkFrame(connections_page_frame, fg_color=card_color)
    # place the connection box to the grid based on its position (first connection at the top, last at the bottom)
    if connection_nr == 1:
        activity_frame.grid(row=3, column=0, columnspan=4, sticky=tk.NSEW)
    elif connection_nr == 2:
        activity_frame.grid(row=6, column=0, columnspan=4, sticky=tk.NSEW)
    elif connection_nr == 3:
        activity_frame.grid(row=9, column=0, columnspan=4, sticky=tk.NSEW)
    else:
        activity_frame.grid(row=12, column=0, columnspan=4, sticky=tk.NSEW)

    # define the grid layout for the connection box
    for i in range(4):
        activity_frame.rowconfigure(i, weight=1)
    for i in range(3):
        activity_frame.columnconfigure(i, weight=1)

    # select image based on the activity type:
    if activity_type == "Playing guitar":
        activity_square_image = playing_guitar_square_image
    elif activity_type == "Going to cinema":
        activity_square_image = going_to_cinema_square_image
    elif activity_type == "Cooking":
        activity_square_image = cooking_square_image
    elif activity_type == "Creative writing":
        activity_square_image = creative_writing_square_image
    elif activity_type == "Doing school work together":
        activity_square_image = doing_school_work_together_square_image
    elif activity_type == "Social dancing":
        activity_square_image = social_dancing_square_image

    # label which displays the image of the activity
    image_label = ctk.CTkLabel(activity_frame,
                               text=None,
                               image=activity_square_image)

    # label which displays WhatsApp button
    whatsapp_button = ctk.CTkButton(activity_frame,
                                    text=None,
                                    image=whatsapp_icon,
                                    fg_color=card_color,
                                    hover_color=box_hover_color,
                                    command=lambda: open_contact_on_whatsapp(activity_contact),
                                    width=50)

    # text with activity's name
    activity_label = ctk.CTkLabel(activity_frame,
                                  text=f"{activity_name}\nwith {activity_people}",
                                  text_color=standard_label_text_color,
                                  font=heading_4_medium,
                                  justify="left",
                                  fg_color=card_color,
                                  pady=0)

    # text with activity's people
    people_label = ctk.CTkLabel(activity_frame,
                                text=f"Phone number:\n{activity_contact}",
                                text_color=standard_label_text_color,
                                font=heading_4,
                                justify="left",
                                fg_color=card_color,
                                pady=0)

    # delete (bin) button
    remove_connection_button = ctk.CTkButton(activity_frame,
                                             text=None,
                                             image=bin_icon,
                                             fg_color=card_color,
                                             hover_color=delete_color,
                                             command=lambda: remove_connection(unique_activity_identifier_activity,
                                                                               "connections_page",
                                                                               activity_name, activity_people),
                                             width=20)

    # place all items to the connection box
    image_label.grid(row=0, column=0, rowspan=4)
    activity_label.grid(row=0, rowspan=2, column=1, columnspan=3, sticky="w")
    people_label.grid(row=2, rowspan=2, column=1, columnspan=3, sticky="w")
    remove_connection_button.place(relx=1, x=-1, y=2, anchor="ne")
    whatsapp_button.place(relx=1.0, rely=0.9, anchor ='se')

# define the Connections page
def connections_page():
    # make the frame available for the function bottom_navigation_bar (to display the bottom navigation bar on this page)
    global connections_page_frame

    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the Connections page
    connections_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the Connections page to the window
    connections_page_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the Connections page
    for i in range(20):
        connections_page_frame.rowconfigure(i, weight=1)
    for i in range(4):
        connections_page_frame.columnconfigure(i, weight=1)

    # display the bottom navigation bar by passing the Connections page frame
    # and same number of rows as defined in the grid structure
    bottom_navigation_bar("connections_page_frame",20)

    # define and place the heading to the grid
    upper_bar = ctk.CTkLabel(connections_page_frame,
                             text=" Your connections",
                             text_color=standard_label_text_color,
                             font=heading_4,
                             fg_color=box_color,
                             image=connections_taskbar_icon_outline,
                             height=50,
                             compound="left")
    upper_bar.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

    # read the csv file with user data
    user_database = pd.read_csv("data/users_data.csv")
    # set usernames as the index
    user_database.set_index("username", inplace=True)
    # load the current connections of the user
    current_user_connections = user_database.loc[current_username, "connections"]
    # turn the string variable into a list one (it has to be stored as string in Dataframe due to its architecture)
    current_user_connections = eval(current_user_connections)

    # if there is at least one saved activity to display on Connections page
    if len(current_user_connections) > 0:
        # display the connection box of the user's first activity
        display_connection(1)

    # if there are at least two saved activities to display on Connections page
    if len(current_user_connections) >1:
        # display the connection box of the user's second activity
        display_connection(2)

    # if there are at least three saved activities to display on Connections page
    if len(current_user_connections) >2:
        # display the connection box of the user's third activity
        display_connection(3)

    # if there are four saved activities to display on Connections page
    if len(current_user_connections) >3:
        # display the connection box of the user's fourth activity
        display_connection(4)

    # if there are no saved activities to display on Connections page
    if len(current_user_connections) == 0:
        # place label saying there are no connections to display
        no_connections_label = ctk.CTkLabel(connections_page_frame,
                                            text="You have no connections to display.\nYou can add them "
                                                 "in Activity details.",
                                            text_color=standard_label_text_color,
                                            font=normal_text,
                                            fg_color=background_color)
        no_connections_label.grid(row=3, column=0, columnspan=4, sticky=tk.NSEW)

# define a command which will get the unique activity identifier from the marker after the marker is clicked and which
# will run the show_activity_details function
def show_activity_details_from_the_map(marker):
    # pass the data attribute value of the marker (which contains unique activity identifier) to display activity details
    show_activity_details(marker.data,"map page")

# define the Map page
def map_page():
    # make the frame available for the function bottom_navigation_bar
    # (to display the bottom navigation bar on this page)
    # make the activity icons available to the map widget
    global map_page_frame, activity1_icon, activity2_icon

    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the Map page
    map_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the Map page to the window
    map_page_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the Map page
    for i in range(20):
        map_page_frame.rowconfigure(i, weight=1)
    for i in range(4):
        map_page_frame.columnconfigure(i, weight=1)

    # display the bottom navigation bar by passing the Map page frame
    # and same number of rows as defined in the grid structure
    bottom_navigation_bar("map_page_frame",20)

    # define and place the heading to the grid
    upper_bar = ctk.CTkLabel(map_page_frame,
                             text=" Activities near you",
                             text_color=standard_label_text_color,
                             font=heading_4,
                             image=map_taskbar_icon_outline,
                             fg_color=box_color,
                             height=50,
                             compound="left")
    upper_bar.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

    # get user's IP location
    user_location = geocoder.ip("me")

    # read the csv file with activity data
    activities_database = pd.read_csv("data/activities_data.csv")
    # set unique activity identifiers as the index
    activities_database.set_index("unique_activity_identifier", inplace=True)

    # based on activity1_identifier from home page, get the activity1's name
    activity1_name = activities_database.loc[activity1_identifier, "activity_name"]
    # based on activity1_identifier from home page, get the activity1's people
    activity1_people = activities_database.loc[activity1_identifier, "names"]
    # based on activity1_identifier from home page, get the activity1's latitude
    activity1_latitude = activities_database.loc[activity1_identifier, "latitude"]
    # based on activity1_identifier from home page, get the activity1's longitude
    activity1_longitude = activities_database.loc[activity1_identifier, "longitude"]
    # based on activity1_identifier from home page, get the activity1's type
    activity1_activity_type = activities_database.loc[activity1_identifier, "activity_type"]

    # based on activity2_identifier from home page, get the activity2's name
    activity2_name = activities_database.loc[activity2_identifier, "activity_name"]
    # based on activity2_identifier from home page, get the activity2's people
    activity2_people = activities_database.loc[activity2_identifier, "names"]
    # based on activity2_identifier from home page, get the activity2's latitude
    activity2_latitude = activities_database.loc[activity2_identifier, "latitude"]
    # based on activity2_identifier from home page, get the activity2's longitude
    activity2_longitude = activities_database.loc[activity2_identifier, "longitude"]
    # based on activity2_identifier from home page, get the activity2's type
    activity2_activity_type = activities_database.loc[activity2_identifier, "activity_type"]

    # select the right icons for the markers

    # if the activity type is Playing guitar
    if activity1_activity_type == "Playing guitar":
        # select the guitar icon for the activity1 icon
        activity1_icon = guitar_icon
    # if the activity type is Going to cinema
    elif activity1_activity_type == "Going to cinema":
        # select the cinema icon for the activity1 icon
        activity1_icon = cinema_icon
    # if the activity type is Cooking
    elif activity1_activity_type == "Cooking":
        # select the cooking icon for the activity1 icon
        activity1_icon = cooking_icon
    # if the activity type is Creative writing
    elif activity1_activity_type == "Creative writing":
        # select the writing icon for the activity1 icon
        activity1_icon = writing_icon
    # if the activity type is Doing school work together
    elif activity1_activity_type == "Doing school work together":
        # select the homework icon for the activity1 icon
        activity1_icon = homework_icon
    # if the activity type is Social dancing
    else:
        # select the dance icon for the activity1 icon
        activity1_icon = dance_icon

    # if the activity type is Playing guitar
    if activity2_activity_type == "Playing guitar":
        # select the guitar icon for the activity2 icon
        activity2_icon = guitar_icon
    # if the activity type is Going to cinema
    elif activity2_activity_type == "Going to cinema":
        # select the cinema icon for the activity2 icon
        activity2_icon = cinema_icon
    # if the activity type is Cooking
    elif activity2_activity_type == "Cooking":
        # select the cooking icon for the activity2 icon
        activity2_icon = cooking_icon
    # if the activity type is Creative writing
    elif activity2_activity_type == "Creative writing":
        # select the writing icon for the activity2 icon
        activity2_icon = writing_icon
    # if the activity type is Doing school work together
    elif activity2_activity_type == "Doing school work together":
        # select the homework icon for the activity2 icon
        activity2_icon = homework_icon
    # if the activity type is Social dancing
    else:
        # select the dance icon for the activity2 icon
        activity2_icon = dance_icon

    # create map widget
    map_widget = tkmap.TkinterMapView(map_page_frame, width=350, height=600, corner_radius=0)
    # set map widget to the user's location
    map_widget.set_position(user_location.lat, user_location.lng)
    # set activities markers
    activity1_marker = map_widget.set_marker(activity1_latitude,
                                             activity1_longitude,
                                             text=f"{activity1_name} with {activity1_people}",
                                             text_color="navy",
                                             font=heading_4_medium,
                                             icon=activity1_icon,
                                             # this will store the unique activity identifier so once the marker is clicked,
                                             # data attribute can be used to get the activity identifier in the function
                                             # defined in the command parameter
                                             data=activity1_identifier,
                                             command=show_activity_details_from_the_map)
    activity2_marker = map_widget.set_marker(activity2_latitude,
                                             activity2_longitude,
                                             text=f"{activity2_name} with {activity2_people}",
                                             text_color="navy",
                                             font=heading_4_medium,
                                             icon=activity2_icon,
                                             # this will store the unique activity identifier so once the marker is clicked,
                                             # data attribute can be used to get the activity identifier in the function
                                             # defined in the command parameter
                                             data=activity2_identifier,
                                             command=show_activity_details_from_the_map)
    # set map zoom
    map_widget.set_zoom(8)
    # place the map widget to the grid
    map_widget.grid(row=1, column=0, rowspan=15, columnspan=4, sticky=tk.NSEW)

# define a function which will show the details of an activity
def show_activity_details(unique_activity_identifier, source):
    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the activity details page
    activity_details_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the frame for the activity details page to the window
    activity_details_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the activity details page
    for i in range(20):
        activity_details_frame.rowconfigure(i, weight=1)
    for i in range(4):
        activity_details_frame.columnconfigure(i, weight=1)

    # read the csv file with activities data
    activities_database = pd.read_csv("data/activities_data.csv")
    # set unique activity identifiers as the index
    activities_database.set_index("unique_activity_identifier", inplace=True)
    # load the activity name from the activities database
    activity_name = activities_database.loc[unique_activity_identifier, "activity_name"]
    # load the activity's people from the activities database
    activity_people = activities_database.loc[unique_activity_identifier, "names"]
    # load the activity description from the activities database
    activity_description = activities_database.loc[unique_activity_identifier, "description"]
    # load the activity's contact from the activities database
    activity_contact = activities_database.loc[unique_activity_identifier, "contact"]
    # load the activity's latitude from the activities database
    activity_latitude = activities_database.loc[unique_activity_identifier, "latitude"]
    # load the activity's longitude from the activities database
    activity_longitude = activities_database.loc[unique_activity_identifier, "longitude"]
    # load the activity's type from the activities database
    activity_type = activities_database.loc[unique_activity_identifier, "activity_type"]

    # read the csv file with user data
    user_database = pd.read_csv("data/users_data.csv")
    # set usernames as the index
    user_database.set_index("username", inplace=True)
    # load the current Connections of the user
    current_user_connections = user_database.loc[current_username, "connections"]
    # turn the string variable into a list one (it has to be stored as string in Dataframe due to its architecture)
    current_user_connections = eval(current_user_connections)

    # if the user got to the activity details page from the home page
    if source == "home page":
        # set the command which the return button will execute after being clicked to the one which loads the home page
        return_to = home_page
        # set the source page to the home page version so when a user deletes a connection, it will reload the version
        # in which the back button goes to home page
        source_page = "show_activity_details_home"
    # if the user got to the activity details page from the map page
    else:
        # set the command which the return button will execute after being clicked to the one which loads the map page
        return_to = map_page
        # set the source page to the map page version so when a user deletes a connection, it will reload the version
        # in which the back button goes to map page
        source_page = "show_activity_details_map"

    # return button (left arrow)
    return_button = ctk.CTkButton(activity_details_frame,
                                  text=None,
                                  image=arrow_left_icon,
                                  fg_color=background_color,
                                  hover_color=box_hover_color,
                                  command=return_to,
                                  width=50)
    return_button.grid(row=0, rowspan=3, column=0, sticky="w", padx=5)

    # if the user already stored this activity's contact in the Connection page
    if unique_activity_identifier in current_user_connections:
        # add a remove button from Connections page
        remove_connection_button = ctk.CTkButton(activity_details_frame,
                                                 text="Remove connection",
                                                 text_color=standard_button_text_color,
                                                 fg_color=standard_button_color,
                                                 hover_color=standard_button_hover_color,
                                                 command=lambda:remove_connection(unique_activity_identifier,
                                                                                  source_page,
                                                                                  activity_name,
                                                                                  activity_people),
                                                 width=50,
                                                 anchor="w")
        remove_connection_button.grid(row=0, rowspan=3, column=3)
    # if the user has not stored this activity's contact on the Connection page
    else:
        # add an add button to Connections page
        add_connection_button = ctk.CTkButton(activity_details_frame,
                                              text="Add connection",
                                              text_color=standard_button_text_color,
                                              fg_color=standard_button_color,
                                              hover_color=standard_button_hover_color,
                                              command=lambda: add_connection(unique_activity_identifier, source_page),
                                              width=50,
                                              anchor="w")
        add_connection_button.grid(row=0, rowspan=3, column=3)

    # place activity's name
    activity_name_label = ctk.CTkLabel(activity_details_frame,
                                       text=activity_name,
                                       text_color=standard_label_text_color,
                                       font=heading_2,
                                       fg_color=background_color)
    activity_name_label.grid(row=3, column=0, columnspan=4, sticky=tk.SW, padx=20, pady=0)

    # place activity's people
    activity_people_label = ctk.CTkLabel(activity_details_frame,
                                         text=f"with {activity_people}",
                                         text_color=standard_label_text_color,
                                         font=heading_4,
                                         fg_color=background_color)
    activity_people_label.grid(row=4, column=0, columnspan=4, sticky=tk.NW, padx=20, pady=0)

    # select the right icon for the marker on the map based on the activity's type

    # if the activity type is Playing guitar
    if activity_type == "Playing guitar":
        # select the guitar icon for the activity1 icon
        activity_icon = guitar_icon
    # if the activity type is Going to cinema
    elif activity_type == "Going to cinema":
        # select the cinema icon for the activity1 icon
        activity_icon = cinema_icon
    # if the activity type is Cooking
    elif activity_type == "Cooking":
        # select the cooking icon for the activity1 icon
        activity_icon = cooking_icon
    # if the activity type is Creative writing
    elif activity_type == "Creative writing":
        # select the writing icon for the activity1 icon
        activity_icon = writing_icon
    # if the activity type is Doing school work together
    elif activity_type == "Doing school work together":
        # select the homework icon for the activity1 icon
        activity_icon = homework_icon
    # if the activity type is Social dancing
    else:
        # select the dance icon for the activity1 icon
        activity_icon = dance_icon

    # create map widget for activity location
    map_of_activity = tkmap.TkinterMapView(activity_details_frame, width=350, height=250, corner_radius=0)
    # set the location of the map to where the activity's location is
    map_of_activity.set_position(activity_latitude, activity_longitude)
    # add the marker of the activity to the map
    activity_marker = map_of_activity.set_marker(activity_latitude,
                                             activity_longitude,
                                             icon=activity_icon)
    # place the map widget to the page
    map_of_activity.grid(row=5, column=0, rowspan=6, columnspan=4, sticky=tk.NSEW)

    # place label for description of the activity
    description_label = ctk.CTkLabel(activity_details_frame,
                                     text=activity_description,
                                     text_color=standard_label_text_color,
                                     font=heading_4,
                                     justify="left",
                                     wraplength=310,
                                     fg_color=background_color)
    description_label.grid(row=12, rowspan=2, column=0, columnspan=4, sticky=tk.W, padx=20)

    # place label for contact title
    contact_title_label = ctk.CTkLabel(activity_details_frame,
                                       text="Contact",
                                       text_color=standard_label_text_color,
                                       font=heading_3_bold,
                                       fg_color=background_color)
    contact_title_label.grid(row=14, column=0, columnspan=4, sticky=tk.SW, padx=20)

    # place label for contact details (phone number)
    contact_label = ctk.CTkLabel(activity_details_frame,
                                 text="+421 879 5847 5867",
                                 text_color=standard_label_text_color,
                                 font=heading_4,
                                 fg_color=background_color)
    contact_label.grid(row=15, column=0, columnspan=4, sticky=tk.NW, padx=20)

# define a function which will create a new activity in the activities database based on the user-inputted data
def submit_activity(activity_type, activity_name, activity_description, individual_group, organizers_name,
                    activity_latitude, activity_longitude, activity_contact):
    # if not all fields are filled, remind the user to fill them in
    if (len(organizers_name) == 0 or len(activity_latitude) == 0
            or len(activity_longitude) == 0 or len(activity_contact) == 0):
        # display desktop warning
        tk.messagebox.showwarning("Warning", "Please fill in all the details for the activity.")
    # if latitude or longitude fields are not filled properly (there is no dot in them)
    elif "." not in activity_latitude or "." not in activity_longitude:
        # display desktop warning asking user to correct the latitude/longitude input
        tk.messagebox.showwarning("Warning", "Latitude and longitude have to be in the correct format.")
    # if all fields are filled
    else:
        # read the csv file with user data
        user_database = pd.read_csv("data/users_data.csv")
        # set usernames as the index
        user_database.set_index("username", inplace=True)
        # load the current user's status
        current_user_status = user_database.loc[current_username, "status"]

        # if the current user came to Germany based on their registration
        if current_user_status == "I came to Germany":
            # assign their status as Non-German
            status = "Non-German"
        # if the current user is from Germany based on their registration
        else:
            # assign their status as German
            status = "German"

        # generate unique activity identifier based on the current date and time
        identifier = str(datetime.now())
        # remove space, hyphen, colon, and dot from the generated value
        identifier = identifier.replace(" ", "")
        identifier = identifier.replace("-", "")
        identifier = identifier.replace(":", "")
        identifier = identifier.replace(".", "")

        # write new activity data into a dictionary
        activity_data = ({"activity_type": activity_type,
                          "activity_name": activity_name,
                          "group_activity": individual_group,
                          "names": organizers_name,
                          "latitude": activity_latitude,
                          "longitude": activity_longitude,
                          "description": activity_description,
                          "contact": activity_contact,
                          "organizers_status": status,
                          "unique_activity_identifier": identifier
                          })
        # convert the dictionary to a data frame
        new_row_df = pd.DataFrame([activity_data])
        # write the data frame to a .csv file
        new_row_df.to_csv("data/activities_data.csv", index=False, header=False, mode="a")  # mode "a" means append

        # inform the user that the activity was saved and published
        tk.messagebox.showinfo("Success", "Your activity was saved and published.")

        # go back to Activities page (home page)
        home_page()

# define the second page of the add activity process
def add_activity_2(activity_type, activity_name, activity_description, individual_group):
    # get rid of newline characters in the activity description (added because of ctk Textbox widget) as this would
    # cause problems when adding this information to csv file (it would create a new line)
    activity_description = activity_description.strip("\n")

    # if not all fields are filled, remind the user to fill them in
    if (len(activity_type) == 0 or len(activity_name) == 0
            or len(activity_description) == 0 or len( individual_group) == 0):
        # display desktop warning
        tk.messagebox.showwarning("Warning", "Please fill in all the details for the activity.")
    # if all fields are filled
    else:
        # destroy previous widgets
        destroy_previous_widgets()

        # create a frame for the second page of the add activity process
        add_activity_2_frame = ctk.CTkFrame(window, fg_color=background_color)
        # place the second page of the add activity process to the window
        add_activity_2_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

        # define the grid layout for the second page of the add activity process
        for i in range(20):
            add_activity_2_frame.rowconfigure(i, weight=1)
        for i in range(4):
            add_activity_2_frame.columnconfigure(i, weight=1)

        # define and place the heading to the grid
        upper_bar = ctk.CTkLabel(add_activity_2_frame,
                                 text="Add activity (2/2)",
                                 text_color=standard_label_text_color,
                                 font=heading_4,
                                 fg_color=box_color,
                                 height=50)
        upper_bar.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

        # place label and entry box for the name of organizers of the activity
        organizers_name_label = ctk.CTkLabel(add_activity_2_frame,
                                             text="What is your name\n(names if you are multiple people)",
                                             text_color=standard_label_text_color,
                                             font=normal_text,
                                             fg_color=background_color)
        organizers_name_label.grid(row=5, column=1, columnspan=2)
        # variable which will store organizers' names
        organizers_name_value = tk.StringVar()
        organizers_name_box = ctk.CTkEntry(add_activity_2_frame,
                                           textvariable=organizers_name_value,
                                           width=200)
        organizers_name_box.grid(row=6, column=1, columnspan=2)

        # place label and entry box for activity's latitude
        activity_latitude_label = ctk.CTkLabel(add_activity_2_frame,
                                               text="What is the latitude of this activity?",
                                               text_color=standard_label_text_color,
                                               font=normal_text,
                                               fg_color=background_color)
        activity_latitude_label.grid(row=7, column=1, columnspan=2)
        # variable which will store activity's latitude
        activity_latitude_value = tk.StringVar()
        activity_latitude_box = ctk.CTkEntry(add_activity_2_frame,
                                             textvariable=activity_latitude_value,
                                             width=200)
        activity_latitude_box.grid(row=8, column=1, columnspan=2)

        # place label and entry box for activity's longitude
        activity_longitude_label = ctk.CTkLabel(add_activity_2_frame,
                                                text="What is the longitude of this activity?",
                                                text_color=standard_label_text_color,
                                                font=normal_text,
                                                fg_color=background_color)
        activity_longitude_label.grid(row=9, column=1, columnspan=2)
        # variable which will store activity's longitude
        activity_longitude_value = tk.StringVar()
        activity_longitude_box = ctk.CTkEntry(add_activity_2_frame,
                                              textvariable=activity_longitude_value,
                                              width=200)
        activity_longitude_box.grid(row=10, column=1, columnspan=2)

        # place label and entry box for organizers' contact
        activity_contact_label = ctk.CTkLabel(add_activity_2_frame,
                                              text="What is your phone number (international format)?",
                                              text_color=standard_label_text_color,
                                              fg_color=background_color,
                                              font=normal_text)
        activity_contact_label.grid(row=11, column=1, columnspan=2)
        # variable which will store organizers' contact
        activity_contact_value = tk.StringVar()
        activity_contact_box = ctk.CTkEntry(add_activity_2_frame,
                                            textvariable=activity_contact_value,
                                            width=200)
        activity_contact_box.grid(row=12, column=1, columnspan=2)

        # define a function which will display submit activity button based on whether the T&C button has been checked
        def display_submit_button():
            # make the button widget available beyond this function for it to display when ticking the T&C checkbox
            global submit_activity_button
            # if terms and conditions have been checked
            if terms_and_conditions_checked.get() == "checked":
                # show submit activity button
                submit_activity_button = ctk.CTkButton(add_activity_2_frame,
                                                       text="Submit activity",
                                                       text_color=standard_button_text_color,
                                                       fg_color=standard_button_color,
                                                       hover_color=standard_button_hover_color,
                                                       command=lambda: submit_activity(activity_type, activity_name,
                                                                                       activity_description, individual_group,
                                                                                       organizers_name_value.get(),
                                                                                       activity_latitude_value.get(),
                                                                                       activity_longitude_value.get(),
                                                                                       activity_contact_value.get()))
                submit_activity_button.grid(row=17, column=2, columnspan=2)
                # reposition cancel button too (so both buttons are displayed next to each other)
                cancel_button.grid(row=17, column=0, columnspan=2)
            # if terms and conditions have been not checked
            else:
                # do not show submit activity button
                submit_activity_button.grid_remove()
                # reposition cancel button too (so only Cancel button is shown)
                cancel_button.grid(row=17, column=1, columnspan=2)

        # variable which will store the value of the checkbox, the default value is unchecked
        terms_and_conditions_checked = ctk.StringVar(value="unchecked")
        # checkbox for terms and conditions
        checkbox_t_and_c = ctk.CTkCheckBox(add_activity_2_frame,
                                           text="I agree to Terms and Conditions",
                                           fg_color=standard_button_color,
                                           hover_color=standard_button_hover_color,
                                           variable=terms_and_conditions_checked,
                                           onvalue="checked",
                                           offvalue="unchecked",
                                           command=display_submit_button)
        checkbox_t_and_c.grid(row=13, column=1, columnspan=2)

        # cancel button (cancels the creation of new activity and goes back to home page)
        cancel_button = ctk.CTkButton(add_activity_2_frame,
                                      text="Cancel",
                                      text_color=standard_label_text_color,
                                      fg_color=box_color,
                                      hover_color=box_hover_color,
                                      command=home_page)
        cancel_button.grid(row=17, column=1, columnspan=2)

def add_activity():
    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the first page of the add activity process
    add_activity_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the first page of the add activity process to the window
    add_activity_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the first page of the add activity process
    for i in range(20):
        add_activity_frame.rowconfigure(i, weight=1)
    for i in range(4):
        add_activity_frame.columnconfigure(i, weight=1)

    # define and place the heading to the grid
    upper_bar = ctk.CTkLabel(add_activity_frame,
                             text="Add activity (1/2)",
                             text_color=standard_label_text_color,
                             font=heading_4,
                             fg_color=box_color,
                             height=50)
    upper_bar.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

    # place label and dropdown for the type of added activity
    activity_type_label = ctk.CTkLabel(add_activity_frame,
                                       text="What type is your activity?",
                                       text_color=standard_label_text_color,
                                       font=normal_text,
                                       fg_color=background_color)
    activity_type_label.grid(row=3, column=0, columnspan=4)
    # variable which will store the type of activity selected
    activity_type_value = tk.StringVar()
    activity_type_dropdown = ctk.CTkComboBox(add_activity_frame,
                                             values=["Playing guitar", "Going to cinema", "Cooking", "Creative writing",
                                                     "Doing school work together", "Social dancing"],
                                             font=normal_text,
                                             dropdown_font=normal_text,
                                             justify="center",
                                             variable=activity_type_value,
                                             state="readonly",
                                             width=200)
    activity_type_dropdown.grid(row=4, column=0, columnspan=4)

    # place label and entry box for name of added activity
    activity_name_label = ctk.CTkLabel(add_activity_frame,
                                       text="What is the name of your activity?",
                                       text_color=standard_label_text_color,
                                       font=normal_text,
                                       fg_color=background_color)
    activity_name_label.grid(row=5, column=0, columnspan=4)
    # variable which will store the activity's name
    activity_name_value = tk.StringVar()
    activity_name_box = ctk.CTkEntry(add_activity_frame,
                                     textvariable=activity_name_value,
                                     width=200)
    activity_name_box.grid(row=6, column=0, columnspan=4)

    # place label and entry box for description of added activity
    activity_description_label = ctk.CTkLabel(add_activity_frame,
                                              text="Shortly describe your activity",
                                              text_color=standard_label_text_color,
                                              font=normal_text,
                                              fg_color=background_color)
    activity_description_label.grid(row=7, column=0, columnspan=4)
    # textbox which stores the input
    activity_description_box = ctk.CTkTextbox(add_activity_frame)
    activity_description_box.grid(row=8, column=0, columnspan=4)

    # place label and dropdown for individual/group activity selection
    individual_group_label = ctk.CTkLabel(add_activity_frame,
                                          text="Are you an individual or a group",
                                          text_color=standard_label_text_color,
                                          font=normal_text,
                                          fg_color=background_color)
    individual_group_label.grid(row=9, column=0, columnspan=4)
    # variable which will store the selection of individual/group
    individual_group_value = tk.StringVar()
    individual_group_dropdown = ctk.CTkComboBox(add_activity_frame,
                                                values=["Individual", "Group of people"],
                                                font=normal_text,
                                                dropdown_font=normal_text,
                                                justify="center",
                                                variable=individual_group_value,
                                                state="readonly",
                                                width=150,)
    individual_group_dropdown.grid(row=10, column=0, columnspan=4)

    # continue button (goes to the second page of the add new activity process)
    continue_button = ctk.CTkButton(add_activity_frame,
                                    text="Continue",
                                    text_color=standard_button_text_color,
                                    fg_color=standard_button_color,
                                    hover_color=standard_button_hover_color,
                                    command=lambda: add_activity_2(activity_type_value.get(), activity_name_value.get(),
                                                                 activity_description_box.get(0.1, ctk.END),
                                                                 individual_group_value.get()))
    continue_button.grid(row=17, column=2, columnspan=2)

    # cancel button (cancels the creation of new activity and goes back to home page)
    cancel_button = ctk.CTkButton(add_activity_frame,
                                  text="Cancel",
                                  text_color=standard_label_text_color,
                                  fg_color=box_color,
                                  hover_color=box_hover_color,
                                  command=home_page)
    cancel_button.grid(row=17, column=0, columnspan=2)

# define a function which will display the closest activity based on user's preferences and current location
def display_closest_activity(activity_type_preference_number):
    # make these variables globally available as they are later worked with in indented parts of the code
    global distance_latitude, distance_longitude

    # read the csv file with user data
    user_database = pd.read_csv("data/users_data.csv")
    # set usernames as the index
    user_database.set_index("username", inplace=True)

    # load the activity type preference from the user's data (1st/2nd preference is passed to this function from
    # the home page based on whether this activity will be displayed in the first or second preference box)
    user_activity = user_database.loc[current_username, activity_type_preference_number]
    # load the individual/group preference from the user's data
    group_preference = user_database.loc[current_username, "looking_for"]
    # load the user's location latitude
    user_latitude = float(user_database.loc[current_username, "latitude"])
    # load the user's location longitude
    user_longitude = float(user_database.loc[current_username, "longitude"])
    # load the user's status
    user_status = (user_database.loc[current_username, "status"])

    # read the csv file with activities data
    activities_database = pd.read_csv("data/activities_data.csv")
    # select only that activity type which the user selected for their first/second activity preference
    selected_activities = activities_database.loc[activities_database["activity_type"] == user_activity]
    # further select only that individual/group activity type which the user selected
    selected_activities = selected_activities.loc[selected_activities["group_activity"] == group_preference]
    # if the user is non-German
    if user_status == "I came to Germany":
        # further select only German organizers (the purpose of the app is connecting Germans with non-Germans)
        selected_activities = selected_activities.loc[selected_activities["organizers_status"] == "German"]
    # if the user is German
    else:
        # further select only non-German organizers (the purpose of the app is connecting non-Germans with Germans)
        selected_activities = selected_activities.loc[selected_activities["organizers_status"] == "Non-German"]

    # ____ This part will get the two closest activities - one closest in latitude and one closest in longitude

    # get the activity row which has the latitude value closest to the user's latitude
    nearest_latitude = selected_activities.loc[(selected_activities["latitude"] - user_latitude).abs().idxmin()]
    # get the activity row which has the longitude value closest to the user's longitude
    nearest_longitude = selected_activities.loc[(selected_activities["longitude"] - user_longitude).abs().idxmin()]

    # ---- These differentiations prevent the problem of getting negative distance numbers
    # if the closest activity latitude is bigger than the user's latitude
    if nearest_latitude.loc["latitude"] > user_latitude:
        # calculate the distance by subtracting user's latitude (smaller) from the activity latitude (bigger)
        distance_latitude = nearest_latitude.loc["latitude"] - user_latitude
    # if the closest activity latitude is smaller than the user's latitude
    else:
        # calculate the distance by subtracting activity latitude (smaller) from the user's latitude (bigger)
        distance_latitude = user_latitude - nearest_latitude.loc["latitude"]

    # if the closest activity longitude is bigger than the user's longitude
    if nearest_longitude.loc["latitude"] > user_latitude:
        # calculate the distance by subtracting user's longitude (smaller) from the activity longitude (bigger)
        distance_longitude = nearest_longitude.loc["latitude"] - user_longitude
    # if the closest activity longitude is smaller than the user's longitude
    else:
        # calculate the distance by subtracting activity longitude (smaller) from the user's longitude (bigger)
        distance_longitude = user_longitude - nearest_longitude.loc["latitude"]
    # ----

    # ____ This part will find out whether the closest latitude or the closest longitude is nominally closer to the
    #      user
    # if distance in longitudes is bigger than distance in latitudes
    if distance_longitude > distance_latitude:
        # get the unique identifier of the activity
        unique_activity_identifier = nearest_latitude.loc["unique_activity_identifier"]
        # get the activity's name
        activity_name = nearest_latitude.loc["activity_name"]
        # get the activity's organizers' names
        activity_people = nearest_latitude.loc["names"]
        # get the activity's type
        activity_type = nearest_latitude.loc["activity_type"]
    # if distance in latitudes is bigger than distance in longitudes
    else:
        # get the unique identifier of the activity
        unique_activity_identifier = nearest_longitude.loc["unique_activity_identifier"]
        # get the activity's name
        activity_name = nearest_longitude.loc["activity_name"]
        # get the activity's organizers' names
        activity_people = nearest_longitude.loc["names"]
        # get the activity's type
        activity_type = nearest_longitude.loc["activity_type"]

    # display the activity closer to user

    # create a frame for the activity box
    activity_frame = ctk.CTkFrame(home_page_frame, fg_color=card_color)
    activity_frame.grid(row=1, column=0, columnspan=4, sticky=tk.NSEW)

    # define the grid layout for the activity box
    for i in range(2):
        activity_frame.rowconfigure(i, weight=1)
    for i in range(3):
        activity_frame.columnconfigure(i, weight=1)

    # select the image for the activity box based on the activity type
    if activity_type == "Playing guitar":
        activity_image = playing_guitar_image
    elif activity_type == "Going to cinema":
        activity_image = going_to_cinema_image
    elif activity_type == "Cooking":
        activity_image = cooking_image
    elif activity_type == "Creative writing":
        activity_image = creative_writing_image
    elif activity_type == "Doing school work together":
        activity_image = doing_school_work_together_image
    elif activity_type == "Social dancing":
        activity_image = social_dancing_image

    # define label with the activity image
    image_label = ctk.CTkLabel(activity_frame,
                               text=None,
                               image=activity_image)

    # define the label with the activity's name
    activity_label = ctk.CTkLabel(activity_frame,
                                  text=activity_name,
                                  text_color=standard_label_text_color,
                                  font=heading_2,
                                  fg_color=card_color,
                                  pady=0,
                                  anchor="s")

    # define the label with the activity's people
    people_label = ctk.CTkLabel(activity_frame,
                                text=f"with {activity_people}",
                                text_color=standard_label_text_color,
                                font=normal_text,
                                fg_color=card_color,
                                pady=0,
                                anchor="n")

    # show more button (opens Activity details page)
    show_more_button = ctk.CTkButton(activity_frame,
                                     text="Show more",
                                     text_color=standard_button_text_color,
                                     fg_color=standard_button_color,
                                     hover_color=standard_button_hover_color,
                                     command=lambda:show_activity_details(unique_activity_identifier, "home page"),
                                     width=50,
                                     anchor="w")

    # place all these elements to the activity box
    image_label.grid(row=0, column=0, columnspan=4)
    activity_label.grid(row=1, column=0, columnspan=3, sticky="w", padx=20)
    show_more_button.grid(row=1, column=3, rowspan=2, padx=20)
    people_label.grid(row=2, column=0, columnspan=3, sticky="w", padx=20)


    # place the activity box at the top because it is the first preferred activity
    if activity_type_preference_number == "activity1":
        activity_frame.grid(row=2, rowspan=3, column=0, columnspan=4, sticky=tk.NSEW)
    # place the activity box below the first activity box because it is the second preferred activity
    else:
        activity_frame.grid(row=6, rowspan=3, column=0, columnspan=4, sticky=tk.NSEW)

    # return the unique activity identifier to save as a variable for the Map page
    # (for display of the same activities as on the home page)
    return unique_activity_identifier

# define the Activities page (home page)
def home_page():
    # make the frame available for the function bottom_navigation_bar (to display the bottom navigation bar on this page)
    # make the unique activity identifiers available to the Map page
    global home_page_frame, activity1_identifier, activity2_identifier

    # destroy previous widgets
    destroy_previous_widgets()

    # read the csv file with user data to load the app in the right light/dark mode of the user
    user_database = pd.read_csv("data/users_data.csv")
    # set usernames as the index
    user_database.set_index("username", inplace=True)

    # if the user set their appearance mode to dark, show the app like that
    if user_database.loc[current_username, "dark_mode"] == "Yes":
        # set the appearance mode to dark mode
        ctk.set_appearance_mode("dark")
    # if the user set their appearance mode to light, show the app like that
    else:
        # set the appearance mode to light mode
        ctk.set_appearance_mode("light")

    # create a frame for the home page
    home_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the home page to the window
    home_page_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the home page
    for i in range(20):
        home_page_frame.rowconfigure(i, weight=1)
    for i in range(4):
        home_page_frame.columnconfigure(i, weight=1)

    # display the bottom navigation bar by passing the home page frame and same number of rows as defined in the grid structure
    bottom_navigation_bar("home_page_frame",20)

    # define and place the heading to the grid
    upper_bar = ctk.CTkLabel(home_page_frame,
                             text=" Activities for you",
                             text_color=standard_label_text_color,
                             font=heading_4,
                             image=activities_taskbar_icon_outline,
                             fg_color=box_color,
                             height=50,
                             compound="left")
    upper_bar.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

    # place activity one box based on the user's first preferred activity and the closest matching activity
    activity1_identifier = display_closest_activity("activity1")

    # place activity two box based on the user's second preferred activity and the closest matching activity
    activity2_identifier = display_closest_activity("activity2")

    # place label below the activity suggestions boxes informing user that this is the end of suggestions
    end_of_suggestions_label = ctk.CTkLabel(home_page_frame,
                                            text="Those are all suggestions for now.",
                                            text_color=standard_label_text_color,
                                            font=normal_text,
                                            fg_color=background_color)
    end_of_suggestions_label.grid(row=10, column=0, columnspan=4, sticky=tk.NSEW)

    # add activity button
    add_activity_button = ctk.CTkButton(home_page_frame,
                                        text="Create activity",
                                        text_color=standard_button_text_color,
                                        image=plus_icon,
                                        fg_color=standard_button_color,
                                        hover_color=standard_button_hover_color,
                                        command=add_activity,
                                        height=20,
                                        compound="left")
    add_activity_button.grid(row=17, column=2, columnspan=2)

# define a page which will show before the home page after setting the password
# and which will write user data into a csv file
def submit_password(username,name,status,activity1,activity2,looking_for,password):
    # define numbers for checking the password validity
    numbers = "0123456789"
    # define what counts as special characters for checking the password validity
    special_characters = "!@#$%^&*()-+?_=,<>/"

    # if the password is shorter than 6 characters
    if len(password) < 6:
        # display desktop warning that it must be longer
        tk.messagebox.showwarning("Warning",
                                  "Password must be at least 6 characters long.")
    # if the password has at least 6 characters
    else:
        # check if the password contains at least one number
        if any(c in numbers for c in password):
            # if so, check if the password contains at least one special character
            if any(c in special_characters for c in password):
                # if yes, destroy previous widgets
                destroy_previous_widgets()

                # create a frame for the password confirmation page
                password_confirmation_frame = ctk.CTkFrame(window, fg_color=background_color)
                # place the password confirmation page
                password_confirmation_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

                # write now complete user data into a dictionary
                user_data = {
                    "username": username,
                    "password": password,
                    "name": name,
                    "status": status,
                    "activity1": activity1,
                    "activity2": activity2,
                    "looking_for": looking_for,
                    "latitude": geocoder.ip("me").lat,
                    "longitude": geocoder.ip("me").lng,
                    "connections": "[]",
                    "dark_mode": "No"
                }
                # convert the dictionary to a data frame
                user_data_df = pd.DataFrame([user_data])
                # write the data frame to a .csv file at the end using the append method
                user_data_df.to_csv("data/users_data.csv", index=False, header=False, mode="a")  # mode "a" means append

                # define the grid layout for this page
                for i in range(5):
                    password_confirmation_frame.rowconfigure(i, weight=1)
                password_confirmation_frame.columnconfigure(0, weight=1)

                # header welcoming user to the app after registering
                before_home_page_header = ctk.CTkLabel(password_confirmation_frame,
                                                       text=f"All set, {current_username}!", fg_color="#ded9e0",
                                                       text_color=standard_label_text_color, font=heading_1)
                before_home_page_header.grid(row=1, column=0)

                # description explaining what to do next
                before_home_page_description = ctk.CTkLabel(password_confirmation_frame,
                                                            text="Click on the button to enter the home page\nand "
                                                                 "see activities suggestions for you!",
                                                            text_color=standard_label_text_color,
                                                            font=heading_4,
                                                            fg_color="#ded9e0")
                before_home_page_description.grid(row=2, column=0)

                # continue button (leads to home page)
                continue_button = ctk.CTkButton(password_confirmation_frame,
                                                text="Continue",
                                                text_color=standard_button_text_color,
                                                fg_color=standard_button_color,
                                                hover_color=standard_button_hover_color,
                                                command=home_page)
                continue_button.grid(row=3, column=0)
            # if the password does not contain at least one special character, remind the user
            else:
                # display desktop warning
                tk.messagebox.showwarning("Warning",
                                          "Username must contain at least one special character.")
        # if the password does not contain at least one number, remind the user
        else:
            # display desktop warning
            tk.messagebox.showwarning("Warning",
                                      "Username must contain at least one number.")


# define a function for a creating-password screen during registration which will take information user already entered before
def create_password(username,name,status,activity1,activity2,looking_for):

    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the password creation page
    password_setup_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the password creation page to the window
    password_setup_page_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the password creation page
    for i in range(20):
        password_setup_page_frame.rowconfigure(i, weight=1)
    password_setup_page_frame.columnconfigure(0, weight=1)

    # description asking for password
    password_instruction = ctk.CTkLabel(password_setup_page_frame,
                                        text="Please create a password\nso you can log in again later.",
                                        text_color=standard_label_text_color,
                                        font=heading_4,
                                        fg_color=background_color)
    password_instruction.grid(row=9, column=0)

    # define a label which will store the user's password
    password_entry = tk.StringVar()
    # box for entering the password, shows only * when input is given
    password_entry_box = ctk.CTkEntry(password_setup_page_frame,
                                      textvariable=password_entry,
                                      show="*", # "show" will hide the characters
                                      width=250)
    password_entry_box.grid(row=10, column=0)

    # description detailing the password requirements
    password_requirements = ctk.CTkLabel(password_setup_page_frame,
                                         text="A password must be at least 6 characters long\nand contain 1 number "
                                              "and 1 special character.",
                                         text_color=standard_label_text_color,
                                         font=normal_text,
                                         fg_color=background_color)
    password_requirements.grid(row=11, column=0)

    # submit button which also passes the information from the user from the previous page for later storage
    submit_button = ctk.CTkButton(password_setup_page_frame,
                                  text="Submit",
                                  text_color=standard_button_text_color,
                                  fg_color=standard_button_color,
                                  hover_color=standard_button_hover_color,
                                  command=lambda:submit_password(username,
                                                                 name,
                                                                 status,
                                                                 activity1,
                                                                 activity2,
                                                                 looking_for,
                                                                 password_entry.get()
                                                                 )
                                  )
    submit_button.grid(row=12, column=0)

    # inform user that by continuing, their geolocation will be used
    location_info = ctk.CTkLabel(password_setup_page_frame,
                                 text="When you continue, your location\nwill be stored based on your IP address",
                                 text_color=standard_label_text_color,
                                 font=heading_4,
                                 fg_color=background_color)
    location_info.grid(row=19, column=0)

# define a function for completing the registration form
def submit_data():
    global current_username

    # if not all fields are filled, remind the user to fill them in
    if (len(name_entry.get()) == 0 or len(username_entry.get()) == 0 or len(status_value.get()) == 0
            or len(activity1_value.get()) == 0 or len(activity2_value.get()) == 0 or len(looking_for_value.get()) == 0):
        # display desktop warning
        tk.messagebox.showwarning("Warning", "Please fill in all data.")
    # if all fields are filled
    else:
        # if the user chose a username which does not have at least 5 characters
        if len(username_entry.get()) < 5:
            # display desktop warning
            tk.messagebox.showwarning("Warning",
                                      "Username must be at least 5 characters long.")
        # if the username is taken already
        elif username_entry.get() in usernames:
            # display desktop warning
            tk.messagebox.showwarning("Warning", "This username is taken. Please choose "
                                                 "another one and resubmit.")
        # if the user chose the same for both activities preferences
        elif activity1_value.get() == activity2_value.get():
            # display desktop warning
            tk.messagebox.showwarning("Warning",
                                      "You cannot choose the same activity for both first "
                                      "and second preference.")
        # if the username is not taken already and the fields are filled correctly
        else:
            # variable for storing the current user's session
            current_username = username_entry.get()

            # ask the user to create a password and pass the data from the user to the next function for later storage
            create_password(username_entry.get(),
                            name_entry.get(),
                            status_value.get(),
                            activity1_value.get(),
                            activity2_value.get(),
                            looking_for_value.get()
                            )

# define the registration page
def register_page():
    # make the data variables available to other functions too
    global name_entry, username_entry, status_value, activity1_value,\
        activity2_value, looking_for_value, register_page_frame

    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the register page
    register_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the registration page to the window
    register_page_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the registration page
    for i in range(26):
        register_page_frame.rowconfigure(i, weight=1)
    register_page_frame.columnconfigure(0, weight=1)

    # heading welcoming the user to the app
    welcome_page_header = ctk.CTkLabel(register_page_frame,
                                       text="Great to have you here!",
                                       text_color=standard_label_text_color,
                                       font=heading_1,
                                       fg_color=background_color)
    welcome_page_header.grid(row= 4, column= 0)
    # description explaining the registration process
    welcome_page_description = ctk.CTkLabel(register_page_frame,
                                            text="To set up your account,\nwe want to know more about you.",
                                            text_color=standard_label_text_color,
                                            font=heading_4,
                                            fg_color=background_color)
    welcome_page_description.grid(row= 5, column= 0)

    # place label and user input box for name
    name_label = ctk.CTkLabel(register_page_frame,
                              text="Your full name:",
                              text_color=standard_label_text_color,
                              font=normal_text,
                              fg_color=background_color)
    name_label.grid(row=6, column=0)
    # define a label which will store the user's input
    name_entry = tk.StringVar()
    name_entry_box = ctk.CTkEntry(register_page_frame,
                                  textvariable=name_entry,
                                  width=250)
    name_entry_box.grid(row=7, column=0)

    # place label and user input box for username
    username_label = ctk.CTkLabel(register_page_frame,
                                  text="Your username:",
                                  text_color=standard_label_text_color,
                                  font=normal_text,
                                  fg_color=background_color)
    username_label.grid(row=8, column=0)
    # define a label which will store the user's input
    username_entry = tk.StringVar()
    username_entry_box = ctk.CTkEntry(register_page_frame,
                                      textvariable=username_entry,
                                      width=200)
    username_entry_box.grid(row=9, column=0)

    # place label and dropdown for status (German/newcomer)
    status_label = ctk.CTkLabel(register_page_frame,
                                text="Your status:",
                                text_color=standard_label_text_color,
                                font=normal_text,
                                fg_color=background_color)
    status_label.grid(row=10, column=0)
    # variable which will store the selection of status
    status_value = tk.StringVar()
    status_dropdown = ctk.CTkComboBox(register_page_frame,
                                      values=["I am German", "I came to Germany"],
                                      font=normal_text,
                                      dropdown_font=normal_text,
                                      justify="center",
                                      variable=status_value,
                                      state="readonly",
                                      width=150)
    status_dropdown.grid(row=11, column=0)

    # place label and dropdown for preferred activity 1
    activity1_label = ctk.CTkLabel(register_page_frame,
                                   text="What is your first preferred activity?",
                                   text_color=standard_label_text_color,
                                   font=normal_text,
                                   fg_color=background_color)
    activity1_label.grid(row=12, column=0)
    # variable which will store the selection of activity 1
    activity1_value = tk.StringVar()
    activity1_dropdown = ctk.CTkComboBox(register_page_frame,
                                         values=["Playing guitar", "Going to cinema", "Cooking", "Creative writing",
                                                 "Doing school work together", "Social dancing"],
                                         font=normal_text,
                                         dropdown_font=normal_text,
                                         justify="center",
                                         variable= activity1_value,
                                         state="readonly",
                                         width=200)
    activity1_dropdown.grid(row=13, column=0)

    # place label and dropdown for preferred activity 2
    activity2_label = ctk.CTkLabel(register_page_frame,
                                   text="What is your second preferred activity?",
                                   text_color=standard_label_text_color,
                                   font=normal_text,
                                   fg_color=background_color)
    activity2_label.grid(row=14, column=0)
    # variable which will store the selection of activity 2
    activity2_value = tk.StringVar()
    activity2_dropdown = ctk.CTkComboBox(register_page_frame,
                                         values=["Playing guitar", "Going to cinema", "Cooking", "Creative writing",
                                                 "Doing school work together", "Social dancing"],
                                         font=normal_text,
                                         dropdown_font=normal_text,
                                         justify="center",
                                         variable=activity2_value,
                                         state="readonly",
                                         width=200)
    activity2_dropdown.grid(row=15, column=0)

    # place label and dropdown for looking for individuals/group selection
    looking_for_label = ctk.CTkLabel(register_page_frame,
                                     text="Who are you looking for?",
                                     text_color=standard_label_text_color,
                                     font=normal_text,
                                     fg_color=background_color)
    looking_for_label.grid(row=16, column=0)
    # variable which will store the selection of preference for another individual/group
    looking_for_value = tk.StringVar()
    looking_for_dropdown = ctk.CTkComboBox(register_page_frame,
                                           values=["Another person", "Group of people"],
                                           font=normal_text,
                                           dropdown_font=normal_text,
                                           justify="center",
                                           variable=looking_for_value,
                                           state="readonly",
                                           width=150)
    looking_for_dropdown.grid(row=17, column=0)

    # submit button to continue the registration process
    submit_button = ctk.CTkButton(register_page_frame,
                                  text="Submit",
                                  text_color=standard_button_text_color,
                                  fg_color=standard_button_color,
                                  hover_color=standard_button_hover_color,
                                  command=submit_data)
    submit_button.grid(row=18, column=0)

    # add a return button (left arrow) to welcome page if one wants to login instead of registering
    return_button = ctk.CTkButton(register_page_frame,
                                  text=None,
                                  image=arrow_left_icon,
                                  fg_color=background_color,
                                  hover_color=box_hover_color,
                                  command=welcome_page,
                                  width=50)
    return_button.grid(row=0, rowspan=4, column=0, sticky="w", padx=5)

# define a function which logs the user in
def login():
    # make the current username available to all functions for them to properly take the data of the current user
    global current_username

    # if the username exists
    if username_login_entry.get() in usernames:
        # read the csv file with user data
        user_database = pd.read_csv("data/users_data.csv")
        # set usernames as the index
        user_database.set_index("username", inplace=True)
        # check if the entered password is matching the entered username
        if user_database.loc[username_login_entry.get(), "password"] == password_login_entry.get():
            # if it is, set the current username session
            current_username = username_login_entry.get()
            # go to the Activities page (home page)
            home_page()
        # if the password is not matching with the username, ask the user to review the password
        else:
            # display desktop warning
            tk.messagebox.showwarning("Warning", "The password you entered does not match the username. "
                                                 "Please review your login information.")
    # if the username does not exist
    else:
        # display desktop warning
        tk.messagebox.showwarning("Warning", "This username does not exist. Check your login details "
                                             "or register.")

# define the login page
def login_page():
    # make these variables available to the function which is going to log the user in
    global username_login_entry, password_login_entry

    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for this page
    login_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place frame to the window
    login_page_frame.pack(fill="both", expand=1)  # fill "both" means horizontally and vertically

    # define the grid layout for the login page
    for i in range(25):
        login_page_frame.rowconfigure(i, weight=1)
    login_page_frame.columnconfigure(0, weight=1)

    # header welcoming the user back
    welcome_page_header = ctk.CTkLabel(login_page_frame,
                                       text="Welcome back!",
                                       text_color=standard_label_text_color,
                                       font=heading_1,
                                       fg_color=background_color)
    welcome_page_header.grid(row=9, column=0)

    # place instructional label for the user to know what they should do
    instructional_label = ctk.CTkLabel(login_page_frame,
                                       text="Enter your username and password to login.",
                                       text_color=standard_label_text_color,
                                       font=normal_text,
                                       fg_color=background_color)
    instructional_label.grid(row=10, column=0)

    # place label for the username
    username_label = ctk.CTkLabel(login_page_frame,
                                  text="Your username:",
                                  text_color=standard_label_text_color,
                                  font=normal_text,
                                  fg_color=background_color)
    username_label.grid(row=11, column=0)

    # define a variable which will store the username input
    username_login_entry = tk.StringVar()
    # define a box for user's username and place it to the grid
    username_login_entry_box = ctk.CTkEntry(login_page_frame,
                                            textvariable=username_login_entry,
                                            width=200)
    username_login_entry_box.grid(row=12, column=0)

    # place label for the password
    password_label = ctk.CTkLabel(login_page_frame,
                                  text="Your password:",
                                  text_color=standard_label_text_color,
                                  font=normal_text,
                                  fg_color=background_color)
    password_label.grid(row=13, column=0)

    # define a variable which will store the user's password
    password_login_entry = tk.StringVar()
    # place the box for password entry
    password_login_entry_box = ctk.CTkEntry(login_page_frame,
                                            textvariable=password_login_entry,
                                            show="*", # "show" will hide the characters and show only asterisk
                                            width=200)
    password_login_entry_box.grid(row=14, column=0)

    # login button
    login_button = ctk.CTkButton(login_page_frame,
                                 text="Submit",
                                 text_color=standard_button_text_color,
                                 fg_color=standard_button_color,
                                 hover_color=standard_button_hover_color,
                                 command=login)
    login_button.grid(row=15, column=0)

    # add a return button (left arrow) to welcome page if one wants to register instead of login
    return_button = ctk.CTkButton(login_page_frame,
                                  text=None,
                                  image=arrow_left_icon,
                                  fg_color=background_color,
                                  hover_color=box_hover_color,
                                  command=welcome_page,
                                  width=50)
    return_button.grid(row=0, rowspan=2, column=0, sticky="w", padx=5)

# define the first page of the app (welcome page)
def welcome_page():
    # destroy previous widgets
    destroy_previous_widgets()

    # create a frame for the welcome page
    welcome_page_frame = ctk.CTkFrame(window, fg_color=background_color)
    # place the welcome page to the window
    welcome_page_frame.pack(fill="both", expand=1) # fill "both" means horizontally and vertically

    # define the grid layout for the welcome page
    for i in range(15):
        welcome_page_frame.rowconfigure(i, weight=1)
    welcome_page_frame.columnconfigure(0, weight=1)

    # create a label with the sun icon
    sun_icon_label = ctk.CTkLabel(welcome_page_frame,
                                  text=None,
                                  image=sun_icon,
                                  fg_color=background_color)
    # place the icon using the grid method
    sun_icon_label.grid(row= 5, column= 0)

    # heading welcoming the user
    welcome_page_header = ctk.CTkLabel(welcome_page_frame,
                                       text="Welcome to Activities!",
                                       text_color=standard_label_text_color,
                                       font=heading_1,
                                       fg_color=background_color)
    welcome_page_header.grid(row= 6, column= 0)

    # button for existing users to login
    german_button = ctk.CTkButton(welcome_page_frame,
                                  text="Login",
                                  text_color=standard_button_text_color,
                                  fg_color=standard_button_color,
                                  hover_color=standard_button_hover_color,
                                  command=login_page)
    german_button.grid(row= 8, column= 0)
    # button for new users to register
    newcomer_button = ctk.CTkButton(welcome_page_frame,
                                    text="Register",
                                    text_color=standard_button_text_color,
                                    fg_color=standard_button_color,
                                    hover_color=standard_button_hover_color,
                                    command=register_page)
    newcomer_button.grid(row= 9, column= 0)

# display the welcome page as the first page when the user opens the app
welcome_page()

# run the app
window.mainloop()