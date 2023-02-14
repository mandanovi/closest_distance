import sys
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Closest Distance")

        layout = QVBoxLayout()

        self.label = QLabel("Reference Address:")
        self.reference_address = QLineEdit()
        layout.addWidget(self.label)
        layout.addWidget(self.reference_address)

        self.label = QLabel("Number of Addresses to Compare:")
        self.num_compare_addresses = QLineEdit()
        layout.addWidget(self.label)
        layout.addWidget(self.num_compare_addresses)

        self.entry_list = []
        for i in range(5):
            self.label = QLabel()
            self.label.setText(f"Address {i + 1}:")
            self.entry = QLineEdit()
            layout.addWidget(self.label)
            layout.addWidget(self.entry)
            self.entry_list.append(self.entry)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)
        layout.addWidget(self.calculate_button)

        self.result_label = QLabel("Result will be displayed here.")
        layout.addWidget(self.result_label)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def location_(self, address):
        geolocator = Nominatim(user_agent="Closest_Distance")
        location = geolocator.geocode(address)
        return (location.latitude, location.longitude)

    def get_distance(self, address1, address2):
        first_loc = self.location_(address1)
        second_loc = self.location_(address2)
        return float(geodesic(first_loc, second_loc).miles)

    def calculate(self):
        user_address = self.reference_address.text()
        try:
            count_address = int(self.num_compare_addresses.text())
        except Exception as e:
            self.result_label.setText(str(e))
            return

        my_dict = {}
        my_list = []

        for i in range(count_address):
            compare_address = self.entry_list[i].text()
            try:
                my_dict[compare_address] = self.get_distance(user_address, compare_address)
                my_list.append(self.get_distance(user_address, compare_address))
            except Exception as e:
                self.result_label.setText(f"{user_address} is not able to be checked it's latitude and longitude.")
                return

        print(my_list)

        closest_place = min(my_dict, key=my_dict.get)
        closest_distance = min(my_list)
        farthest_distance = max(my_list)
        farthest_place = max(my_dict, key=my_dict.get)
        result = f"The closest location from reference address: {closest_place} with distance: {closest_distance} miles.\n" \
                 f"The farthest location from reference address: {farthest_place} with distance: {farthest_distance} miles."

        self.result_label.setText(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


## tkinter GUI
# import tkinter as tk
# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
#
#
# def location_(address):
#     geolocator = Nominatim(user_agent="Closest_Distance")
#     location = geolocator.geocode(address)
#     return (location.latitude, location.longitude)
#
#
# def get_distance(address1, address2):
#     first_loc = location_(address1)
#     second_loc = location_(address2)
#     return float(geodesic(first_loc, second_loc).miles)
#
#
# def calculate_distances():
#     try:
#         count_address = int(entry_count.get())
#         my_dict = {}
#         my_list = []
#
#         for i in range(count_address):
#             compare_address = entry_list[i].get()
#             my_dict[compare_address] = get_distance(entry_ref.get(), compare_address)
#             my_list.append(get_distance(entry_ref.get(), compare_address))
#
#         closest_place = min(my_dict, key=my_dict.get)
#         closest_distance = min(my_list)
#         farthest_distance = max(my_list)
#         farthest_place = max(my_dict, key=my_dict.get)
#         result_label.config(text=f"The closest location from reference address: {closest_place} with distance: {round(closest_distance, 1)} miles.\n"
#                            f"The farthest location from reference address: {farthest_place} with distance: {round(farthest_distance, 1)} miles.")
#     except Exception as e:
#         result_label.config(text=str(e))
#
#
# root = tk.Tk()
# root.title("Closest Distance Calculator")
#
# label_ref = tk.Label(root, text="Reference Address:")
# label_ref.grid(row=0, column=0, sticky="W", padx=10, pady=10)
#
# entry_ref = tk.Entry(root)
# entry_ref.grid(row=0, column=1, padx=10, pady=10)
#
# label_count = tk.Label(root, text="Number of Addresses to Compare:")
# label_count.grid(row=1, column=0, sticky="W", padx=10, pady=10)
#
# entry_count = tk.Entry(root)
# entry_count.grid(row=1, column=1, padx=10, pady=10)
#
# entry_list = []
# for i in range(10):
#     label = tk.Label(root, text=f"Address {i + 1}:")
#     label.grid(row=i + 2, column=0, sticky="W", padx=10, pady=10)
#     entry = tk.Entry(root)
#     entry.grid(row=i + 2, column=1, padx=10, pady=10)
#     entry_list.append(entry)
#
# calculate_button = tk.Button(root, text="Calculate Distances", command=calculate_distances)
# calculate_button.grid(row=12, column=0, columnspan=2, pady=10)
#
# result_label = tk.Label(root, text="", justify="left")
# result_label.grid(row=13, column=0, columnspan=2, padx=10, pady=10)
#
# root.mainloop()