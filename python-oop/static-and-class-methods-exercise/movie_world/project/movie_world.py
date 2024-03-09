from typing import List
from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity() -> int:
        return 15

    @staticmethod
    def customer_capacity() -> int:
        return 10

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < MovieWorld.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        dvd = next(filter(lambda d: d.id == dvd_id, self.dvds))

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd not in customer.rented_dvds and dvd.is_rented:
            return "DVD is already rented"
        elif customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = next(filter(lambda c: c.id == customer_id, self.customers))
        try:
            dvd = next(filter(lambda d: d.id == dvd_id, customer.rented_dvds))
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        except StopIteration:
            return f"{customer.name} does not have that DVD"

    def __repr__(self) -> str:
        result = ""
        for customer in self.customers:
            result += f"{customer.__repr__()}\n"
        for dvd in self.dvds:
            result += f"{dvd.__repr__()}\n"
        return result.strip()
