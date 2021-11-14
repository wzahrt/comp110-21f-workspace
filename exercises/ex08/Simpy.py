"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730490857"


class Simpy:
    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize a list for Simpy."""
        self.values = values
    
    def __str__(self) -> str:
        """Makes simpy a string representation."""
        return f"Simpy({self.values})"

    def fill(self, number: float, multiplier: int) -> None:
        """Fills simpy's values with a specific number of repeating values."""
        self.values = []
        i: int = 0
        while i < multiplier:
            self.values.append(number)
            i += 1
        
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fills in simpy's values with values attribute with range of values like the range function but for floats."""
        step != 0.0
        self.values = []
        i: float = 0.0
        while i + start != stop:
            self.values.append(start + i)
            i += step
    
    def sum(self) -> float:
        """Sums up simpy's values and returns a float."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds two simpy classes together or adds the same value to each value in simpy's list."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i += 1
        return result
    
    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Raises one simpy class to the power of another or raises the same value to the power of each of the values in simpy's list."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                result.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compares two simpy classes or a simpy and a float and produces a bool based on whether they are equal."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value == rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] == rhs.values[i])
                i += 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Compares two simpy classes or a simpy and a float and produces a bool based on whether the first argument is greater than the second."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                result.append(value > rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                result.append(self.values[i] > rhs.values[i])
                i += 1
        return result
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription notation."""
        if isinstance(rhs, int):
            i: int = 0
            while i != rhs:
                i += 1
            return self.values[i]
        else:
            result: Simpy = Simpy([])
            i: int = 0
            while i < len(rhs):
                if rhs[i] is True:
                    result.values.append(self.values[i])
                i += 1
            return result