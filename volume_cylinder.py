# calculate volume of cylinder


from math import pi as pi
from typing import Any, Union


def volume_cylinder(radius, height):
    """ Returns volume of a cylinder given radius, height."""
    assert isinstance(height, object)
    volume: Union[float, Any] = pi * radius ** 2 * height
    return volume

six_pack_volume = volume_cylinder(2.5, 5) * 6
print(six_pack_volume)
