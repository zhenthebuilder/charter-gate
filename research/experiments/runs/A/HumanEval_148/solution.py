def bf(planet1, planet2):
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    try:
        idx1 = planets.index(planet1)
        idx2 = planets.index(planet2)
    except ValueError:
        return ()
    
    min_idx = min(idx1, idx2)
    max_idx = max(idx1, idx2)
    
    return planets[min_idx + 1:max_idx]
