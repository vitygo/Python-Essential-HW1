import json
import os

class URLShortener:
    def __init__(self, filename="link.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump([], file)

    def add_url(self, short_link, full_link):
        short_link = short_link.lower().strip()
        full_link = full_link.lower().strip()

        with open(self.filename, "r") as file:
            link_data = json.load(file)

        # Перевіряємо, чи вже існує коротке посилання
        for link in link_data:
            if link['short_link'] == short_link:
                raise ValueError(f"Посилання з назвою '{short_link}' вже існує.")

        # Додаємо нове посилання
        link_data.append({"short_link": short_link, "full_link": full_link})

        with open(self.filename, "w") as file:
            json.dump(link_data, file, indent=4)

    def get_url(self, short_link):
        short_link = short_link.lower().strip()

        with open(self.filename, 'r') as file:
            link_data = json.load(file)

        for link in link_data:
            if link["short_link"] == short_link:
                return link['full_link']

        raise ValueError(f"Посилання з назвою '{short_link}' не знайдено.")
