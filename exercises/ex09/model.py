"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730511294"  


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> Point:
        """Calculates the distance between two points."""
        return sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = constants.VULNERABLE

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def contract_disease(self) -> None:
        """Converts a cell into an infected one."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Tests to see if a cell is uninfected."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False

    def is_infected(self) -> bool:
        """Tests to see if a cell is infected."""
        if self.sickness == constants.INFECTED:
            return True
        elif self.sickness >= constants.INFECTED:
            return True
        else:
            return False

    def tick(self) -> None:
        """Computes the cell's new location frame by frame."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
 
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "green"
        if self.is_immune():
            return "orange"
        else:
            return "gray"

    def contact_with(self, cell: Cell) -> None:
        """Interaction if two cells make contact."""
        if (self.is_vulnerable() and cell.is_vulnerable()) or (self.is_infected() and cell.is_infected()) is True:
            self.is_infected()
            self.contract_disease()
        elif self.is_immune() or cell.is_immune():
            return
        elif self.is_infected() is True:
            cell.contract_disease()
        elif cell.is_infected() is True:
            self.contract_disease()
    
    def immunize(self) -> None:
        """Converts the sickness of a cell to immune."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Return true if the tested cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, i_population: int, healthy: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if i_population >= cells or i_population <= 0:
            raise ValueError("Need a valid # of infected.")
        if healthy < 0:
            raise ValueError("Need a valid # of immune.")
        if healthy + i_population > cells:
            raise ValueError("Need a valid # of infected and immune.")
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(i_population):
            self.population[_].contract_disease()
        for _ in range(i_population, i_population + healthy):
            self.population[_].immunize()
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0
    
    def check_contacts(self) -> None:
        """Checks to see if two cells made contact."""
        for key in range(len(self.population)):
            for i in range(key + 1, len(self.population)):
                if self.population[key].location.distance(self.population[i].location) < constants.CELL_RADIUS:
                    self.population[key].contact_with(self.population[i])

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for _ in self.population:
            if _.is_infected():
                return False
        return True