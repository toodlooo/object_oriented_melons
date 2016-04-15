"""This file should have our order classes in it."""

class AbstractMelonOrder (object):
    """ Abstract class for shared attributes/methods from domestic and international melon orders """

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.order_type = None
        self.shipped = False
        tax = None

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    def __init__(self):
        self.order_type = "domestic" # Only for Domestic, different value
        self.tax = 0.08 # Only for Domestic, different value

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    #country_code = country_code # Only for International
    def __init__(self, species, qty, country_code):
        super(InternationalMelonOrder, self).__init__(species, qty, "international", 0.17)
        self.country_code = country_code
        # self.order_type = "international" # Only for International, different value
        # self.tax = 0.17 # Only for International, different value

    def get_country_code(self): # Only for International
        """Return the country code."""
        return self.country_code