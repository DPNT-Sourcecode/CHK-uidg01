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
    if any_offer := any_three_items_offer(skus_counter):
        return any_offer

    free_items = get_free_items(skus_counter)

    for free_item in free_items:
        if free_item in skus_counter:
            skus_counter[free_item] -= 1

    any_three_items_discount = any_three_items_offer(skus_counter)

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
    free_item: str
    free_item_quantity: int


@dataclass
class Item:
    name: str
    price: int
    special_offers: list[SpecialOffer | FreeItemOffer] | None = None

    def get_price(self, quantity):
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


def any_three_items_offer(counter):
    # buy any 3 of (S,T,X,Y,Z) for 45
    items = {'S', 'T', 'X', 'Y', 'Z'}
    offer = 0
    if set(counter.keys()).intersection(items):
        if sum([counter[item] for item in items]) >= 3:
            times = sum([counter[item] for item in items]) // 3
            offer += times * 45
    return offer


store = {
    'A': Item('A', 50, [SpecialOffer(3, 130), SpecialOffer(5, 200)]),
    'B': Item('B', 30, [SpecialOffer(2, 45)]),
    'C': Item('C', 20),
    'D': Item('D', 15),
    'E': Item('E', 40, [FreeItemOffer(2, 'B', 1)]),
    'F': Item('F', 10, [SpecialOffer(3, 20)]),
    'G': Item('G', 20),
    'H': Item('H', 10, [SpecialOffer(5, 45), SpecialOffer(10, 80)]),
    'I': Item('I', 35),
    'J': Item('J', 60),
    'K': Item('K', 70, [SpecialOffer(2, 120)]),
    'L': Item('L', 90),
    'M': Item('M', 15),
    'N': Item('N', 40, [FreeItemOffer(3, 'M', 1)]),
    'O': Item('O', 10),
    'P': Item('P', 50, [SpecialOffer(5, 200)]),
    'Q': Item('Q', 30, [SpecialOffer(3, 80)]),
    'R': Item('R', 50, [FreeItemOffer(3, 'Q', 1)]),
    'S': Item('S', 20), # buy any 3 of (S,T,X,Y,Z) for 45
    'T': Item('T', 20), # buy any 3 of (S,T,X,Y,Z) for 45
    'U': Item('U', 40, [SpecialOffer(4, 120)]),
    'V': Item('V', 50, [SpecialOffer(2, 90), SpecialOffer(3, 130)]),
    'W': Item('W', 20),
    'X': Item('X', 17), # buy any 3 of (S,T,X,Y,Z) for 45
    'Y': Item('Y', 20), # buy any 3 of (S,T,X,Y,Z) for 45
    'Z': Item('Z', 21), # buy any 3 of (S,T,X,Y,Z) for 45
}



