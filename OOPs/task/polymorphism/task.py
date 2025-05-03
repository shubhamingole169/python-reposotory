class YouTubeVideo:
    def play(self):
        print("Playing YouTube video .....")

class Movie:
    def play(self):
        print("Playing movie from local storage ....")
        
        
def play_video(video):
    video.play()

y = YouTubeVideo()
m = Movie()

play_video(y)
play_video(m)