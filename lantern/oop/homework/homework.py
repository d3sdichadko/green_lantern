class Cat:
    """
    Write Class Cat which will receive age from user
    * Add to class average_speed variable which will get it's values
      from private method _set_average_speed()

    * Add to class saturation_level variable with value 50

    * Implement private methods _increase_saturation_level and _reduce_saturation_level
      that will receive value and add/subtract from saturation_level this value
      if saturation_level is less than 0, return 0
      if saturation_level is grosser than 100, return 100

    * Implement method eat which will receive from user product value
      if product eq fodder use _increase_saturation_level with value eq 10
      if product eq apple use _increase_saturation_level with value eq 5
      if product eq milk use _increase_saturation_level with value eq 2

    * Implement private method _set_average_speed
      if age less or eq 7 return 12
      if age between 7(not including) and 10(including) return 9
      if age grosser than 10(not including) return 6

    * Implement method run it receives hours value
      Calculate run km per hours remember that you have average_speed value
      Than if your cat run less or eq than 25 _reduce_saturation_level with value 2
      if it runs between 25(not including) and 50(including) than _reduce_saturation_level with value 5
      if it runs between 50(not including) and 100(including) than _reduce_saturation_level with value 15
      if it runs between 100(not including) and 200(including) than _reduce_saturation_level with value 25
      if it runs more than 200(not including) than _reduce_saturation_level with value 50

      return text like this: f"Your cat ran {ran_km} kilometers"

    * Implement get_saturation_level and return saturation_level
      if saturation_level eq 0 return text like this: "Your cat is dead :("

    * Implement get_average_speed and return average_speed

    """

    def __init__(self, age):
        self.age = age
        self.average_speed = self._set_average_speed()
        self.saturation_level = 50

    def eat(self, product):
        """  * Implement method eat which will receive from user product value
         if product eq fodder use _increase_saturation_level with value eq 10
         if product eq apple use _increase_saturation_level with value eq 5
         if product eq milk use _increase_saturation_level with value eq 2 """

        if product == 'fodder':
            self._increase_saturation_level(10)
        if product == 'apple':
            self._increase_saturation_level(5)
        if product == 'milk':
            self._increase_saturation_level(2)

    def _reduce_saturation_level(self, value):
        self.saturation_level -= value
        if self.saturation_level - value < 0:  self.saturation_level = 0

    def _increase_saturation_level(self, value):
        self.saturation_level += value
        if self.saturation_level + value > 100: self.saturation_level = 100

    def _set_average_speed(self):

        """ * Implement private method _set_average_speed
      if age less or eq 7 return 12
      if age between 7(not including) and 10(including) return 9
      if age grosser than 10(not including) return 6 """
        if self.age <= 7:
            return 12
        if 7 < self.age <= 10:
            return 9
        elif self.age > 10:
            return 6

    def run(self, hours):

        """ Implement method run it receives hours value
      Calculate run km per hours remember that you have average_speed value
      Than if your cat run less or eq than 25 _reduce_saturation_level with value 2
      if it runs between 25(not including) and 50(including) than _reduce_saturation_level with value 5
      if it runs between 50(not including) and 100(including) than _reduce_saturation_level with value 15
      if it runs between 100(not including) and 200(including) than _reduce_saturation_level with value 25
      if it runs more than 200(not including) than _reduce_saturation_level with value 50

      return text like this: f"Your cat ran {ran_km} kilometers" """
        ran_km = self.average_speed * hours
        if self.average_speed <= 25:
            self._reduce_saturation_level(2)
        if 25 < self.average_speed <= 50:
            self._reduce_saturation_level(5)
        if 50 < self.average_speed <= 100:
            self._reduce_saturation_level(15)
        if 100 < self.average_speed <= 200:
            self._reduce_saturation_level(25)
        if self.average_speed < 200:
            self._reduce_saturation_level(50)
        return f"Your cat ran {ran_km} kilometers"

    """ * Implement get_saturation_level and return saturation_level
      if saturation_level eq 0 return text like this: "Your cat is dead :("

    * Implement get_average_speed and return average_speed """

    def get_saturation_level(self):
        return self.saturation_level if self.saturation_level > 0 else 'Your cat is died :('

    def get_average_speed(self):
        return self.average_speed


