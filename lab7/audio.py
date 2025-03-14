import pygame
import os

pygame.init()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Music Player")

pygame.mixer.init()

music_dir = "music"  
tracks = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
current_track = 0

def play_track(index):
    if 0 <= index < len(tracks):
        pygame.mixer.music.load(tracks[index])
        pygame.mixer.music.play()
        print(f"Now playing: {os.path.basename(tracks[index])}")
    else:
        print("No more tracks.")
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

def next_track():
    global current_track
    current_track = (current_track + 1) % len(tracks)
    play_track(current_track)
    
def previous_track():
    global current_track
    current_track = (current_track - 1) % len(tracks)
    play_track(current_track)

running = True
paused = False
play_track(current_track) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: 
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                    print("Music paused.")
                else:
                    if paused:
                        pygame.mixer.music.unpause()
                        paused = False
                        print("Music resumed.")
                    else:
                        play_track(current_track)
            elif event.key == pygame.K_s: 
                stop_music()
            elif event.key == pygame.K_n:  
                next_track()
            elif event.key == pygame.K_b: 
                previous_track()
pygame.quit()