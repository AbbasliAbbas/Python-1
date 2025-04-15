#Tapsiriq 5
course = {
    "name": "Full-Stack Python",
    "duration": 6,
    "topics": ["Python", "SQL", "API", "Docker"]
}


course["topics"].append("React")


course["duration"] += 1

if "API" in course["topics"]:
    print("API movzusu oyrenilecek")


print("Yeni course", course)