import tkinter as tk
from tkinter import ttk
from Product import Product
from savedData import dictionaryInformation

class DisplayInventoryWindow:
    def __init__(self, parent, inventory):
        self.parent = parent
        self.inventory = inventory

        self.window = tk.Toplevel(parent)
        self.window.title("Inventory")

        # Add a label to display inventory
        self.inventory_label = tk.Label(self.window, text="Inventory:")
        self.inventory_label.pack(padx=20, pady=10)

        # Create a Treeview widget for displaying inventory
        self.tree = ttk.Treeview(self.window, columns=("Product ID", "Product Name", "Price", "Quantity"), show="headings")
        self.tree.pack(fill="both", expand=True)

        # Define column headings
        self.tree.heading("Product ID", text="Product ID")
        self.tree.heading("Product Name", text="Product Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")

        # Set style to add white lines
        self.tree_style = ttk.Style()
        self.tree_style.configure("Treeview", background="white", foreground="black", fieldbackground="white")
        self.tree_style.map("Treeview", background=[('selected', 'blue')])

        # Define custom style for even and odd rows
        self.tree_style.configure("Treeview.Item", background="white", foreground="black", fieldbackground="white")
        self.tree.tag_configure("evenrow", background="white", foreground="black")
        self.tree.tag_configure("oddrow", background="white", foreground="black")

        # Display all inventory items
        self.display_all_inventory()

        
        # Add other buttons for different functionalities
        remove_product_button = ttk.Button(self.mainframe, text='Remove Product', command=self.remove_product)
        remove_product_button.grid(row=1, column=1, pady=10, padx=20, sticky="nsew")

        update_quantity_button = ttk.Button(self.mainframe, text='Update Quantity', command=self.update_quantity)  # Corrected command
        update_quantity_button.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")

    def display_all_inventory(self):
        # Display all inventory items in the Treeview
        for index, product in enumerate(self.inventory):
            # Insert item with white lines
            tags = ('oddrow',) if index % 2 == 0 else ('evenrow',)
            self.tree.insert("", "end", values=(product.get_id(), product.get_name(), product.get_price(), product.get_quantity()), tags=tags)

class UpdateQuantityWindow:
    def __init__(self, parent, inventory):
        self.parent = parent
        self.inventory = inventory

        self.window = tk.Toplevel(parent)
        self.window.title("Update Product Quantity")

        # Set the size of the window
        self.window.geometry('300x200')  # Width x Height

        # Add label and dropdown menu for selecting product ID
        tk.Label(self.window, text="Select Product ID:").pack(pady=5)

        # Create a list of product IDs
        product_ids = [product.get_id() for product in self.inventory]

        # Set the default value of the selected product ID to the first ID in the list
        self.selected_product_id = tk.StringVar(value=product_ids[0])

        # Create a dropdown menu for selecting the product ID
        self.product_id_dropdown = ttk.OptionMenu(self.window, self.selected_product_id, *product_ids)
        self.product_id_dropdown.pack(pady=5)

        # Add label and entry for entering new quantity
        tk.Label(self.window, text="Enter New Quantity:").pack(pady=5)
        self.new_quantity_entry = tk.Entry(self.window)
        self.new_quantity_entry.pack(pady=5)

        # Add button to confirm quantity update
        confirm_button = ttk.Button(self.window, text="Confirm", command=self.confirm_update)
        confirm_button.pack(pady=5)

    def confirm_update(self):
        # Get the product ID and new quantity
        product_id = int(self.selected_product_id.get())
        new_quantity = int(self.new_quantity_entry.get())

        # Update the quantity of the selected product
        for product in self.inventory:
            if product.get_id() == product_id:
                product.set_quantity(new_quantity)
                break

        # Close the window after update
        self.window.destroy()

class RemoveProductWindow:
    def __init__(self, parent, inventory):
        self.parent = parent
        self.inventory = inventory

        self.window = tk.Toplevel(parent)
        self.window.title("Remove Product")

        # Set the size of the window
        self.window.geometry('300x150')  # Width x Height

        # Add label and entry for entering product ID
        tk.Label(self.window, text="Select Product ID to remove:").pack(pady=5)

        # Create a list of product IDs
        product_ids = [product.get_id() for product in self.inventory]

        # Set the default value of the selected product ID to the first ID in the list
        self.selected_product_id = tk.StringVar(value=product_ids[0])

        # Create a dropdown menu for selecting the product ID
        self.product_id_dropdown = ttk.OptionMenu(self.window, self.selected_product_id, *product_ids)
        self.product_id_dropdown.pack(pady=5)

        # Add button to confirm removal
        confirm_button = ttk.Button(self.window, text="Confirm", command=self.confirm_removal)
        confirm_button.pack(pady=5)

    def confirm_removal(self):
        # Get the product ID to remove
        product_id = int(self.selected_product_id.get())

        # Remove the product from the inventory if it exists
        for product in self.inventory:
            if product.get_id() == product_id:
                self.inventory.remove(product)
                break

        # Close the window after removal
        self.window.destroy()

