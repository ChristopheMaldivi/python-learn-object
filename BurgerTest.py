import unittest


class Kebab(object):
    def __init__(self):
        self.bread = False
        self.tomatoes = False
        self.onions = False
        self.salad = False
        self.meat = False

    def add_bread(self):
        self.bread = True
    def add_tomatoes(self):
        self.tomatoes = True
    def add_onions(self):
        self.onions = True
    def add_salad(self):
        self.salad = True
    def add_meat(self):
        self.meat = True

    def description(self):
        if not self.meat:
            return "I am a veggie kebab"
        elif self.bread:
            return "I am an empty bread only kebab, please help!"
        else:
            return 'IAmAnEmptyKebab'


class KebabTest(unittest.TestCase):
    def test_kebab_can_say_IAmAnEmptyKebab(self):
        # given
        kebab = Kebab()
        # when
        description = kebab.description
        # then
        self.assertEqual('IAmAnEmptyKebab', description)

    def test_kebab_with_bread_and_others(self):
        # given
        kebab = Kebab()
        # when
        kebab.add_bread()
        description = kebab.description
        # then
        self.assertEqual('I am an empty bread only kebab, please help!', description)

    def test_kebab_for_veggie(self):
        # given
        kebab = Kebab()
        # when
        kebab.add_bread()
        kebab.add_tomatoes()
        kebab.add_onions()
        kebab.add_salad()
        description = kebab.description
        # then
        self.assertEqual('I am a veggie kebab', description)


if __name__ == '__main__':
    unittest.main()
