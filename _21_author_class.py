from datetime import datetime

# Author class
class Author:
    def __init__(self, name, nationality, birth_year):
        self.name = name
        self.nationality = nationality
        self.birth_year = birth_year

# Article class that inherits from Author
class Article(Author):
    def __init__(self, name, nationality, birth_year, title, published_year):
        super().__init__(name, nationality, birth_year)
        self.title = title
        self.published_year = published_year

    # Method to simulate publishing an article
    def publish_article(self, title, year):
        self.title = title
        current_year = datetime.now().year
        if year > current_year:
            print(f"Error: Cannot publish '{title}' in the future (Year {year}).")
        else:
            self.published_year = year
            print(f"Article '{title}' has been published in {year}.")

    # Method to display the article's information
    def display_article_info(self):
        print(f"Article Title: {self.title}")
        print(f"Author: {self.name}")
        print(f"Published Year: {self.published_year}")

# Creating two articles and simulating publishing
article1 = Article("John Doe", "American", 1980, "", 0)
article1.publish_article("Understanding AI", 2023)
article1.display_article_info()

article2 = Article("Jane Smith", "British", 1975, "", 0)
article2.publish_article("Advances in Robotics", 2025)  # Simulates future year handling
article2.display_article_info()
