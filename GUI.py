import tkinter as tk
from tkinter import ttk, messagebox
from Product import Product
import pickle

# Sample data for dictionaryInformation
dictionaryInformation = [
    (1, "Chocolate Milk", 10.99, 50),
    (2, "Peanut Butter", .99, 30),
    (3, "Cake", 14.49, 40)
]

class RemoveProductWindow:
    def __init__(self, parent, inventory, deleted_product_ids):
        self.parent = parent
        self.inventory = inventory
        self.deleted_product_ids = deleted_product_ids

        self.window = tk.Toplevel(parent)
        self.window.title("Remove Product")

        # Set the size of the window
        self.window.geometry('300x150')  # Width x Height

        # Add label and dropdown menu for selecting product ID
        tk.Label(self.window, text="Select Product ID to remove:").pack(pady=5)

        # Create a set of unique product IDs excluding the deleted ones
        unique_product_ids = set(product.get_id() for product in self.inventory if product.get_id() not in self.deleted_product_ids)

        # Convert the set to a list for dropdown menu options
        product_ids = list(unique_product_ids)

        # Set the default value of the selected product ID to the first ID in the list
        if product_ids:
            self.selected_product_id = tk.StringVar(value=product_ids[0])
        else:
            self.selected_product_id = tk.StringVar(value="No products available")

        # Create a dropdown menu for selecting the product ID
        self.product_id_dropdown = ttk.OptionMenu(self.window, self.selected_product_id, *product_ids)
        self.product_id_dropdown.pack(pady=5)

        # Add button to confirm removal
        confirm_button = ttk.Button(self.window, text="Confirm", command=self.confirm_removal)
        confirm_button.pack(pady=5)

    def confirm_removal(self):
        # Get the product ID to remove
        selected_product_id = self.selected_product_id.get()

        # Check if a valid product ID is selected
        if selected_product_id != 'No products available':
            product_id = int(selected_product_id)

            # Remove the product from the inventory if it exists
            for product in self.inventory:
                if product.get_id() == product_id:
                    self.inventory.remove(product)
                    self.deleted_product_ids.add(product_id)  # Add the deleted product ID to the set
                    break
        else:
            messagebox.showerror("Error", "No products available to remove.")

        # Close the window after removal
        self.window.destroy()

# Other classes and functions remain the same

class App:
    def __init__(self):
        # Initialize other attributes
        self.deleted_product_ids = set()  # Set to keep track of deleted product IDs
        # Rest of the code remains the same


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
        self.tree = ttk.Treeview(self.window, columns=("Product ID", "Product Name", "Price", "Quantity"),
                                  show="headings")
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

        # Display unique inventory items by ID
        self.display_unique_inventory()

        # Add button for updating quantity
        update_quantity_button = ttk.Button(self.window, text='Update Quantity', command=self.update_quantity)
        update_quantity_button.pack(pady=10, padx=20)

    def display_unique_inventory(self):
        # Initialize a set to keep track of unique product IDs
        unique_ids = set()

        # Display unique inventory items by ID
        for product in self.inventory:
            # Check if the product ID is already displayed
            if product.get_id() not in unique_ids:
                # Insert item with white lines
                tags = ('oddrow',) if len(unique_ids) % 2 == 0 else ('evenrow',)
                self.tree.insert("", "end",
                                 values=(product.get_id(), product.get_name(), product.get_price(), product.get_quantity()),
                                 tags=tags)
                unique_ids.add(product.get_id())

    def update_quantity(self):
        # Open a window to update quantity
        UpdateQuantityWindow(self.parent, self.inventory)


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

        # Filter out duplicate product IDs
        unique_product_ids = set(product.get_id() for product in self.inventory)

        # Convert the set to a list for dropdown menu options
        product_ids = list(unique_product_ids)

        # Set the default value of the selected product ID to the first ID in the list
        if product_ids:
            self.selected_product_id = tk.StringVar(value=product_ids[0])
        else:
            self.selected_product_id = tk.StringVar(value="No products available")

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
        # Get the input values
        product_id = int(self.product_id_entry.get())
        product_name = self.product_name_entry.get()
        price = float(self.price_entry.get())
        quantity = int(self.quantity_entry.get())

        # Check if the product ID already exists in the inventory
        for product in self.inventory:
            if product.get_id() == product_id:
                messagebox.showerror("Error", "Product ID already exists!")
                return  # Exit the method if the ID already exists

        # Create a new product object and add it to the inventory
        new_product = Product(product_id, product_name, price, quantity)
        self.inventory.append(new_product)  # Add the product to the inventory list

        # Close the window after adding the product
        self.window.destroy()


