import requests

endpoint = "http://localhost:8000/api/"

r = requests.get(endpoint, json={"link":"https://youtu.be/c708Nf0cHrs?list=PLEsfXFp6DpzRKcXDuQq0mYbqGy62yZH-T"})
print(r.json())