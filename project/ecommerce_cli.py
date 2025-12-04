#!/usr/bin/env python3
"""
Simple CLI E-commerce demo

Features:
- Browse products
- Search products
- Add/remove items to cart
- Checkout and save order to a file

This script contains a compulsory `main()` function and multiple classes
(`Product`, `Catalog`, `Cart`, `Order`) plus several helper functions.
"""
from dataclasses import dataclass
from typing import Dict, List, Optional
import json
import datetime
import os


@dataclass
class Product:
    id: str
    name: str
    price: float
    stock: int
    description: str = ""

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
            "description": self.description,
        }


class Catalog:
    def __init__(self, products: Optional[List[Product]] = None):
        self.products: Dict[str, Product] = {}
        if products:
            for p in products:
                self.products[p.id] = p

    def list_products(self) -> List[Product]:
        return list(self.products.values())

    def get_product(self, product_id: str) -> Optional[Product]:
        return self.products.get(product_id)

    def search(self, term: str) -> List[Product]:
        t = term.lower()
        return [p for p in self.products.values() if t in p.name.lower() or t in p.description.lower()]


class Cart:
    def __init__(self):
        self.items: Dict[str, int] = {}

    def add(self, product: Product, qty: int = 1) -> bool:
        if product.stock < qty:
            return False
        self.items[product.id] = self.items.get(product.id, 0) + qty
        return True

    def remove(self, product_id: str, qty: int = 1) -> bool:
        if product_id not in self.items:
            return False
        if qty >= self.items[product_id]:
            del self.items[product_id]
        else:
            self.items[product_id] -= qty
        return True

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def clear(self):
        self.items.clear()

    def view(self, catalog: Catalog) -> List[Dict]:
        rows = []
        for pid, qty in self.items.items():
            p = catalog.get_product(pid)
            if p:
                rows.append({"id": pid, "name": p.name, "price": p.price, "qty": qty, "subtotal": p.price * qty})
        return rows

    def total(self, catalog: Catalog) -> float:
        return sum((catalog.get_product(pid).price * qty) for pid, qty in self.items.items() if catalog.get_product(pid))


class Order:
    def __init__(self, items: Dict[str, int], catalog: Catalog, customer: str = "guest"):
        self.items = items.copy()
        self.catalog = catalog
        self.customer = customer
        self.created_at = datetime.datetime.utcnow().isoformat() + "Z"
        self.total_amount = self.compute_total()

    def compute_total(self) -> float:
        return sum((self.catalog.get_product(pid).price * qty) for pid, qty in self.items.items() if self.catalog.get_product(pid))

    def to_dict(self) -> Dict:
        return {
            "customer": self.customer,
            "created_at": self.created_at,
            "total_amount": self.total_amount,
            "items": [{"id": pid, "qty": qty, "name": self.catalog.get_product(pid).name if self.catalog.get_product(pid) else None} for pid, qty in self.items.items()],
        }

    def save(self, path: str = "orders.txt") -> None:
        data = self.to_dict()
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")


def load_sample_products() -> Catalog:
    sample = [
        Product(id="p1", name="T-shirt", price=19.99, stock=10, description="Comfortable cotton tee"),
        Product(id="p2", name="Sneakers", price=59.99, stock=5, description="Running shoes"),
        Product(id="p3", name="Coffee Mug", price=9.5, stock=20, description="Ceramic mug 300ml"),
        Product(id="p4", name="Notebook", price=4.25, stock=50, description="A5 ruled notebook"),
        Product(id="p5", name="Backpack", price=39.0, stock=7, description="Water-resistant backpack"),
    ]
    return Catalog(sample)


def display_products(catalog: Catalog) -> None:
    print("\nAvailable products:")
    for p in catalog.list_products():
        print(f"{p.id}: {p.name} — ${p.price:.2f} — stock: {p.stock}")


def display_cart(cart: Cart, catalog: Catalog) -> None:
    print("\nYour cart:")
    rows = cart.view(catalog)
    if not rows:
        print(" (empty)")
        return
    for r in rows:
        print(f"{r['id']}: {r['name']} x{r['qty']} — ${r['subtotal']:.2f}")
    print(f"Total: ${cart.total(catalog):.2f}")


def checkout(cart: Cart, catalog: Catalog) -> None:
    if cart.is_empty():
        print("Cart is empty — nothing to checkout.")
        return
    name = input("Enter your name for the order (or press Enter for 'guest'): ").strip() or "guest"
    order = Order(cart.items, catalog, customer=name)
    os.makedirs("./data", exist_ok=True)
    order.save(path=os.path.join("data", "orders.txt"))
    # reduce stock
    for pid, qty in cart.items.items():
        p = catalog.get_product(pid)
        if p:
            p.stock = max(0, p.stock - qty)
    cart.clear()
    print(f"Order saved for {name}. Total: ${order.total_amount:.2f}")


def display_menu() -> None:
    print("\n--- CLI E-commerce ---")
    print("1. List products")
    print("2. Search products")
    print("3. View product details")
    print("4. Add to cart")
    print("5. View cart")
    print("6. Remove from cart")
    print("7. Checkout")
    print("0. Exit")


def main() -> None:
    """Compulsory entry point for the CLI app."""
    catalog = load_sample_products()
    cart = Cart()

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_products(catalog)
        elif choice == "2":
            term = input("Search term: ").strip()
            results = catalog.search(term)
            if not results:
                print("No products found.")
            else:
                for p in results:
                    print(f"{p.id}: {p.name} — ${p.price:.2f} — stock: {p.stock}")
        elif choice == "3":
            pid = input("Product id: ").strip()
            p = catalog.get_product(pid)
            if not p:
                print("Product not found.")
            else:
                print(f"{p.id}: {p.name}\nPrice: ${p.price:.2f}\nStock: {p.stock}\nDesc: {p.description}")
        elif choice == "4":
            pid = input("Product id to add: ").strip()
            qty = input("Quantity: ").strip()
            if not qty.isdigit() or int(qty) <= 0:
                print("Invalid quantity")
                continue
            qty = int(qty)
            p = catalog.get_product(pid)
            if not p:
                print("Product not found.")
            else:
                if p.stock < qty:
                    print(f"Not enough stock. Available: {p.stock}")
                else:
                    cart.add(p, qty)
                    print(f"Added {qty} x {p.name} to cart.")
        elif choice == "5":
            display_cart(cart, catalog)
        elif choice == "6":
            pid = input("Product id to remove: ").strip()
            if cart.remove(pid):
                print("Removed / decremented from cart")
            else:
                print("That item is not in your cart.")
        elif choice == "7":
            checkout(cart, catalog)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Unknown option — try again.")


if __name__ == "__main__":
    main()
