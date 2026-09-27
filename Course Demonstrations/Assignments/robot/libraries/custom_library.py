from robot.api.deco import keyword


class CustomLibrary:

    @keyword("Calculate Sum")
    def calculate_sum(self, first_number, second_number):
        return int(first_number) + int(second_number)

    @keyword("Create Greeting")
    def create_greeting(self, name):
        return f"Hello, {name}!"