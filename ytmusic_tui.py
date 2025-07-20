import subprocess
from ytmusicapi import YTMusic
from rich.console import Console
from rich.table import Table

console = Console()
ytmusic = YTMusic()

def search_music(query):
    results = ytmusic.search(query, filter="songs")
    return results[:10]  # limit hasil biar rapih

def display_results(results):
    table = Table(title="Search Results")
    table.add_column("Index", style="cyan")
    table.add_column("Title", style="magenta")
    table.add_column("Artist", style="green")

    for idx, track in enumerate(results):
        table.add_row(str(idx), track["title"], track["artists"][0]["name"])
    console.print(table)

def play_song(video_id):
    url = f"https://music.youtube.com/watch?v={video_id}"
    subprocess.run(["mpv", url])

def main():
    query = input("Search YouTube Music: ")
    results = search_music(query)
    display_results(results)

    choice = int(input("Enter song index to play: "))
    selected = results[choice]
    console.print(f"[bold yellow]Playing:[/bold yellow] {selected['title']} - {selected['artists'][0]['name']}")
    play_song(selected['videoId'])

if __name__ == "__main__":
    main()
