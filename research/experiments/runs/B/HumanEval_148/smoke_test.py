from solution import bf

# Test examples from docstring
assert bf("Jupiter", "Neptune") == ("Saturn", "Uranus")
assert bf("Earth", "Mercury") == ("Venus",)
assert bf("Mercury", "Uranus") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")

# Test invalid planet names
assert bf("Jupiter", "InvalidPlanet") == ()
assert bf("InvalidPlanet", "Jupiter") == ()
assert bf("Pluto", "Earth") == ()

# Test adjacent planets (nothing between them)
assert bf("Mercury", "Venus") == ()
assert bf("Saturn", "Uranus") == ()

# Test same planet
assert bf("Earth", "Earth") == ()

# Test reversed order (should give same result)
assert bf("Neptune", "Jupiter") == ("Saturn", "Uranus")
assert bf("Mercury", "Earth") == ("Venus",)

# Test larger ranges
assert bf("Mercury", "Neptune") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus")
assert bf("Venus", "Saturn") == ("Earth", "Mars", "Jupiter")

# Test with first and last planets
assert bf("Mercury", "Mars") == ("Venus", "Earth")
assert bf("Uranus", "Mercury") == ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
