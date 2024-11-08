
def city_country(city, country, population=None):
    # Return a city and country, optionally with population, neatly formatted.
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
