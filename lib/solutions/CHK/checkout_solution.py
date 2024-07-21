from collections import Counter
from dataclasses import dataclass

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    for sku in skus:
        if sku not in store:
            return -1

    total_checkout = 0

    free_items = []
    skus_counter = Counter(skus)
    for sku, quantity in skus_counter.items():
        price, free_item = store[sku].get_price(quantity)
        total_checkout += price
        if free_item:
            free_items.append(free_item)

    for free_item in free_items:
        if free_item.name in skus_counter:
            total_checkout -= free_item.price

    return total_checkout


@dataclass
class SpecialOffer:
    quantity: int
    price: int


@dataclass
class FreeItemOffer:
    quantity: int
    free_item: str
    free_item_quantity: int

@dataclass
class FreeItem:
    name: str
    price: int


@dataclass
class Item:
    name: str
    price: int
    special_offers: list[SpecialOffer | FreeItemOffer] | None = None

    def get_price(self, quantity=1) -> tuple[int, FreeItem | None]:
        if self.special_offers:
            price = 0
            quantity_offers = sorted(
                [offer for offer in self.special_offers if isinstance(offer, SpecialOffer)],
                key=lambda x: x.quantity, reverse=True
            )

            for offer in quantity_offers:
                if quantity >= offer.quantity:
                    price += offer.price * (quantity // offer.quantity)
                    quantity %= offer.quantity
                else:
                    pass
            else:
                price += self.price * quantity

            _free_item = None
            free_item_offers = [offer for offer in self.special_offers if isinstance(offer, FreeItemOffer)]
            for offer in free_item_offers:
                if quantity >= offer.quantity:
                    free_item_quantity = quantity // offer.quantity
                    free_item = store[offer.free_item]
                    quantity %= offer.quantity
                    _free_item = FreeItem(free_item.name, free_item_quantity * offer.free_item_quantity)
            return price, _free_item

        return self.price * quantity, None


store = {
    'A': Item('A', 50, [SpecialOffer(3, 130), SpecialOffer(5, 200)]),
    'B': Item('B', 30, [SpecialOffer(2, 45)]),
    'C': Item('C', 20),
    'D': Item('D', 15),
    'E': Item('E', 40, [FreeItemOffer(2, 'B', 1)],)
}




