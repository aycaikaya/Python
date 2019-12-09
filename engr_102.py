import re
#from clusters import *
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.filedialog as tkFileDialog
from PIL import Image
from PIL import ImageTk

# Declare district start line
DISTRICT_START = 'Kaynak: YSK'

# Declare constants for the view class
DENDROGRAM_FILE_NAME = 'clusters.jpg'
DISTRICT_BUTTON = 0
POLITICAL_PARTY_BUTTON = 1


# GUI class
class View:

    # Constructor
    def __init__(self, data_center):

        # This variable keeps track of the previously pressed button. If the cluster districts button is
        # pressed previously, refine analysis button will call cluster_districts method of the data center class.
        # If the cluster political parties button is pressed previously, refine analysis button will call
        # cluster_political_parties method from the data center class.
        self.last_button_pressed = 0

        # Save the data center instance to self
        self.data_center = data_center

        # Set the root view
        self.root = Tk()

        # Declare instance variables

        # Window height width for the resolution 1366x768
        self.window_width = 900.0
        self.window_height = 650.0

        # Declare the GUI components that should be accessible from different methods inside this class

        # Declare row_3 and row_4 frames
        self.row_3 = None
        self.row_4 = None

        # Declare districts listbox
        self.districts_listbox = None

        # Declare canvas to show the dendrogram image
        self.canvas = None

        # Declare the image to be displayed in canvas
        self.dendrogram_image = None

        # Declare threshold combobox
        self.threshold_combobox = None

        # Declare input file name
        self.input_filename = ""

        # Define the GUI
        self.define_gui()

    # Shows the view
    def show(self):

        # Set the window title
        self.root.title("Clustering")

        # Hide the root window
        self.root.withdraw()
        self.root.update_idletasks()

        # Calculate width and height of the window
        # The GUI is designed on a system where the resolution is 1366x768,
        # for this program to scale properly in other resolutions, default width and height of the system is multiplied
        # by the following ratios
        width = self.root.winfo_screenwidth() * (self.window_width / 1366)
        height = self.root.winfo_screenheight() * (self.window_height / 768)

        # Calculate the position of the window in order to center it
        x = (self.root.winfo_screenwidth() / 2.0) - (width / 2.0)
        y = (self.root.winfo_screenheight() / 2.0) - (height / 2.0)

        # Apply the calculated geometry
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))

        # Show the root window
        self.root.deiconify()

        # Show window
        Tk.mainloop(self.root)

    # Defines how the user interface will look like
    def define_gui(self):

        # Create and place the label
        label = Label(text='Election Data Analysis Tool v. 1.0', font=("Helvetica", 12, 'bold'), bg='red', fg='white')
        label.grid(row=0, column=0, sticky=EW)

        # Expand the label along the row
        Grid.columnconfigure(self.root, 0, weight=1)

        # Create and place the load data button
        load_election_data_button = Button(text='Load Election Data',
                                           height=2, width=40, command=self.load_election_data_button_pressed)
        load_election_data_button.grid(row=1, column=0, padx=10, pady=10)

        # Create a frame in row 2 so pack() can be used inside of it
        row_2 = Frame(self.root)
        row_2.grid(row=2)

        # Create cluster district button in the frame
        cluster_district_button = Button(row_2, text='Cluster Districts', height=3, width=40,
                                         command=self.cluster_districts_button_pressed)

        # Place the button to the side left of the frame
        cluster_district_button.pack(side=LEFT)

        # Create cluster parties button in the frame
        cluster_parties_button = Button(row_2, text='Cluster Political Parties', height=3, width=40,
                                        command=self.cluster_parties_button_pressed)

        # Place the button to the side right of the frame
        cluster_parties_button.pack(side=RIGHT)

        # Create a frame in row 3 so pack() can be used inside of it
        self.row_3 = row_3 = Frame(self.root)

        # Create and place the X scrollbar of the canvas
        canvas_x_scrollbar = Scrollbar(row_3, orient=HORIZONTAL)
        canvas_x_scrollbar.pack(side=BOTTOM, fill=X)

        # Create and place the Y scrollbar of the canvas
        canvas_y_scrollbar = Scrollbar(row_3, orient=VERTICAL)
        canvas_y_scrollbar.pack(side=RIGHT, fill=Y)

        # Create the canvas which will display the dendrogram image
        self.canvas = canvas = Canvas(row_3, xscrollcommand=canvas_x_scrollbar.set,
                                      yscrollcommand=canvas_y_scrollbar.set, width=770, height=300)

        # Place the canvas inside the frame
        canvas.pack(fill=BOTH, expand=YES)

        # Set up the x and y scrollbars for the canvas
        canvas_x_scrollbar.config(command=canvas.xview)
        canvas_y_scrollbar.config(command=canvas.yview)

        # Create a frame in row 4 so pack() can be used inside of it
        self.row_4 = row_4 = Frame(self.root)

        # Create the districts label
        districts_label = Label(row_4, text='Districts:')
        districts_label.pack(side=LEFT)

        # Create a scrollbar for the districts listbox
        districts_scrollbar = Scrollbar(row_4)

        # Create and place the listbox for districts
        districts_listbox = Listbox(row_4, yscrollcommand=districts_scrollbar.set, height=9, selectmode=EXTENDED)
        districts_listbox.pack(side=LEFT)

        # Save the listbox to the instance variable
        self.districts_listbox = districts_listbox

        # Configure the listbox in order to keep the selected item after the user clicks on elsewhere
        districts_listbox.configure(exportselection=False)

        # Place and set the scrollbar for the districts listbox
        districts_scrollbar.pack(side=LEFT, fill=Y)
        districts_scrollbar.config(command=districts_listbox.yview)

        # Create and place the threshold label
        threshold_label = Label(row_4, text='Threshold:')
        threshold_label.pack(side=LEFT)

        # Create and place the threshold combobox
        threshold_combobox = Combobox(row_4,
                                      values=['0%', '1%', '10%', '20%', '30%', '40%', '50%'], width=6, state="readonly")
        threshold_combobox.pack(side=LEFT)

        # Save the combobox to the instance variable
        self.threshold_combobox = threshold_combobox

        # Set the current element in the combobox as the first element
        threshold_combobox.current(0)

        # Create and place the refine analysis button
        refine_analysis_button = Button(row_4, text='Refine Analysis', height=2, width=40,
                                        command=self.refine_analysis_button_pressed)
        refine_analysis_button.pack(side=LEFT)

    # Method to handle presses to the load election data button
    def load_election_data_button_pressed(self):

        # Get the selected file name from the tkDialog
        self.input_filename = tkFileDialog.askopenfilename(initialdir='/', title='Select file',
                                                           filetypes=(('text files', '*.txt'), ('all files', '*.*')))
        # If the user has selected a file name
        if self.input_filename != '':

            # Parse the file
            self.data_center.parse_input(self.input_filename)

            # Add the parsed districts obtained from the data center to the districts listbox
            for district_name in self.data_center.district_names:
                self.districts_listbox.insert(END, district_name)

    # Method to handle presses to the cluster districts button
    def cluster_districts_button_pressed(self):

        # Set the previously pressed button
        self.last_button_pressed = DISTRICT_BUTTON

        # Clear the selection of the districts listbox
        self.districts_listbox.selection_clear(0, END)

        # Check if there is an input file
        if self.input_filename != '':

            # Try to create a dendrogram
            try:

                # Command the data center to create a dendrogram image of the clustered districts with
                # the selected districts and the threshold
                self.data_center.cluster_districts([], threshold=int(self.threshold_combobox.get()[:-1]))

                # Open the dendrogram image using PIL
                dendrogram_image = Image.open(DENDROGRAM_FILE_NAME)

                # Convert image to the Tkinter loadable format using PhotoImage and save its instance to the view class
                # in order to prevent it from getting garbage collected
                self.dendrogram_image = ImageTk.PhotoImage(dendrogram_image)

                # Load image into the canvas
                self.canvas.create_image(0, 0, image=self.dendrogram_image, anchor='nw')

            # If the selection is not suitable for a dendrogram
            except (ZeroDivisionError, IndexError):

                # Clear the canvas
                self.canvas.delete("all")

            finally:

                # Set up the canvas' scroll region
                self.canvas.config(scrollregion=self.canvas.bbox(ALL))

                # Place analysis components to the root grid
                self.place_analysis_on_grid()

    # Method to handle presses to the cluster parties button
    def cluster_parties_button_pressed(self):

        # Set the previously pressed button
        self.last_button_pressed = POLITICAL_PARTY_BUTTON

        # Clear the selection of the districts listbox
        self.districts_listbox.selection_clear(0, END)

        # Check if there is an input file
        if self.input_filename != '':

            # Try to create a dendrogram
            try:

                # Command the data center to create a dendrogram image of the clustered political parties with
                # the selected districts and the threshold
                self.data_center.cluster_political_parties([], threshold=int(self.threshold_combobox.get()[:-1]))

                # Open the dendrogram image using PIL
                dendrogram_image = Image.open(DENDROGRAM_FILE_NAME)

                # Convert image to the Tkinter loadable format using PhotoImage and save its instance to the view class
                # in order to prevent it from getting garbage collected
                self.dendrogram_image = ImageTk.PhotoImage(dendrogram_image)

                # Load image into the canvas
                self.canvas.create_image(0, 0, image=self.dendrogram_image, anchor='nw')

            # If the selection is not suitable for a dendrogram
            except (ZeroDivisionError, IndexError):

                # Clear the canvas
                self.canvas.delete("all")

            finally:

                # Set up the canvas' scroll region
                self.canvas.config(scrollregion=self.canvas.bbox(ALL))

                # Place analysis components to the root grid
                self.place_analysis_on_grid()

    # Method to handle presses to the refine analysis button
    def refine_analysis_button_pressed(self):

        # Get selected districts from the districts listbox
        selected_districts = [self.data_center.district_names[index] for index in self.districts_listbox.curselection()]

        # Try to create a dendrogram
        try:

            # If the last pressed button is cluster districts
            if self.last_button_pressed == DISTRICT_BUTTON:

                # Command the data center to create a dendrogram image of clustered districts with
                # the selected districts and the threshold
                self.data_center.cluster_districts(selected_districts,
                                                   int(self.threshold_combobox.get()[:-1]))

            # If the last pressed button is cluster political parties
            else:

                # Command the data center to create a dendrogram image of the clustered political parties with
                # the selected districts and the threshold
                self.data_center.cluster_political_parties(selected_districts,
                                                           int(self.threshold_combobox.get()[:-1]))

            # Open the dendrogram image using PIL
            dendrogram_image = Image.open(DENDROGRAM_FILE_NAME)

            # Convert image to the Tkinter loadable format using PhotoImage and save its instance to the view class
            # in order to prevent it from getting garbage collected
            self.dendrogram_image = ImageTk.PhotoImage(dendrogram_image)

            # Load image into the canvas
            self.canvas.create_image(0, 0, image=self.dendrogram_image, anchor='nw')

        # If the selection is not suitable for a dendrogram
        except (ZeroDivisionError, IndexError):

            # Clear the canvas
            self.canvas.delete("all")

        finally:

            # Set up the canvas' scroll region
            self.canvas.config(scrollregion=self.canvas.bbox(ALL))

    # Method to add row_3 and row_4 frames to the root grid
    def place_analysis_on_grid(self):
        self.row_3.grid(row=3)
        self.row_4.grid(row=4)


