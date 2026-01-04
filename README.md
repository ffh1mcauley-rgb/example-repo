##  example-repo

# Inventory Database

Note : To use the files -  place them in the directory that your IDE terminal is set to or change the
terminal to their location. Then run the python file inside of your IDE.

This is python program plus a .txt file that operates as a database for an inventory of trainers.
The main chunk of the program is the python file inventory.py which acts as the database control menu.
It works primarily by creating Shoe objects which are stored to a list before being manipulated as per
the user's requests.

Within the menu, you can view your existing database, store new values by inputting the required data,
calculate total value per product by multiplying stock and cost per item.
Also you can restock the item that has the lowest stock as well as put the highest stock item on sale.

The .txt file is used primarily as an external data entry point for the database. The database will read
the file and upload all of the data within it to the database to allow for lots of products to be added 
simultaneously.
