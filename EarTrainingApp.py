import os
import random
import pygame

pygame.mixer.init()

# اسم نت‌ها
natural_notes = [
    "C", "D", "E", "F", "G", "A", "B"
]

chromatic_notes = [
    "C", "C#",
    "D", "D#",
    "E",
    "F", "F#",
    "G", "G#",
    "A", "A#",
    "B"
]

# Easy:
# نت‌های طبیعی فقط در اکتاو 4
easy_notes = [
    "C4", "D4", "E4",
    "F4", "G4", "A4", "B4"
]

# Medium:
# تمام نت‌های طبیعی در 3 اکتاو

medium_notes = []
for octave in(3,4,5):
    for note in natural_notes:
      medium_notes.append(f'{note}{octave}')



flat_to_sharp = {
    'DB' : 'C#' ,
    'EB' : 'D#' ,
    'GB' : 'F#' ,
    'AB' : 'G#' ,
    'BB' : 'A#'
    }


# hard:
# تمام نت‌ها همراه دیز، فقط در اکتاو 4
hard_notes = [
    "C4", "C#4",
    "D4", "D#4",
    "E4",
    "F4", "F#4",
    "G4", "G#4",
    "A4", "A#4",
    "B4"
]

# expert و Extreme:
# تمام نت‌ها در اکتاوهای 3، 4 و 5
all_octave_notes = []

for octave in [3, 4, 5]:

    for note in chromatic_notes:

        full_note = f"{note}{octave}"

        all_octave_notes.append(full_note)

# پخش صدا
def play_note(note):

    file_path = os.path.join(os.path.dirname(__file__),
                'sounds' ,
                f'{note}.wav')
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # صبر می‌کند تا صدا کامل تمام شود
    while pygame.mixer.music.get_busy():

        pygame.time.wait(10)

# انتخاب تعداد راند
def choose_rounds():

    while True:

        answer = input(
            "\nHow many rounds do you wanna play? "
            " press Q to quit: "
        ).strip().upper()

        if answer == "Q":

            return None

        if answer.isdigit():

            rounds = int(answer)

            if rounds > 0:

                return rounds

        print(
            "Please enter a number greater than 0."
        )

# انتخاب درجه سختی
def choose_difficulty():

    while True:

        print("\nChoose difficulty:")
        print("\n1 - Easy:"
              ' natural notes in octave 4'
              
              
              )
        print("\n2 - Medium:"
              ' natural notes in octave 3, 4, 5'
              
              )
        print("\n3 - Hard:"
              ' natural and sharp notes in octave 4'
              )
        print("\n4 - expert:"
              ' natural and sharp notes in octave 3, 4, 5'
              
              
              )
        print("\n5 - extreme:"
              ' natural and sharp notes in octave 3, 4, 5 ' 
              ' octave number is required!' 
    
              
              )
        print("\nQ - Quit")

        choice = input(
            "\nenter Your choice: "
        ).strip().upper()

        if choice == "1":

            return easy_notes, "easy"

        elif choice == "2":

            return medium_notes, "medium"

        elif choice == "3":

            return hard_notes, "hard"

        elif choice == "4":

            return all_octave_notes, "expert"
        
        elif choice == "5":

            return all_octave_notes, "extreme"

        elif choice == "Q":

            return None

        else:

            print("Invalid choice.")

# پرسیدن یک نت
def ask_note(notes, difficulty):

    random_note = random.choice(notes)

    play_note(random_note)

    # در Extreme باید اکتاو هم گفته شود
    if difficulty == "extreme":

        correct_answer = random_note

        valid_answers = all_octave_notes 

    # در بقیه حالت‌ها اکتاو مهم نیست
    else:

        # مثلاً F#5 تبدیل می‌شود به F#
        correct_answer = random_note[:-1]

        if difficulty in ["easy" , 'medium'] :

            valid_answers = natural_notes

        else:

            valid_answers = chromatic_notes



    def is_it_correct(answer):
        if answer not in valid_answers:

            if difficulty == "extreme":

                 print(
                    "Invalid answer. "
                    "Examples: C4 or F#5"
                )

            else:

                print(
                    "Invalid answer. "
                    "Examples: C or F#"
                )
            return None
        elif answer == correct_answer:

            print("Correct!")

            return True

        else:

            print(
                f"Wrong! "
                f"Correct answer: {correct_answer}"
            )

            return False

    while True:

        answer = input(
            "\nGuess the note,"
            "R to replay, "
            "or Q to quit: "
        ).strip().upper()

        if answer == "R":

            play_note(random_note)

        elif difficulty == 'extreme' and answer[:-1] in flat_to_sharp:
            answer = flat_to_sharp[answer[:-1]] + answer[-1]
            result = is_it_correct(answer)
            if result is not None:
                return result
            


        elif answer in flat_to_sharp:
            answer = flat_to_sharp[answer]
            result = is_it_correct(answer)
            if result is not None:
                return result
        
        elif answer == "Q":

            return "quit"
        else:
            result = is_it_correct(answer)
            if result is not None:
                return result


# اجرای اصلی بازی
def main():

    print("======================")
    print("  Ear Training Game")
    print("======================")

    rounds = choose_rounds()

    if rounds is None:

        print("Goodbye!")

        return

    difficulty_result = choose_difficulty()

    if difficulty_result is None:

        print("Goodbye!")

        return

    notes, difficulty = difficulty_result

    score = 0

    for round_number in range(
        1,
        rounds + 1
    ):

        print(
            f"\n----- Round "
            f"{round_number}/{rounds} -----"
        )

        result = ask_note(
            notes,
            difficulty
        )

        if result == "quit":

            print("\nGame stopped.")

            print(
                f"Your score: {score}"
            )

            return

        if result is True:

            score += 1

        print(
            f"Current score: {score}"
        )

    percentage = round(
        score / rounds * 100,
        1
    )

    print("\n======================")
    print("      Game Over")
    print("======================")

    print(
        f"Final score: "
        f"{score}/{rounds}"
    )

    print(
        f"Percentage: "
        f"{percentage}%"
    )

main()

pygame.quit()