class Cheetah(Cat):
    """
    * Inherit from class Cat

    * Redefine method eat from parent class it will receive product value
      if product eq gazelle use _increase_saturation_level from parent class with value 30
      if product eq rabbit use _increase_saturation_level from parent class with value 15

    * Redefine method _set_average_speed
      if age less or eq 5 return 90
      if age between 5 and 15(including) return 75
      if age grosser 15(not including) return 40

    """
    def __init__(self, age):
        super().__init__(age)

    def eat(self, product):
        if product == 'gazelle':
            self._increase_saturation_level(30)
        if product == 'rabbit':
            self._increase_saturation_level(15)

    def _set_average_speed(self):
        if self.age <= 5:
            return 90
        if 5 < self.age <= 15:
            return 75
        elif self.age > 15:
            return 40


class Wall:
    """
    * Implement class Wall which receives such parameters: width and height

    * Implement method wall_square which return result of simple square formula of rectangle

    * Implement method number_of_rolls_of_wallpaper which receives such parameters: roll_width_m, roll_length_m
      (_m in the parameters name means meters) return number of rolls of wallpaper

      Example:
          count of lines in roll eq roll length in meters divide height of the wall (use rounding down)
          count of lines eq width of the wall divide roll width in meters
          number of rolls of wallpaper eq count of lines divide  count of lines in roll
    """

    def __init__(self, wall_width, wall_height):
        # pass
        self.wall_width = wall_width
        self.wall_height = wall_height

    def wall_square(self):
        # pass
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        # pass
        return self.width * self.height / roll_width_m * roll_length_m


class Roof:
    """
        * Implement class Roof which receives such parameters: width, height and roof_type

        * Implement method roof_square that returns square of the roof
          if roof_type eq "gable" the roof square if simple rectangle square formula multiplied 2
          if roof_type eq "single-pitch" the roof square if simple rectangle square formula
          if other roof_type raise ValueError like this "Sorry there is only two types of roofs"

    """

    # __roof = None

    def __init__(self, roof_width, roof_height, roof_type):
        # pass
        self.roof_width = roof_width
        self.roof_height = roof_height
        self.roof_type = roof_type

    def roof_square(self):
        # pass
        if self.roof_type == 'gable':
            return self.roof_width * self.roof_height * 2
        if self.roof_type == 'single-pinch':
            return self.roof_width * self.roof_height
        else:
            raise ValueError("Sorry there is only two types of roofs")
        # round


class Window:
    """
       * Implement class Window which receives such parameters: width and height

       * Implement method window_square which return result of simple square formula of rectangle

    """

    def __init__(self, window_width, window_height):
        # pass
        self.window_width = window_width
        self.window_height = window_height

    def window_square(self):
        # pass
        return self.window_width * self.window_height


class Door:
    """
     * Implement class Door which receives such parameters: width and height
      add variables wood_price eq 10, metal_price eq 3

     * Implement method door_square which return result of simple square formula of rectangle

     * Implement method door_price which receives material value as a parameter
       if material eq wood return door_square multiplied on wood_price
       if material eq metal return door_square multiplied on metal_price
       if material value is another one (not metal or wood) raise ValueError "Sorry we don't have such material"

     *  Implement method update_wood_price which receives new_price value and updates your old price

     *  Implement method update_metal_price which receives new_price value and updates your old price

    """
    def __init__(self, door_width, door_height, wood_price, metal_price):
        # pass
        self.door_width = door_width
        self.door_height = door_height
        self.wood_price = wood_price
        self.metal_price = metal_price

    def door_square(self):
        return self.door_width * self.door_height

    def door_price(self, material):
        # self.material = material
        if material == 'wood':
            return self.door_width * self.door_height * self.wood_price
        if aterial == 'metal':
            return self.door_width * self.door_height * self.metal_price
        else:
            raise ValueError("Sorry we don't have such material")

    def update_wood_price(self, new_wood_price):
        # pass
        self.wood_price = new_wood_price

    def update_metal_price(self, new_metal_price):
        # pass
        self.metal_price = new_metal_price


