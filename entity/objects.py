# --- Создание персонажей ---
class GameObject:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_cords(self):
        return self._x, self._y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def draw(self, screen):
        pass


class Model:
    def __init__(self, image):
        self._image = image

    @property
    def image(self):
        return self._image


class Creature(GameObject):
    max_hp = 100

    def __init__(self, hp, weapon, models, x, y):
        super().__init__(x, y)
        self._hp = hp
        self._weapon = weapon
        self._models = models
        self.__active_model_idx = 0

    def hit(self, damage):
        self._hp -= damage
        return self._hp <= 0

    def heal(self, value):
        self._ph += value
        if self._ph > Creature.max_hp:
            self._ph = Creature.max_hp

    def speed(self):
        pass

    def move(self, directions, barriers):
        if len(directions) == 0:
            return None
        if not self.can_go(directions, barriers):
            return None
        if "right" in directions:
            self._x += self.speed()
        if "left" in directions:
            self._x -= self.speed()
        if "up" in directions:
            self._y -= self.speed()
        if "down" in directions:
            self._y += self.speed()
        self._next_model()
        return None

    def can_go(self, directions, barriers):
        if "right" in directions:
            x = self._x + self.speed()
        elif "left" in directions:
            x = self._x - self.speed()
        else:
            x = self._x
        if "up" in directions:
            y = self._y - self.speed()
        elif "down" in directions:
            y = self._y + self.speed()
        else:
            y = self._y
        for cords in barriers:
            if self.squares_intersect((x, y), cords):
                return False
        return True

    def squares_intersect(self, p1, p2, size=80):
        x1, y1 = p1
        x2, y2 = p2

        left1 = x1
        right1 = x1 + size
        bottom1 = y1 + size
        top1 = y1

        left2 = x2
        right2 = x2 + size
        bottom2 = y2 + size
        top2 = y2

        intersect_x = not (right1 <= left2 or right2 <= left1)
        intersect_y = not (top1 >= bottom2 or top2 >= bottom1)

        return intersect_x and intersect_y

    def get_active_model(self):
        return self._models[self.__active_model_idx]

    def _next_model(self):
        if self.__active_model_idx < len(self._models) - 1:
            self.__active_model_idx += 1
        else:
            self.__active_model_idx = 0


class Weapon(GameObject):
    def force(self):
        pass

    def lenForce(self):
        pass


class Sword(Weapon):
    def force(self):
        return 10

    def lenForce(self):
        return 3


class Gun(Weapon):
    def force(self):
        return 5

    def lenForce(self):
        return 10


class Robber(Creature):

    def get_barrier(self, directions, barriers):
        if "right" in directions:
            x = self._x + self.speed()
        elif "left" in directions:
            x = self._x - self.speed()
        else:
            x = self._x
        if "up" in directions:
            y = self._y - self.speed()
        elif "down" in directions:
            y = self._y + self.speed()
        else:
            y = self._y
        for cords in barriers:
            if self.squares_intersect((x, y), cords):
                return cords
        return None

    def move(self, directions, barriers):
        if len(directions) == 0:
            return None
        if self.can_go(directions, barriers):
            return super().move(directions, barriers)
        barrier_cords = self.get_barrier(directions, barriers)
        if barrier_cords[-1] < self._y:
            self._y += self.speed()
        else:
            self._y -= self.speed()
        self._next_model()
        return None



    def speed(self):
        return 3

    def move_to_player(self, player_cords, barriers):
        directions = []
        if player_cords[0] < self.get_cords()[0]:
            directions.append("left")
        if player_cords[0] > self.get_cords()[0]:
            directions.append("right")
        if player_cords[1] < self.get_cords()[1]:
            directions.append("up")
        if player_cords[1] > self.get_cords()[1]:
            directions.append("down")
        self.move(directions, barriers)

class Werewolf(Creature):
    def speed(self):
        return 5

    def transform(self):
        pass


class Elf(Creature):
    def speed(self):
        return 2


class Area(GameObject):
    def __init__(self, x, y, models):
        super().__init__(x, y)
        self._models = models

    @property
    def models(self):
        return self._models
