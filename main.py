import csv
import os
from time import sleep

import discogs_client as dc
from discogs_client.exceptions import HTTPError

import track as t


def main():
    # user input
    token = input("Paste your token: \n")
    filename = input("Please enter the name of the csv file: \n")  # TODO delete
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

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter="\t")
        header = open("header.txt", "r").read().split("\n")
        writer.writerow(header)
        write_release_data(release_ids, client, writer)


def write_release_data(release_ids, client, writer):
    # iterate through all releases
    for release_id in release_ids:
        release = client.release(release_id)

        # get all data of the release
        catno = release.labels[0].catno
        year = release.year
        album = release.title
        album_artists = get_album_artists(release)
        label = release.labels[0].name
        genre = get_genres(release)
        subgenre = get_subgenres(release)
        format = get_format(release)

        # TODO refactoring
        # iterate through all tracks of the release
        for track in release.tracklist:
            duration = convert_duration(duration_raw=track.duration)
            position = track.position
            track_artists = get_track_artists(track, album_artists)
            track_object = t.Track(
                str(release_id) + "_" + position,
                catno,
                year,
                album,
                album_artists,
                track_artists,
                position,
                label,
                genre,
                subgenre,
                track.title,
                duration,
                format,
            )
            t.Track.logging(track_object)
            writer.writerow(t.Track.get_values(track_object))
            sleep(0.25)


def get_album_artists(release) -> str:
    return (
        " & ".join([artist.name for artist in release.artists])
        if len(release.artists) > 0
        else release.artists[0]
    )


def get_track_artists(track, album_artist: str) -> str:
    return (
        " & ".join([artist.name for artist in track.artists])
        if len(track.artists) > 0
        else album_artist
    )


def get_genres(release) -> str:
    return "_".join(release.genres) if len(release.genres) > 0 else release.genres[0]


def get_subgenres(release) -> str:
    return "_".join(release.styles) if release.styles else ""


def convert_duration(duration_raw: str) -> str:
    if not duration_raw:
        return ""
    durations = duration_raw.split(":")
    sec = int(durations[0]) * 60 + int(durations[1])
    return str(sec) + ".000" if len(durations) == 2 else str(sec) + "." + durations[2]


def get_format(release) -> str:
    format = release.formats[0]["name"]
    if "descriptions" in release.formats[0]:
        format += "_"
        for description in release.formats[0]["descriptions"]:
            format += description + "_"
    # delete last "_"
    return format[:-1]


if __name__ == "__main__":
    main()
