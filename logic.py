from random import randint
import requests

class Pokemon:
    pokemons = {}

    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1, 1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.weight, self.height = self.get_weight_height()

        # Инициализация уровня счастья
        self.happiness = 0 
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['sprites']['front_default']  # Получаем ссылку на изображение
        return None
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()['forms'][0]['name']
        return "Pikachu"

    # Метод для получения веса и роста покемона
    def get_weight_height(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['weight'], data['height']
        return None, None

    #Метод для кормления покемона
    def feed(self):
        self.happiness += 10  #Увеличиваем уровень счастья
        print(f"{self.name} был покормлен! Уровень счастья: {self.happiness}")

    #Метод класса для получения информации
    def info(self):
        return (
            f"Имя покемона: {self.name}, "
            f"Вес: {self.weight}, Рост: {self.height}, "
            f"Уровень счастья: {self.happiness}"
        )
    
    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

#Пример использования
trainer_name = "Ash"
my_pokemon = Pokemon(trainer_name)
print(my_pokemon.info())
my_pokemon.feed()  #Кормим покемона
print(my_pokemon.info())
