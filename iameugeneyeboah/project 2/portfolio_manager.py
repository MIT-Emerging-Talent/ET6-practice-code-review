import json
import os
from datetime import datetime


class Photo:
    def __init__(self, title, description, category, date_taken):
        self.title = title
        self.description = description
        self.category = category
        self.date_taken = date_taken

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "date_taken": self.date_taken,
        }

    @staticmethod
    def from_dict(photo_dict):
        return Photo(
            photo_dict["title"],
            photo_dict["description"],
            photo_dict["category"],
            photo_dict["date_taken"],
        )


class PortfolioManager:
    def __init__(self, file_name="portfolio.json"):
        self.file_name = file_name
        self.photos = self.load_portfolio()

    def load_portfolio(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                data = json.load(file)
                return [Photo.from_dict(photo) for photo in data]
        return []

    def save_portfolio(self):
        with open(self.file_name, "w") as file:
            data = [photo.to_dict() for photo in self.photos]
            json.dump(data, file)

    def add_photo(self, title, description, category, date_taken):
        new_photo = Photo(title, description, category, date_taken)
        self.photos.append(new_photo)
        self.save_portfolio()

    def search_photos(self, category=None, date_range=None, keyword=None):
        results = self.photos
        if category:
            results = [
                photo for photo in results if photo.category.lower() == category.lower()
            ]
        if date_range:
            start_date, end_date = date_range
            results = [
                photo
                for photo in results
                if start_date
                <= datetime.strptime(photo.date_taken, "%Y-%m-%d")
                <= end_date
            ]
        if keyword:
            results = [
                photo
                for photo in results
                if keyword.lower() in photo.title.lower()
                or keyword.lower() in photo.description.lower()
            ]
        return results

    def edit_metadata(self, title, new_title=None, new_description=None):
        for photo in self.photos:
            if photo.title == title:
                if new_title:
                    photo.title = new_title
                if new_description:
                    photo.description = new_description
                self.save_portfolio()
                return photo
        return None

    def delete_photo(self, title):
        self.photos = [photo for photo in self.photos if photo.title != title]
        self.save_portfolio()

    def view_portfolio(self):
        return self.photos


def print_photo_details(photos):
    for photo in photos:
        print(f"Title: {photo.title}")
        print(f"Category: {photo.category}")
        print(f"Description: {photo.description}")
        print(f"Date Taken: {photo.date_taken}")
        print("-" * 30)


def main():
    portfolio = PortfolioManager()

    while True:
        print("\n1. Add Photo")
        print("2. Search Photos")
        print("3. Edit Metadata")
        print("4. Delete Photo")
        print("5. View Portfolio")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title: ")
            description = input("Enter description: ")
            category = input("Enter category: ")
            date_taken = input("Enter date taken (YYYY-MM-DD): ")
            portfolio.add_photo(title, description, category, date_taken)
        elif choice == "2":
            category = input("Enter category to search (or press Enter to skip): ")
            date_range_input = input(
                "Enter date range (YYYY-MM-DD to YYYY-MM-DD) or press Enter to skip: "
            )
            keyword = input(
                "Enter keyword to search for in title/description or press Enter to skip: "
            )

            date_range = None
            if date_range_input:
                start_date, end_date = date_range_input.split(" to ")
                date_range = (
                    datetime.strptime(start_date, "%Y-%m-%d"),
                    datetime.strptime(end_date, "%Y-%m-%d"),
                )

            results = portfolio.search_photos(
                category=category, date_range=date_range, keyword=keyword
            )
            print_photo_details(results)
        elif choice == "3":
            title = input("Enter title of the photo to edit: ")
            new_title = input("Enter new title (or press Enter to skip): ")
            new_description = input("Enter new description (or press Enter to skip): ")
            updated_photo = portfolio.edit_metadata(title, new_title, new_description)
            if updated_photo:
                print(f"Updated: {updated_photo.title}")
            else:
                print("Photo not found.")
        elif choice == "4":
            title = input("Enter title of the photo to delete: ")
            portfolio.delete_photo(title)
            print("Photo deleted.")
        elif choice == "5":
            photos = portfolio.view_portfolio()
            print_photo_details(photos)
        elif choice == "6":
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