# District class which holds data about a district
class District:

    # Constructor
    def __init__(self, name):

        # Declare instance variables
        self.name = name
        self._election_results = {}

    # Method to add a political party acronym and vote percentage to the district
    def add_political_party(self, acronym, vote_percentage):

        # Add given values to the election results dictionary
        self._election_results[acronym] = vote_percentage

    # Returns the given political party's vote percentage in this district
    def get_political_party_percentage(self, acronym):

        # Try to get vote percentage of the given political party from the election results of self
        try:
            return self._election_results[acronym]

        # If there is no vote percentage for the given party in this district, return 0
        except KeyError:
            return 0.0


# Political party class which holds data about a political party
class PoliticalParty:

    # Constructor
    def __init__(self, acronym):

        # Declare instance variables
        self.acronym = acronym
        self._election_results = {}
        self.vote_count = 0

    # Method to add a district name and vote percentage to the political party
    def add_district(self, name, vote_percentage, count):

        # Add given values to the election results dictionary
        self._election_results[name] = vote_percentage
        self.vote_count += count

    # Returns the vote percentage of self for the given district
    def get_district_percentage(self, district_name):

        # Try to get vote percentage of the given district from the election results of self
        try:
            return self._election_results[district_name]

        # If there is no vote percentage for the given district in this political party, return 0
        except KeyError:
            return 0.0


