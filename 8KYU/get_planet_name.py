def get_planet_name(id):
    """ This function returns planet`s name by id. """
    planet = {1: 'Mercury',
              2: 'Venus',
              3: 'Earth',
              4: 'Mars',
              5: 'Jupiter',
              6: 'Saturn',
              7: 'Uranus',
              8: 'Neptune'}
    for key, val in planet.items():
        if key == id:
            return val