player = {
"name": "Osimhen",
"goals": "25",
"club": "Napoli",
"nationality": "Nigerian"
}

print(player["name"])
print(player["goals"])

# Professional way — uses the actual dictionary values
print(f"{player['name']} has scored {player['goals']} goals for {player['club']}")