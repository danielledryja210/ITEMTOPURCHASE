CREATE class ItemToPurchase
    SET item name, description, price, and quantity
    IF no values are provided
        SET item name to "none"
        SET item description to "none"
        SET item price to 0
        SET item quantity to 0
    CREATE method print_item_cost
        CALCULATE total cost as price multiplied by quantity
        DISPLAY item name, quantity, price, and total cost
    CREATE method print_item_description
        DISPLAY item name and item description
