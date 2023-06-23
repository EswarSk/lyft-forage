import unittest
from datetime import date
from system.car import CarFactory

class CarTest(unittest.TestCase):
    def test_calliope_needs_service(self):
        current_date = date(2023, 1, 1)
        last_service_date = date(2021, 1, 1)
        current_mileage = 40000
        last_service_mileage = 20000

        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_glissade_needs_service(self):
        current_date = date(2023, 1, 1)
        last_service_date = date(2021, 1, 1)
        current_mileage = 40000
        last_service_mileage = 20000

        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_palindrome_needs_service(self):
        current_date = date(2023, 1, 1)
        last_service_date = date(2021, 1, 1)
        warning_light_on = True

        car = CarFactory.create_palindrome(current_date, last_service_date, warning_light_on)
        self.assertTrue(car.needs_service())

    def test_rorschach_needs_service(self):
        current_date = date(2023, 1, 1)
        last_service_date = date(2021, 1, 1)
        current_mileage = 80000
        last_service_mileage = 50000

        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_thovex_needs_service(self):
        current_date = date(2023, 1, 1)
        last_service_date = date(2021, 1, 1)
        current_mileage = 80000
        last_service_mileage = 50000

        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

if __name__ == '__main__':
    unittest.main()
