class Audio:
    #Users can create audio using URLs available online.
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.ratings = []
    #Users can give ratings to playlist and audio
    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
    #Rating displayed is the average rating calculated 
    def audio_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0
    
class Playlist:
    #Users can create multiple Playlists based on the genre of the song.
    def __init__(self, genre, name):
        self.genre = genre
        self.name = name
        self.audio_files = []
        self.ratings = []
#Users can add multiple audio files into each playlist created.
    def add_audio(self, audio):
        self.audio_files.append(audio)
#randomly generate ratings from 1 to 5.
    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def playlist_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0
    
class AudioLibrary:
    def __init__(self):
        self.audio_collection = []
        self.playlists = []
#create audio and append to audio collections
    def create_audio(self, name, url):
        audio = Audio(name, url)
        self.audio_collection.append(audio)
        return audio
#create playlist and append to playlists
    def create_playlist(self, genre, name):
        playlist = Playlist(genre, name)
        self.playlists.append(playlist)
        return playlist
#Users can search audio by name.
    def search_audio_by_name(self, name):
        for audio in self.audio_collection:
            if audio.name == name:
                return audio
        return None
#Users can search the playlist by name
    def search_playlist_by_name(self, name):
        for playlist in self.playlists:
            if playlist.name == name:
                return playlist
        return None    
# Example usage
if __name__ == "__main__":
    library = AudioLibrary()

    # Creating some audio files
    audio1 = library.create_audio("User1", "http://example.com/song1")
    audio2 = library.create_audio("User2", "http://example.com/song2")
    audio3 = library.create_audio("User3", "http://example.com/song3")
    # Creating playlists
    playlist1 = library.create_playlist("Pop", "Pop Hits")
    playlist2 = library.create_playlist("Rock", "Rock Classics")
    playlist3 = library.create_playlist("Western", "Party")
    # Adding audio files to playlists
    playlist1.add_audio(audio1)
    playlist1.add_audio(audio2)
    playlist3.add_audio(audio2)

    # Rating audio files and playlists
    audio1.add_rating(4)
    audio2.add_rating(2)
    audio3.add_rating(5)
    playlist1.add_rating(4)
    playlist2.add_rating(3)
    playlist3.add_rating(5)

    # Displaying average ratings
    print("<--------------------USER1----------------------->")
    print(f"Audio '{audio1.name}': Average Rating - {audio1.audio_average_rating()}")
    print(f"Playlist '{playlist1.name}': Average Rating - {playlist1.playlist_average_rating()}")

    print("<--------------------USER2----------------------->")
    print(f"Audio '{audio2.name}': Average Rating - {audio2.audio_average_rating()}")
    print(f"Playlist '{playlist2.name}': Average Rating - {playlist2.playlist_average_rating()}")

    print("<--------------------USER3----------------------->")
    print(f"Audio '{audio3.name}': Average Rating - {audio2.audio_average_rating()}")
    print(f"Playlist '{playlist3.name}': Average Rating - {playlist3.playlist_average_rating()}")
    print("<-------------------------------------------------->")
