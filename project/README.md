# CLI E-commerce Demo

This is a small command-line e-commerce demonstration built for a class project.

Features
- Browse a small catalog of sample products
- Search products by name/description
- View product details
- Add / remove items from a shopping cart
- Checkout — saves orders to `project/data/orders.txt`

Files
- `ecommerce_cli.py`: Main CLI application. Run this to start the interactive app.

How it works
- The app ships with a small sample product catalog.
- Use the numbered menu to browse, add items to your cart, and checkout.
- On checkout, orders are appended as JSON lines into `project/data/orders.txt`.

Run
Open a terminal in the workspace root (Windows PowerShell) and run:

```powershell
python .\project\ecommerce_cli.py
```

Notes
- The script requires Python 3.6+ (uses dataclasses if running on 3.7+; if you run on 3.6 install `dataclasses` backport).
- Orders are stored in `project/data/orders.txt` (created automatically).

Possible improvements
- Persist catalog to JSON and allow adding new products
- Add basic validation, pricing discounts, or user accounts
- Add unit tests for core classes

Enjoy testing the small CLI shop!
