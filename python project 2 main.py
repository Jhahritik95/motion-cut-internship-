def count_words(text):	
    """
    Counts the number of words in the given text.
    
    Args:
    text (str): The input text to count words in.
    
    Returns:
    int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def main():
    """
    Main function to run the word counter program.
    """
    print("Welcome to the Word Counter Program!")
    print("Please enter a sentence or paragraph:")
    
    # Get user input
    user_input = input("Input: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: The input is empty. Please enter some text.")
    else:
        # Count words
        word_count = count_words(user_input)
        # Display the word count
        print(f"The number of words in the input text is: {word_count}")

# Run the main function
if __name__ == "__main__":
    main()

