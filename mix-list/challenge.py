#!/usr/bin/python3
movies = [{"scifi":{"best":"matrix","worst":"matrix reloaded"}},{"comedy":{"best":"spaceballs","worst":"click"}},{"horror":{"best":"conjuring","worst":"glass house"}},]
print("Pick a genre from scifi, horror, or comedy")
genre = input(">")
print("Pick best or worst of the genre")
choice = input(">")

x = 0
for test in movies:
    if genre in test.keys():
       print(f"The {choice} {genre} film is: {test[genre][choice]}")