class House:
    """
    !!!! DON'T WRITE NEW METHODS TO THIS CLASS EXCEPT FOR THOSE LISTED BELOW !!!

    * Add super private variable __walls and its value will be empty list
    * Add super private variable __windows and its value will be empty list
    * Add super private variable __roof and its value will be None
    * Add super private variable __door and its value will be None

    * Implement method create_wall which will create new wall using class Wall and add it to the __walls list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      if user have more than 4 walls raise ValueError "Our house can not have more than 4 walls"

    * Implement method create_roof which will create new roof using class Roof and assign it to the __roof variable
      it receives parameters width, height and roof_type
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another roof if we already have another one,
              otherwise raise ValueError "The house can not have two roofs"

    * Implement method create_window which will create new window using class Window and add it to the __windows list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"

    * Implement method create_door which will create new door using class Door and assign it to the __door variable
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another door if we already have another one,
              otherwise raise ValueError "The house can not have two doors"

    * Implement method get_count_of_walls that returns count of walls

    * Implement method get_count_of_windows that returns count of windows

    * Implement method get_door_price that receives material value and returns price of the door

    * Implement method update_wood_price that receives new_wood_price and updates old one

    * Implement method update_metal_price that receives new_metal_price and updates old one

    * Implement method get_roof_square that returns the roof square

    * Implement method get_walls_square that returns sum of all walls square that we have

    * Implement method get_windows_square that returns sum of all windows square that we have

    * Implement method get_door_square that returns the square of the door

    * Implement method get_number_of_rolls_of_wallpapers that returns sum of the number of rolls of wallpapers
      needed for all our walls
      it receives roll_width_m, roll_length_m parameters
      Check if roll_width_m or roll_length_m eq 0 raise ValueError "Sorry length must be not 0"

    * Implement method get_room_square that returns the square of our room
      (from walls_square divide windows and door square)

    """

    def __init__(self, __walls, __windows, __roof, __door):
        # pass
        self.__walls = []
        self.__windows = []
        self.__roof = None
        self.__door = None

    def create_wall(self, width, height):
        # pass
        # new_wall = Wall(width, height)
        if width or height == 0:
            raise ValueError("Value must be not 0")
        self.__walls.append((width, height))
        if len(self.__walls) > 4:
            raise ValueError("Our house can not have more than 4 walls")

    def create_roof(self, roof_width, roof_height, roof_type):
        # pass
        self.__roof.append((roof_width, roof_height, roof_type))
        if roof_width or roof_height == 0:
            raise ValueError("Value must be not 0")
        if len(self.__roof) > 1:
            raise ValueError("The house can not have two roofs")

    def create_window(self, window_width, window_height):
        # pass
        if window_width or window_height == 0:
            raise ValueError("Value must be not 0")
        self.__windows.append((window_width, window_height))

    def create_door(self, door_width, door_height):
        # pass
        if door_width or door_height == 0:
            raise ValueError("Value must be not 0")
        else:
            self.__door.append((door_width, door_height))
        if len(self.__door) > 1:
            raise ValueError("The house can not have two doors")

    def get_count_of_walls(self):
        return len(self.__walls)

    def get_count_of_windows(self):
        return len(self.__windows)

    def get_door_price(self, material):
        return Door.door_price(material)

    def update_wood_price(self, new_wood_price):
        # pass
        #new_wood_price
        self.wood_price = new_wood_price

    def update_metal_price(self, new_metal_price):
        # pass
        self.metal_price = new_metal_price

    def get_roof_square(self, roof_width, roof_height):
        # pass
        return roof_width * roof_height

    def get_walls_square(self):
        # pass
        return sum(wall.wall_width*wall.wall_height + wall.wall_width*wall.wall_height +
            wall.wall_width*wall.wall_height + wall.wall_width*wall.wall_height)

        # def __init__(self, wall_width, wall_height):
        #     # pass
        #     self.wall_width = wall_width
        #     self.wall_height = wall_height

    def get_windows_square(self):
        # pass
        return window.window_width * window.window_height

    def get_door_square(self):
        #pass
        return door.door_width * door.door_height

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        # pass
        if roll_width_m == 0 or roll_length_m == 0:
            raise ValueError("Sorry length must be not 0")
        else:
            return round(sum(wall.wall_width*wall.wall_height + wall.wall_width*wall.wall_height +
            wall.wall_width*wall.wall_height + wall.wall_width*wall.wall_height) / roll_width_m * roll_length_m)

    def get_room_square(self):
        pass

