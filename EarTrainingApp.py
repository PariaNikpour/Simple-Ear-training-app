import random
import pygame 


pygame.mixer.init()
notes_list = [ 'C', 'D','E','F','G','A','B' ]
score = 0
def name_the_note():
    global score
    random_note = random.choice(notes_list)
    #file_path = 'path.random_note'
    #uncomment the line above , and write down the path to your notes wavs. then for actually access each note, you should write down the wav file's name but replace the part (a,b,c, ...) with random_note variable
    pygame.mixer.music.load(file_path)
    while True :

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        action = input('guess the note or press r to replay').upper()

        if action == 'R':
            continue
        elif action in notes_list:
             guess = action
             break
        else:
            print('invalid answer')
            
    if random_note == guess :
        score +=1
        print('YAY')
    else : 
        print('OOPS',f'right answer = {random_note}')
        return

for i in range(3):
    name_the_note()
print(f'game over , Total_score: {score}')
