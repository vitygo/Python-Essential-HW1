class NotValidGenreError(Exception):
    def __init__(self, genre, message="invalid genere error"):
        self.genre = genre
        self.message = message
        super().__init__(self.message) 
    
def validate_genre(user_input:str) -> str:
    if user_input in ["rock", "pop", "jazz", "classical", "rap"]:
        return True
    else:
        raise NotValidGenreError(user_input)
    

def main():
    user_input = input("Enter your favorite music genre: ").strip().lower()
    try:
        result = validate_genre(user_input)
        if result:
            print(f"{user_input} is valid music genre")
    except NotValidGenreError as e:
        print(f"Error: {e}")

main()