class AddToCartWindow:
    def __init__(self, parent, inventory, cart):
        self.parent = parent
        self.inventory = inventory
        self.cart = cart
        self.recently_added = []  # List to store recently added items
        self.displayed_product_ids = set()  # Set to store displayed product IDs

        self.window = tk.Toplevel(parent)
        self.window.title("Add to Cart")

        # Add label and Treeview widget for displaying inventory
        tk.Label(self.window, text="Select Product to Add:").pack(pady=5)
        self.tree = ttk.Treeview(self.window, columns=("Product ID", "Product Name", "Price", "Quantity"),
                                  show="headings")
        self.tree.pack(fill="both", expand=True)

        # Define column headings
        self.tree.heading("Product ID", text="Product ID")
        self.tree.heading("Product Name", text="Product Name")
        self.tree.heading("Price", text="Price")
        self.tree.heading("Quantity", text="Quantity")

        # Display all inventory items
        self.display_all_inventory()

        # Add entry for quantity selection
        tk.Label(self.window, text="Quantity:").pack(pady=5)
        self.quantity_entry = tk.Entry(self.window)
        self.quantity_entry.pack(pady=5)

        # Add button to add selected product to cart
        add_to_cart_button = ttk.Button(self.window, text="Add to Cart", command=self.add_to_cart_button_clicked)
        add_to_cart_button.pack(pady=5)

        # Add button to undo last addition
        undo_button = ttk.Button(self.window, text="Undo", command=self.undo_last_addition)
        undo_button.pack(pady=5)

    def display_all_inventory(self):
        # Display all inventory items in the Treeview
        for product in self.inventory:
            # Check if the product ID has already been displayed
            if product.get_id() not in self.displayed_product_ids:
                # Insert item with white lines
                tags = ('oddrow',) if len(self.displayed_product_ids) % 2 == 0 else ('evenrow',)
                self.tree.insert("", "end",
                                 values=(product.get_id(), product.get_name(), product.get_price(), product.get_quantity()),
                                 tags=tags)
                # Add the displayed product ID to the set
                self.displayed_product_ids.add(product.get_id())

    def add_to_cart_button_clicked(self):
        # Get the selected product ID and quantity
        selected_item = self.tree.selection()
        if selected_item:
            product_id = int(self.tree.item(selected_item, "values")[0])
            quantity_str = self.quantity_entry.get()

            # Check if quantity entry is empty
            if quantity_str:
                # Convert quantity to integer
                quantity = int(quantity_str)

                # Find the product in inventory
                selected_product = None
                for product in self.inventory:
                    if product.get_id() == product_id:
                        selected_product = product
                        break

                if selected_product:
                    # Check if the selected quantity is available in the inventory
                    if selected_product.get_quantity() >= quantity > 0:
                        # Check if the product is already in the cart
                        found_in_cart = False
                        for i, item in enumerate(self.cart):
                            if item[0].get_id() == product_id:
                                # Create a new tuple with updated quantity
                                self.cart[i] = (item[0], item[1] + quantity)
                                found_in_cart = True
                                break

                        if not found_in_cart:
                            # Add the item to the cart
                            self.cart.append((selected_product, quantity))
                            # Record the recently added item
                            self.recently_added.append((selected_product, quantity))

                        messagebox.showinfo("Success",
                                            f"{quantity} {selected_product.get_name()} added to cart.")
                    else:
                        messagebox.showwarning("Error", "Selected quantity not available or exceeds inventory.")
                else:
                    messagebox.showwarning("Error", "Product not found in inventory.")
            else:
                messagebox.showwarning("Error", "Please enter a quantity.")
        else:
            messagebox.showwarning("Error", "Please select a product.")

    def undo_last_addition(self):
        # Check if there are any recently added items
        if self.recently_added:
            # Remove the last added item from the recently added list
            last_added = self.recently_added.pop()
            self.cart.remove(last_added)  # Remove the item from the cart
            messagebox.showinfo("Undo", "Last addition undone.")
        else:
            messagebox.showinfo("Undo", "No recent additions to undo.")


