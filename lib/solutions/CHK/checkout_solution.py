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
    free_items = get_free_items(skus_counter)

    for free_item in free_items:
        if free_item in skus_counter:
            skus_counter[free_item] -= 1

    for sku, quantity in skus_counter.items():
        total_checkout += store[sku].get_price(quantity, skus)
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
class Item:
    name: str
    price: int
    special_offers: list[SpecialOffer | FreeItemOffer] | None = None

    def get_price(self, quantity, skus):
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

            return price

        return self.price * quantity

def get_free_items(counter):
    free_items = []
    for sku, quantity in counter.items():
        if sku in store:
            item = store[sku]
            if item.special_offers:
                free_item_offers = [offer for offer in item.special_offers if isinstance(offer, FreeItemOffer)]
                for offer in free_item_offers:
                    if quantity >= offer.quantity:
                        times = quantity // offer.quantity
                        for _ in range(times):
                            free_items.append(offer.free_item)
    return free_items

store = {
    'A': Item('A', 50, [SpecialOffer(3, 130), SpecialOffer(5, 200)]),
    'B': Item('B', 30, [SpecialOffer(2, 45)]),
    'C': Item('C', 20),
    'D': Item('D', 15),
    'E': Item('E', 40, [FreeItemOffer(2, 'B', 1)],)
}







