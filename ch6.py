class Fridge:
    """This class implements a fridge where ingredients can be added and removed
    individually,or in groups.
    Methods:
    has(food_name [,quantity])
    has_various(foods)
    add_one(food_name)
    add_many(food_dict)
    get_one(food_name)
    get_many(food_dict)
    get_ingredients(food)"""

    def __init__(self,items={}):
        """Optionally pass in an initial dictionary of items"""
        if type(items) != type({}):
            raise TypeError("Fridge requires a dictionary but was given %s" %type(items))
        self.items = items
        return
        
    def __add_multi(self,food_name,quantity):
        if (not food_name in self.items):
            self.items[food_name] = 0
        self.items[food_name] = self.items[food_name] + quantity

    def add_one(self,food_name):
        if type(food_name) != type(""):
            raise TypeError,"add_one requires a string,given %s" % type(food_name)
        else:
            self.__add_multi(food_name,1)
        return True

    def add_many(self,food_dict):
        if type(food_dict) != type({}):
            raise TypeError("add_many requires a dictionary,got a %s" % type(food_dict))
        for item in food_dict.keys():
            self.__add_multi(item,food_dict[item])
        return
    def has(self,food_name,quantity=1):
        """
        has(food_name,[quantity[) check if the string food_name is in the fridge.
        Quantity defaults to 1.
        """
        return self.has_variouse({food_name:quantity})

    def has_variouse(self,foods):
        """
        has_variouse(foods) determines if the dictionary food_name
        has enough of every element to satisfy a request.
        """
        try:
            for food in foods.keys():
                if self.items[food] < foods[food]:
                    return False
            return True
        except KeyError:
            return False
    def __get_multi(self,food_name,quantity):
        """
        __get_multi(food_name,quantity)-removes move than one of a food item.
        Return the numble of items removed.
        """
        try:
            if (self.item[food_name] is None):
                return False
            if (quantity > self.items[food_name]):
                return False
            self.items[food_name] = self.items[food_name] - quantity
        except KeyError:
            return False
        return quantity

    def get_one(self,food_name):
        if type(food_name) != type(""):
            raise TypeError("get_one requires a string,given a %s" % type(food_name))
        else:
            result = self.__get_multi(food_name,1)
        return result

    def get_many(self,food_dict):
        if self.has_variouse(food_dict):
            food_removed = {}
            for item in food_dict.keys():
                food_removed[item] = self.__get_multi(item,food_dict[item])
            return food_removed

    def get_ingredients(self,food):
        """get_ingredients(food) -If passed an object that has the __ingreients__
        method,get_many will invoke this to get the list of ingreients.
        """
        try:
            ingredients = self.get_many(food.__ingreients__())
        except AttributeError:
            return False
        if ingredients != False:
            return ingreients