class RemoveFromInventoryWindow:
    def __init__(self, parent, inventory):
        self.parent = parent
        self.inventory = inventory

        self.window = tk.Toplevel(parent)
        self.window.title("Remove from Inventory")

        # Set the size of the window
        self.window.geometry('300x150')  # Width x Height

        # Add label and dropdown menu for selecting product to remove
        tk.Label(self.window, text="Select Product to Remove:").pack(pady=5)

        # Create a list of product names
        product_names = [product.get_name() for product in self.inventory]

        # Set the default value of the selected product name to the first name in the list
        self.selected_product_name = tk.StringVar(value=product_names[0])

        # Create a dropdown menu for selecting the product name
        self.product_name_dropdown = ttk.OptionMenu(self.window, self.selected_product_name, *product_names)
        self.product_name_dropdown.pack(pady=5)

        # Add button to confirm removal
        confirm_button = ttk.Button(self.window, text="Confirm", command=self.confirm_removal)
        confirm_button.pack(pady=5)

    def confirm_removal(self):
        # Get the selected product name to remove
        selected_product_name = self.selected_product_name.get()

        # Find the selected product in the inventory and remove it
        for product in self.inventory:
            if product.get_name() == selected_product_name:
                self.inventory.remove(product)
                break

        # Close the window after removal
        self.window.destroy()


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x300')
        self.root.title('Product Manager')
        self.deleted_product_ids = set()

        # Initialize application variables
        self.inventory = []
        self.cart = []

        # Load data from file
        self.load_data()

        # Populate inventory
        self.populate_inventory()

        # Mainframe setup
        self.mainframe = tk.Frame(self.root, background='white')
        self.mainframe.pack(fill='both', expand=True)

        # Add buttons for different functionalities
        add_product_button = ttk.Button(self.mainframe, text='Add Product', command=self.open_add_product_window)
        add_product_button.grid(row=0, column=0, pady=10, padx=20, sticky="nsew")

        display_inventory_button = ttk.Button(self.mainframe, text='Display Inventory', command=self.display_inventory)
        display_inventory_button.grid(row=0, column=1, pady=10, padx=20, sticky="nsew")

        remove_product_button = ttk.Button(self.mainframe, text='Remove Product', command=self.remove_product)
        remove_product_button.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")

        update_quantity_button = ttk.Button(self.mainframe, text='Update Quantity', command=self.open_update_quantity_window)
        update_quantity_button.grid(row=1, column=1, pady=10, padx=20, sticky="nsew")

        add_to_cart_button = ttk.Button(self.mainframe, text='Add to Cart', command=self.open_add_to_cart_window)
        add_to_cart_button.grid(row=2, column=0, pady=10, padx=20, sticky="nsew")

        remove_from_cart_button = ttk.Button(self.mainframe, text='Remove from Cart', command=self.remove_from_cart)
        remove_from_cart_button.grid(row=2, column=1, pady=10, padx=20, sticky="nsew")

        display_cart_button = ttk.Button(self.mainframe, text='Display Cart', command=self.display_cart)
        display_cart_button.grid(row=3, column=0, pady=10, padx=20, sticky="nsew")

        close_button = ttk.Button(self.mainframe, text='Close Program', command=self.close_program)
        close_button.grid(row=3, column=1, pady=10, padx=20, sticky="nsew")  # Moved to row 3, column 1

        # Configure row and column weights to center the buttons
        for i in range(4):
            self.mainframe.rowconfigure(i, weight=1)
        for j in range(2):
            self.mainframe.columnconfigure(j, weight=1)

        self.root.mainloop()

    def close_program(self):
     # Save data to file before closing
        self.save_data()
        self.root.destroy()

    def save_data(self):
        # Save inventory and cart data to a file using pickle
        with open("data.pkl", "wb") as file:
            pickle.dump((self.inventory, self.cart), file)
            
            # If the inventory and cart are empty, also save empty lists to the file
        if not self.inventory and not self.cart:
            with open("data.pkl", "wb") as file:
                pickle.dump(([], []), file)

    def load_data(self):
        # Load inventory and cart data from file if available
        try:
            with open("data.pkl", "rb") as file:
                self.inventory, self.cart = pickle.load(file)
        except FileNotFoundError:
            # File not found, initialize with empty lists
            self.inventory = []
            self.cart = []

    def open_add_product_window(self):
        AddProductWindow(self.root, self.inventory)

    def open_update_quantity_window(self):
        UpdateQuantityWindow(self.root, self.inventory)

    def display_inventory(self):
        # Open a new window to display inventory
        DisplayInventoryWindow(self.root, self.inventory)

    def remove_product(self):
        # Open a window to remove a product
        RemoveProductWindow(self.root, self.inventory)

    def open_add_to_cart_window(self):
        # Open window to add products to cart
        AddToCartWindow(self.root, self.inventory, self.cart)

    def remove_from_cart(self):
        # Check if the cart is empty
        if self.cart:
            # Open a window to remove a product from the cart
            RemoveFromCartWindow(self.root, self.cart, self.update_cart_display)
        else:
            messagebox.showinfo("Empty Cart", "The cart is empty.")

    def display_cart(self):  # Moved inside the App class
        # Open a new window to display the cart
        cart_window = tk.Toplevel(self.root)
        cart_window.title("Cart")

        # Add label and Treeview widget for displaying the cart
        tk.Label(cart_window, text="Cart Items:").pack(pady=5)

        cart_tree = ttk.Treeview(cart_window, columns=("Product ID", "Product Name", "Price", "Quantity"),
                                  show="headings")
        cart_tree.pack(fill="both", expand=True)

        # Define column headings
        cart_tree.heading("Product ID", text="Product ID")
        cart_tree.heading("Product Name", text="Product Name")
        cart_tree.heading("Price", text="Price")
        cart_tree.heading("Quantity", text="Quantity")

        # Display cart items
        for item in self.cart:
            cart_tree.insert("", "end",
                             values=(item[0].get_id(), item[0].get_name(), item[0].get_price(), item[1]))

        # Add button to close cart window
        close_button = ttk.Button(cart_window, text="Close", command=cart_window.destroy)
        close_button.pack(pady=10)

    def update_cart_display(self):
        # Refresh the cart display after making changes
        self.display_cart()

    def populate_inventory(self):
        ## Filter out products with IDs present in the deleted_product_ids set
        filtered_inventory = [product for product in dictionaryInformation if product[0] not in self.deleted_product_ids]
    
        # Populate the inventory list with filtered inventory data
        for item in filtered_inventory:
            self.inventory.append(Product(*item))

    def display_inventory(self):
        # Open a new window to display inventory
        DisplayInventoryWindow(self.root, self.inventory)

    def open_add_to_cart_window(self):
        # Open window to add products to cart
        AddToCartWindow(self.root, self.inventory, self.cart)

    def open_add_product_window(self):
        AddProductWindow(self.root, self.inventory)

    def open_update_quantity_window(self):
        UpdateQuantityWindow(self.root, self.inventory)

    def populate_inventory(self):
        # Populate the inventory list with inventory data from savedData.py
        for item in dictionaryInformation:
            self.inventory.append(Product(*item))

    def display_inventory(self):
        # Open a new window to display inventory
        DisplayInventoryWindow(self.root, self.inventory)

    def remove_product(self):
        # Open a window to remove a product
        RemoveProductWindow(self.root, self.inventory, self.deleted_product_ids)

    def add_to_cart(self):
        # Implement the logic for adding a product to the cart
        pass

    def remove_from_cart(self):
        # Check if the cart is empty
        if self.cart:
             # Open a window to remove a product from the cart
              RemoveFromCartWindow(self.root, self.cart, self.update_cart_display)
        else:
            messagebox.showinfo("Empty Cart", "The cart is empty.")

    def undo_remove(self):
        # Implement the logic for undoing a removal from the cart
        pass

    def display_cart(self):  # Moved inside the App class
        # Open a new window to display the cart
        cart_window = tk.Toplevel(self.root)
        cart_window.title("Cart")

        # Add label and Treeview widget for displaying the cart
        tk.Label(cart_window, text="Cart Items:").pack(pady=5)

        # Create a Treeview widget for displaying the cart
        cart_tree = ttk.Treeview(cart_window, columns=("Product Name", "Price", "Quantity"), show="headings")
        cart_tree.pack(fill="both", expand=True)

        # Define column headings
        cart_tree.heading("Product Name", text="Product Name")
        cart_tree.heading("Price", text="Price")
        cart_tree.heading("Quantity", text="Quantity")

        total_price = 0  # Initialize total price variable

        # Display cart items
        for item in self.cart:
            cart_tree.insert("", "end", values=(item[0].get_name(), item[0].get_price(), item[1]))
            total_price += item[0].get_price() * item[1]  # Add price of each item to total

        # Add label to display total price
        tk.Label(cart_window, text=f"Total Price: ${total_price:.2f}").pack(pady=5)

        # Add button to close the cart window
        close_button = ttk.Button(cart_window, text='Close', command=cart_window.destroy)
        close_button.pack(pady=10)

    def update_cart_display(self):
        # Refresh the cart display after making changes
        self.display_cart()

    def display_cart(self):
        # Open a new window to display the cart
        cart_window = tk.Toplevel(self.root)
        cart_window.title("Cart")

        # Add label and Treeview widget for displaying the cart
        tk.Label(cart_window, text="Cart Items:").pack(pady=5)

        # Create a Treeview widget for displaying the cart
        cart_tree = ttk.Treeview(cart_window, columns=("Product Name", "Price", "Quantity"), show="headings")
        cart_tree.pack(fill="both", expand=True)

        # Define column headings
        cart_tree.heading("Product Name", text="Product Name")
        cart_tree.heading("Price", text="Price")
        cart_tree.heading("Quantity", text="Quantity")

        total_price = 0  # Initialize total price variable

        # Display cart items
        for item in self.cart:
            cart_tree.insert("", "end", values=(item[0].get_name(), item[0].get_price(), item[1]))
            total_price += item[0].get_price() * item[1]  # Add price of each item to total

        # Add label to display total price
        tk.Label(cart_window, text=f"Total Price: ${total_price:.2f}").pack(pady=5)

        # Add button to close the cart window
        close_button = ttk.Button(cart_window, text='Close', command=cart_window.destroy)
        close_button.pack(pady=10)

