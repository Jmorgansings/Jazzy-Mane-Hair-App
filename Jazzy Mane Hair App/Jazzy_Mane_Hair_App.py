def get_hair_styles(length, occasion):
    #Dictionary to categorize hair styles based on length and occasion
    styles = {
        'short': {
            'formal': ['Pixie Cut', 'Bob Cut', 'Slick Back'],
            'casual': ['Messy Pixie', 'Textured Bob', 'Buzz Cut'],
            'party': ['Elegant Pixie', 'Short Waves', 'Braided Pixie']
        },
        'medium': {
            'formal': ['Shoulde-Length Waves', 'Half Updo', 'Over Shoulder'],
            'casual': ['Beach Waves', 'Simple Bun', 'Messy Hair'],
            'party': ['Loose Curls', 'Half-Up Half-Down', 'Braided  Crown']
        },
        'long': {
            'formal': ['Sleek Straight Hair', 'Long Curls', 'Elegant Updo'],
            'casual': ['Loose Waves', 'High Ponytail', 'Braids'],
            'party': ['Hollywood Waves', 'Fishtail Braid', 'Half-Up Bun']
        }
    }
    
    #Retrive suggested styles based on user input
    return styles.get(length, {}).get(occasion, ["No styles available for this combination."])
    
    def main():
        print("Welcome Jazzy Mane Hair App!")
        print("Please answer the following questions to get a hair style suggestion.\n")
        
        #Get hair length from user
        hair_length = input("What is your hair length? (short, medium, long): ").lower()
        #Get occasion from user
        occasion = input("What is the occasion? (formal, causal, party): ").lower()
        
        #Fetch hair styles suggestions
        suggestions = get_hair_styles(hair_length, occasion)
        
        #Display the suggestion
        print("\nSuggestion Hair Styles:")
        for style in suggestion:
            print(f"-{style}")
            
    if __name__ == "___main__":
        main()
