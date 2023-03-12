#! python3

import os
import csv
import track as t
from retry import retry
from fp.fp import FreeProxy
from itertools import cycle
import discogs_client as dc
from discogs_client.exceptions import HTTPError


def main():
    # user input
    token = input("Paste your token: \n")
    filename = input("Please enter the name of the csv file: \n")
    filename += ".csv" if not filename.endswith(".csv") else ""
    
    # connect to discogs client with token
    client = dc.Client("DiscogsCollector", user_token=token)

    # creates list of all releases of the personal user collection
    release_ids = [
        release.id for release in client.identity().collection_folders[0].releases
    ]

    # delete file if exists (otherwise multiple executions would append the data to the same file)
    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, "a", encoding="UTF8") as file:
        writer = csv.writer(file, delimiter=";")
        header = [
            "id",
            "year",
            "album",
            "artist",
            "label",
            "genre",
            "title",
            "position",  # TODO if empty -> no write
            "duration",
        ]
        writer.writerow(header)

        gen_and_write_track_data(release_ids, client, writer)


@retry(HTTPError, tries=-1)
def gen_and_write_track_data(release_ids, client, writer):
    proxy_list = get_proxies()
    proxy_cycle = cycle(proxy_list)

    # releases
    for id in release_ids:
        release = client.release(id)

        year = str(release.year)
        album = release.title
        artist = release.artists[0].name
        label = release.labels[0].name
        genre = release.genres[0]

        tracklist = release.tracklist

        # tracks
        for star_track in tracklist:
            duration = t.Track.duration_to_ms(
                star_track, duration_raw=star_track.duration
            )
            track = t.Track(
                id,
                year,
                album,
                artist,
                label,
                genre,
                star_track.title,
                star_track.position,
                duration,
            )

            logging(id, year, album, artist, label, genre, star_track, duration)

            writer.writerow(t.Track.get_values(track))

            change_proxy(proxy_cycle)


def logging(id, year, album, artist, label, genre, star_track, duration):
    print("id: " + str(id))
    print("year: " + year)
    print("album: " + album)
    print("artist: " + artist)
    print("label: " + label)
    print("genre: " + genre)
    print("title: " + star_track.title)
    print("position: " + star_track.position)
    print("duration: " + str(duration))
    print("------------------------------")

@retry(tries=10, delay=1, jitter=1, max_delay=4)
def get_proxies(number:int=5, anonym:bool=True, google:bool=False, https:bool=True, country_ids:list[str]=None) -> list:
    proxies = []
    for i in range(number):
        proxies += [FreeProxy(rand=True,
                            anonym=anonym,
                            google=google,
                            https=True,country_id=country_ids
                            ).get()]
    return proxies

def change_proxy(proxy_cycle):
    os.environ['HTTPS_PROXY'] = next(proxy_cycle)

if __name__ == "__main__":
    main()