class RemoveFromCartWindow:
    def __init__(self, parent, cart, callback):
        self.parent = parent
        self.cart = cart
        self.callback = callback

        self.window = tk.Toplevel(parent)
        self.window.title("Remove from Cart")

        # Add label and dropdown menu for selecting product to remove
        tk.Label(self.window, text="Select Product to Remove:").pack(pady=5)

        # Create a list of tuples containing (Product ID, Product Name) for dropdown menu options
        product_options = [(item[0].get_id(), item[0].get_name()) for item in self.cart]
        self.selected_product = tk.StringVar(value=product_options[0][0])  # Set default value to the first ID
        self.product_dropdown = ttk.OptionMenu(self.window, self.selected_product, *product_options)
        self.product_dropdown.pack(pady=5)

        # Add button to confirm removal
        confirm_button = ttk.Button(self.window, text="Confirm", command=self.confirm_removal)
        confirm_button.pack(pady=5)

    def confirm_removal(self):
        # Get the selected product ID to remove
        selected_product_id = int(self.selected_product.get())

        # Find the selected product in the cart and remove it
        for item in self.cart:
            if item[0].get_id() == selected_product_id:
                self.cart.remove(item)
                break

        # Close the window after removal
        self.window.destroy()

        # Callback to update the cart display
        self.callback()

# Run the application
if __name__ == '__main__':
    App()