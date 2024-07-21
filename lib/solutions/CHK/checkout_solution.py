from collections import Counter
from dataclasses import dataclass

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for sku in skus:
        if sku not in store:
            return -1

    total_checkout = 0

    skus_counter = Counter(skus)
    for sku, quantity in skus_counter.items():
        total_checkout += store[sku].get_price(quantity)

    return total_checkout


@dataclass
class SpecialOffer:
    quantity: int
    price: int


@dataclass
class FreeItemOffer:
    quantity: int
    free_item: "Item"
    free_item_quantity: int


@dataclass
class Item:
    name: str
    price: int
    special_offer: list[SpecialOffer] | None = None

    def get_price(self, quantity=1):
        if self.special_offer and quantity >= self.special_offer.quantity:
            return self.special_offer.price * (quantity // self.special_offer.quantity) + self.price * (quantity % self.special_offer.quantity)
        return self.price * quantity


store = {
    'A': Item('A', 50, [SpecialOffer(3, 130), SpecialOffer(5, 200)]),
    'B': Item('B', 30, [SpecialOffer(2, 45)]),
    'C': Item('C', 20),
    'D': Item('D', 15),
    'E': Item('E', 40), # TODO: Add special offer for E
}


