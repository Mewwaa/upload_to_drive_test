# Builder
class PizzaBuilder:
    def __init__(self):
        self._pizza = Pizza()

    def set_crust(self, crust):
        self._pizza.crust = crust

    def add_topping(self, topping):
        self._pizza.toppings.append(topping)

    def build(self):
        pizza = self._pizza
        self._pizza = Pizza()
        return pizza

class Pizza:
    def __init__(self):
        self.crust = None
        self.toppings = []

    def __str__(self):
        return f"Crust: {self.crust}, Toppings: {', '.join(self.toppings)}"


# Observer
class PizzaOrder:
    def __init__(self):
        self._observers = []
        self._pizza = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._pizza)

    def place_order(self, pizza):
        self._pizza = pizza
        self.notify()


class PizzaDeliveryObserver:
    def update(self, pizza):
        print(f"Pizza '{pizza}' is out for delivery!")


# Singleton 
class PizzaDeliveryService:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PizzaDeliveryService()
        return cls._instance

    def deliver_pizza(self, pizza):
        print(f"Delivering pizza '{pizza}' to the customer.")


if __name__ == '__main__':
    pizza_builder = PizzaBuilder()
    pizza_builder.set_crust("Thin crust")
    pizza_builder.add_topping("Cheese")
    pizza_builder.add_topping("Mushrooms")
    pizza = pizza_builder.build()
    print(pizza)

    pizza_order = PizzaOrder()
    pizza_delivery_observer = PizzaDeliveryObserver()
    pizza_order.attach(pizza_delivery_observer)
    pizza_order.place_order(pizza)
   
    delivery_service = PizzaDeliveryService.get_instance()
    delivery_service.deliver_pizza(pizza)
