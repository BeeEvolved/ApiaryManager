# Apiary Management Application

The Apiary Management Application is a Python-based tool that helps beekeepers keep track of their hives, tasks, and hive details. It provides a user-friendly interface for managing apiary-related information.

## Features

- Add, delete, and update hives
- View and manage tasks for each hive
- Sort hives by name
- Save and load data to/from a file

## Usage

To use the ApiaryManager application, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone the repository by running `git clone https://github.com/BeeEvolved/ApiaryManager.git` in your terminal.
3. Navigate to the project directory using `cd repository`.
4. Install the required dependencies by running `pip install -r requirements.txt`.
5. Run the application by executing `python Apiary.py` in your terminal.
6. The application window will open, showing the main interface.

**Adding a Hive:**

- Fill in the Hive Name, Location, Genetics, and Notes fields.
- Click the "Add Hive" button to create a new hive.

**Viewing Hive Details:**

- Select a hive from the list.
- Click the "View Hive Details" button to see more information about the selected hive.

**Sorting Hives by Name:**

- Click the "Sort by Name" button to sort the hives alphabetically by name.

**Saving Data:**

- Click the "Save Data" button to save the apiary data to a file.

**Loading Data:**

- Click the "Load Data" button to load previously saved apiary data from a file.

## Screenshots

![App Screenshot](https://github.com/BeeEvolved/ApiaryManager/blob/main/s1.png)
![App Screenshot](https://github.com/BeeEvolved/ApiaryManager/blob/main/s2.png)
![App Screenshot](https://github.com/BeeEvolved/ApiaryManager/blob/main/s3.png)

Please note that this application uses the Tkinter library for the graphical user interface. If you encounter any issues, make sure you have Tkinter installed and configured properly.

The ApiaryManager application uses the pickle module in Python to save and load data using the pickle serialization format. Here's a detailed explanation of how the app saves data to a pickle file:

1. When you click the "Save Data" button in the application, the `save_data` method of the `ApiaryManager` class is called.
2. Inside the `save_data` method, the `pickle.dump` function is used to serialize the `hives` list (containing all hive data) and save it to a file.
   - The `pickle.dump` function takes two arguments: the object to serialize (`self.hives`) and the file object to write the serialized data.
   - The file object is created using the `open` function with the file path specified.
   - The serialization process converts the object into a byte stream and writes it to the file.
3. The data is now saved in the specified file path as a serialized representation of the `hives` list.

To load previously saved data from a pickle file, the application provides the "Load Data" functionality:

1. When you click the "Load Data" button, the `load_data` method of the `ApiaryManager` class is called.
2. Inside the `load_data` method, the `pickle.load` function is used to deserialize the data from the pickle file and populate the `hives` list.
   - The `pickle.load` function takes the file object as an argument and reads the serialized data from the file.
   - The deserialization process converts the byte stream back into an object, in this case, populating the `hives` list.
3. The `hives` list is now populated with the data from the pickle file, and you can view and manage your apiary using the loaded data.

It's important to note that the application handles exceptions when loading data. If the specified data file is not found (e.g., on the first run), a `FileNotFoundError` is caught, and a warning message is displayed to the user.

Feel free to explore the application and manage your apiary with ease!

