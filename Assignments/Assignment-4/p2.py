'''
Create a class Book  with the following attributes:
• title 
• author 
• list of reviews
And add methods to: 
• add a new review 
• count reviews 
• display all reviews
'''

class Book:
    def __init__(self, title, author, list_of_reviews = []):
        self.title = title
        self.author = author
        self.list_of_reviews = list_of_reviews

    def add_review(self, review):
        self.list_of_reviews.append(review)

    def count_reviews(self):
        print(f"{self.title} has {len(self.list_of_reviews)} reviews")

    def display_reviews(self):
        print("Following are the reviews:")
        for i in range(len(self.list_of_reviews)):
            print(f"{i+1}. {self.list_of_reviews[i]}")


if __name__ == "__main__":
    book1 = Book("Think Straight", "Darius Foroux", ["It's an amazing read", "Good read", "Really helpful", "Highly Recommend"])

    print("\n--- Displaying reviews ---")
    book1.display_reviews()

    print("\n--- Adding Review ---")
    book1.add_review("Love it")
    book1.display_reviews()

    print("\n--- Counting Reviews ---")
    book1.count_reviews()