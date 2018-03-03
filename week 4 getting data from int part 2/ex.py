def get_recipes(keywords):
    recipe_list = list()
    import requests
    from bs4 import BeautifulSoup
    url = "http://www.epicurious.com/search/" + keywords
    response = requests.get(url)
    if not response.status_code == 200:
        return None
    try:
        results_page = BeautifulSoup(response.content, 'lxml')
        recipes = results_page.find_all('article', class_="recipe-content-card")
        for recipe in recipes:
            recipe_link = "http://www.epicurious.com" + recipe.find('a').get('href')
            recipe_name = recipe.find('a').get_text()
            print(recipe_name)
            try:
                recipe_description = recipe.find('p', class_='dek').get_text()
            except:
                recipe_description = ''
            recipe_list.append((recipe_name, recipe_link, recipe_description))
        return recipe_list
    except:
        return None


get_recipes('Tofu chili')

recipe_link = "http://www.epicurious.com" + '/recipes/food/views/spicy-lemongrass-tofu-23384'


def get_recipe_info(recipe_link):
    recipe_dict = dict()
    import requests
    from bs4 import BeautifulSoup
    try:
        response = requests.get(recipe_link)
        if not response.status_code == 200:
            return recipe_dict
        result_page = BeautifulSoup(response.content, 'lxml')
        ingredient_list = list()
        prep_steps_list = list()
        for ingredient in result_page.find_all('li', class_='ingredient'):
            ingredient_list.append(ingredient.get_text())
        for prep_step in result_page.find_all('li', class_='preparation-step'):
            prep_steps_list.append(prep_step.get_text().strip())
        recipe_dict['ingredients'] = ingredient_list
        recipe_dict['preparation'] = prep_steps_list
        return recipe_dict
    except:
        return recipe_dict


get_recipe_info(recipe_link)


def get_all_recipes(keywords):
    results = list()
    all_recipes = get_recipes(keywords)
    for recipe in all_recipes:
        recipe_dict = get_recipe_info(recipe[1])
        recipe_dict['name'] = recipe[0]
        recipe_dict['description'] = recipe[2]
        results.append(recipe_dict)
    return(results)


get_all_recipes("Tofu chili")

from bs4 import BeautifulSoup

text = '<div class_="special"> <a href="http://www.somelink.com">Special link</a>'

A = BeautifulSoup(text, 'lxml').find_all('div', class_='special').get_text()


print(A)
