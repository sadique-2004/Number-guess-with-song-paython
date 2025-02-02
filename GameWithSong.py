import pygame
import time

def main():
    # Initialize the mixer for playing music
    pygame.mixer.init()

    # Start the game
    print("Welcome to the simple game!")
    print("---------------------------")
    user_name = input("Please enter your name: ").strip()
    
    if user_name:
        print(f"\nWelcome, {user_name}! Get ready to enjoy the game and some music 🎵.")
    else:
        print("\nYou did not enter a name! Defaulting to 'Player'. Welcome, Player!")

    # Load the music
    music_file = "music.mp3"
    try:
        pygame.mixer.music.load(music_file)
    except pygame.error as e:
        print(f"\nError: Could not find or load {music_file}. Please ensure it is in the same folder.")
        return
    
    # Start the game message with music
    print("\nStarting your music now!")
    pygame.mixer.music.play()
    
    # Simple game interaction (guess the number)
    print("\nLet's play a simple number game!")
    print("I am thinking of a number between 1 and 10.")
    target_number = 7  # The correct answer
    
    for attempt in range(5):
        try:
            guess = int(input("Take a guess: "))
            if guess == target_number:
                print("\n🎉 Congratulations! You guessed the correct number!")
                break
            elif guess < target_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

    # If the player didn't guess correctly
    else:
        print(f"\nBetter luck next time! The number was {target_number}.")
    
    print("\nThank you for playing, and enjoy the music 🎶.")
    print("You can close the program when you're done listening.")
    
    # Keep music playing until it ends
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    pygame.mixer.quit()


if __name__ == "__main__":
    main()
