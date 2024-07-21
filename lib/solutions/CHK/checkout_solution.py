from dataclasses import dataclass

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for sku in skus:
        if sku not in basket:
            return -1

    total_checkout = 0
    for sku in skus:
        total_checkout += basket[sku].get_price()

    return total_checkout


@dataclass
class SpecialOffer:
    quantity: int
    price: int


@dataclass
class Item:
    name: str
    price: int
    special_offer: SpecialOffer | None = None

    def get_price(self) -> int:
        if self.special_offer:
            return self.special_offer.price
        return self.price


basket = {
    'A': Item('A', 50, SpecialOffer(3, 130)),
    'B': Item('B', 30, SpecialOffer(2, 45)),
    'C': Item('C', 20),
    'D': Item('D', 15),
}