# Class to be used as data center for the whole project
class DataCenter:

    # Constructor
    def __init__(self):

        # Declare instance variables
        self.districts = {}
        self.political_parties = {}
        self.district_names = []
        self.political_party_names = []
        self.total_vote_count = 0
        self.political_party_vote_percentages = {}

    # Parses the input file using the given name and populates necessary data in self
    def parse_input(self, txt_filename):

        # While the file is open
        with open(txt_filename, 'r') as txt_file:

            # Get a list of lines excluding line terminators
            lines = [line.rstrip('\n') for line in txt_file]

        # Regular expression to match lines starting with two capital letters
        political_party_expression = re.compile(r'(^[A-Z][A-Z].*)')

        # Declare district name variable
        district_name = ''

        # For each line in the input file
        for i in range(len(lines)):

            # If the line corresponds to a district start
            if DISTRICT_START in lines[i]:

                # Get the district name
                district_name = lines[i+1]

                # Instantiate a district object with the parsed district name and save it to the districts dictionary
                self.districts[district_name] = District(district_name)

            # If the line contains a vote percentage of a political party and the party is not BGMSZ
            elif political_party_expression.search(lines[i]) and 'BGMSZ' not in lines[i]:

                # Split the line by tab character
                split_list = lines[i].split('\t')

                # Get acronym and the percentage and vote count
                acronym = split_list[0]
                percentage = float(split_list[-1][1:])
                count = int(split_list[-2].replace('.', ''))

                # Try to add a district to an instance of a political party stored in the dictionary
                try:
                    self.political_parties[acronym].add_district(district_name, percentage, count)

                # If the political party does not exist in the dictionary
                except KeyError:

                    # Instantiate a political party object with the parsed acronym and save it to the dictionary
                    self.political_parties[acronym] = PoliticalParty(acronym)

                    # Add the parsed district to the created political party object
                    self.political_parties[acronym].add_district(district_name, percentage, count)

                # Add the parsed political party acronym and the vote percentage to the previously parsed district
                self.districts[district_name].add_political_party(acronym, percentage)

            # Add total vote count in the district to total count in self
            elif 'Toplam\t' in lines[i]:
                self.total_vote_count += int(lines[i].split('\t')[-1].replace('.', ''))

        # Create political party names and district names from the dictionary keys
        self.political_party_names = list(self.political_parties.keys())
        self.district_names = sorted(list(self.districts.keys()))

        # For each political party
        for political_party_name in self.political_party_names:

            # Calculate its total vote percentage
            self.political_party_vote_percentages[political_party_name] = \
                (self.political_parties[political_party_name].vote_count / float(self.total_vote_count)) * 100.0

    # Method that clusters districts using the given district list and threshold. This method creates a
    # dendrogram image file to be read into the canvas in view. Throws ZeroDivisionError
    def cluster_districts(self, selected_districts, threshold=0):

        # Assert that dictionaries are filled
        assert self.districts != {} and self.political_parties != {}

        # If no district is selected by the user, cluster all districts
        if not selected_districts:
            selected_districts = self.district_names

        # Filter out political party names using their total vote percentages and the given threshold value
        political_party_names = [political_party for political_party in self.political_party_names
                                 if self.political_party_vote_percentages[political_party] >= threshold]

        # Initialize the matrix to be clustered. Rows correspond to districts, columns correspond to political parties
        cluster_matrix = [[0.0]*len(political_party_names) for i in range(len(selected_districts))]

        # For each row
        for i in range(len(selected_districts)):

            # For each column
            for j in range(len(political_party_names)):

                # Each cell gets filled by the vote percentage of the party j in the district i
                cluster_matrix[i][j] = self.districts[selected_districts[i]]\
                    .get_political_party_percentage(political_party_names[j])

        # Create a hierarchical cluster using euclidean distance
        cluster = hcluster(cluster_matrix, distance=sim_distance)

        # Create the dendrogram image
        drawdendrogram(cluster, selected_districts)

    # Method that clusters political parties using the given district list and threshold. This method creates a
    # dendrogram image file to be read into the canvas in view. Throws ZeroDivisionError
    def cluster_political_parties(self, selected_districts, threshold=0):

        # Assert that dictionaries are filled
        assert self.districts != {} and self.political_parties != {}

        # If no district is selected by the user, cluster all districts
        if not selected_districts:
            selected_districts = self.district_names

        # Filter out political party names using their total vote percentages and the given threshold value
        political_party_names = [political_party for political_party in self.political_party_names
                                 if self.political_party_vote_percentages[political_party] >= threshold]

        # Initialize the matrix to be clustered. Rows correspond to political parties, columns correspond to districts.
        cluster_matrix = [[0.0] * len(selected_districts) for i in range(len(political_party_names))]

        # For each row
        for i in range(len(political_party_names)):

            # For each column
            for j in range(len(selected_districts)):

                # Each cell gets filled by the vote percentage of the party i in the district j
                cluster_matrix[i][j] = self.political_parties[political_party_names[i]] \
                    .get_district_percentage(selected_districts[j])

        # Create a hierarchical cluster using euclidean distance
        cluster = hcluster(cluster_matrix, distance=sim_distance)

        # Create the dendrogram image
        drawdendrogram(cluster, political_party_names)


# Main method
def main():

    # Initialize the data center
    data_center = DataCenter()

    # Initialize and show the GUI
    gui = View(data_center)
    gui.show()


# Execute the main method
if __name__ == "__main__":
    main()

























