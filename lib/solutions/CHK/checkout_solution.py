from dataclasses import dataclass

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for sku in skus:
        if sku not in basket:
            return -1

    total_checkout = 0

    return -1


@dataclass
class SpecialOffer:
    quantity: int
    price: int


@dataclass
class Item:
    name: str
    price: int
    special_offer: SpecialOffer | None = None


basket = {
    'A': Item('A', 50, SpecialOffer(3, 130)),
    'B': Item('B', 30, SpecialOffer(2, 45)),
    'C': Item('C', 20),
    'D': Item('D', 15),
}

def get_item_checkout_price(item: Item, quantity: int):
    if item.special_offer:
        return item.special_offer.price

    return item.price



