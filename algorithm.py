import sqlite3
from collections import Counter

videos = [
 {"title":"Python Mastery","cat":"coding"},
 {"title":"Gym Beast","cat":"fitness"},
 {"title":"AI Future","cat":"tech"},
 {"title":"BGMI Pro","cat":"gaming"},
 {"title":"Web Dev","cat":"coding"},
]

def recommend(user):
    db = sqlite3.connect("database.db")
    data = db.execute("SELECT category FROM history WHERE user=?",(user,)).fetchall()

    if not data:
        return videos

    cats = [i[0] for i in data]
    fav = Counter(cats).most_common(1)[0][0]

    rec = [v for v in videos if v["cat"]==fav]
    return rec