class AddProductWindow:
    def __init__(self, parent, inventory):
        self.parent = parent
        self.inventory = inventory

        self.window = tk.Toplevel(parent)
        self.window.title("Add New Product")

        # Add widgets for adding a new product
        tk.Label(self.window, text="Product ID:").grid(row=0, column=0, sticky="w")
        self.product_id_entry = tk.Entry(self.window)
        self.product_id_entry.grid(row=0, column=1)

        tk.Label(self.window, text="Product Name:").grid(row=1, column=0, sticky="w")
        self.product_name_entry = tk.Entry(self.window)
        self.product_name_entry.grid(row=1, column=1)

        tk.Label(self.window, text="Price:").grid(row=2, column=0, sticky="w")
        self.price_entry = tk.Entry(self.window)
        self.price_entry.grid(row=2, column=1)

        tk.Label(self.window, text="Quantity:").grid(row=3, column=0, sticky="w")
        self.quantity_entry = tk.Entry(self.window)
        self.quantity_entry.grid(row=3, column=1)

        add_button = ttk.Button(self.window, text="Add Product", command=self.add_product)
        add_button.grid(row=4, columnspan=2, pady=10)

    def add_product(self):
        # Get the input values and add the product
        product_id = int(self.product_id_entry.get())
        product_name = self.product_name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())

        # Create a new product object and add it to the inventory
        new_product = Product(product_id, product_name, price, quantity)
        self.inventory.append(new_product)  # Add the product to the inventory list

        # Close the window after adding the product
        self.window.destroy()

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x300')  # Adjusted size to 400x300
        self.root.title('Product Manager')

        # Initialize your application classes here
        self.inventory = []

        # Populate the inventory list with inventory data from savedData.py
        self.populate_inventory()

        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        # Add buttons for different functionalities
        add_product_button = ttk.Button(self.mainframe, text='Add Product', command=self.open_add_product_window)
        add_product_button.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")

        display_inventory_button = ttk.Button(self.mainframe, text='Display Inventory', command=self.display_inventory)
        display_inventory_button.grid(row=0, column=1, pady=10, padx=20, sticky="nsew")

        close_button = ttk.Button(self.mainframe, text='Close Program', command=self.root.destroy)
        close_button.grid(row=4, columnspan=2, pady=10, padx=20, sticky="nsew")

        # Add other buttons for different functionalities
        remove_product_button = ttk.Button(self.mainframe, text='Remove Product', command=self.remove_product)
        remove_product_button.grid(row=1, column=1, pady=10, padx=20, sticky="nsew")

        update_quantity_button = ttk.Button(self.mainframe, text='Update Quantity', command=self.open_update_quantity_window)
        update_quantity_button.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")

        add_to_cart_button = ttk.Button(self.mainframe, text='Add to Cart', command=self.add_to_cart)
        add_to_cart_button.grid(row=2, column=1, pady=10, padx=20, sticky="nsew")

        remove_from_cart_button = ttk.Button(self.mainframe, text='Remove from Cart', command=self.remove_from_cart)
        remove_from_cart_button.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")

        undo_remove_button = ttk.Button(self.mainframe, text='Undo Remove', command=self.undo_remove)
        undo_remove_button.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")

        display_cart_button = ttk.Button(self.mainframe, text='Display Cart', command=self.display_cart)
        display_cart_button.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")

        # Configure row and column weights to center the buttons
        for i in range(5):
            self.mainframe.rowconfigure(i, weight=1)
        for j in range(2):
            self.mainframe.columnconfigure(j, weight=1)

        self.root.mainloop()

    def open_add_product_window(self):
        AddProductWindow(self.root, self.inventory)

    def open_update_quantity_window(self):
        UpdateQuantityWindow(self.root, self.inventory)

    # Define functions for each button
    def populate_inventory(self):
        # Populate the inventory list with inventory data from savedData.py
        for item in dictionaryInformation:
            self.inventory.append(Product(*item))

    def display_inventory(self):
        # Open a new window to display inventory
        DisplayInventoryWindow(self.root, self.inventory)

    def remove_product(self):
        # Open a window to remove a product
        RemoveProductWindow(self.root, self.inventory)

    def add_to_cart(self):
        # Implement the logic for adding a product to the cart
        pass

    def remove_from_cart(self):
        # Implement the logic for removing a product from the cart
        pass

    def undo_remove(self):
        # Implement the logic for undoing a removal from the cart
        pass

    def display_cart(self):
        # Implement the logic for displaying the cart
        pass

# Run the application
if __name__ == '__main__':
    App()