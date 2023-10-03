from datetime import date


class Track:
    def __init__(
        self,
        externalid,
        catno,
        year,
        album,
        artist,
        position,
        label,
        genre,
        subgenre,
        title,
        duration,
        format,
    ):
        # TODO sanatize
        self.id = ""
        self.externalid = externalid
        self.catno = catno
        if year == 0:
            self.year = ""
            self.decade = ""
        else:
            self.year = str(year)
            self.decade = self.year[0:-1] + "0"
        self.album = album
        self.artist = artist
        self.position = position
        self.label = label
        self.genre = genre
        self.subgenre = subgenre
        self.title = title
        self.duration = duration
        self.format = str(format)
        self.date = str(date.today())
        pass

    def logging(self):
        print("externalid: " + self.externalid)
        print("catalog no: " + self.catno)
        print("year: " + self.year)
        print("decade: " + self.decade)
        print("album: " + self.album)
        print("artist: " + self.artist)
        print("position: " + self.position)
        print("label: " + self.label)
        print("genre: " + self.genre)
        print("subgenre: " + self.subgenre)
        print("title: " + self.title)
        print("duration: " + self.duration)
        print("format: " + self.format)
        print("date: " + self.date)
        print("------------------------------")

    def get_header(self) -> list[str]:
        header = []
        for key in self.__dict__.keys():
            header.append(str(key))
        return header

    def get_values(self) -> str:
        return [str(self.__dict__[key]) for key in self.get_header()]
