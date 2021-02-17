def greet(language):
    """ 
    This function returns a greeting eturns a greeting - if you have it in your database. 
    It should default to English if the language is not in the database, or in the event of an invalid input.
    """
    greet_language = {'english': 'Welcome',
                      'czech': 'Vitejte',
                      'danish': 'Velkomst',
                      'dutch': 'Welkom',
                      'estonian': 'Tere tulemast',
                      'finnish': 'Tervetuloa',
                      'flemish': 'Welgekomen',
                      'french': 'Bienvenue',
                      'german': 'Willkommen',
                      'irish': 'Failte',
                      'italian': 'Benvenuto',
                      'latvian': 'Gaidits',
                      'lithuanian': 'Laukiamas',
                      'polish': 'Witamy',
                      'spanish': 'Bienvenido',
                      'swedish': 'Valkommen',
                      'welsh': 'Croeso'}
    for key, val in greet_language.items():
        if key == language:
            return val
    return 'Welcome'