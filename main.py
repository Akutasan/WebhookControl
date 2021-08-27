import requests

url = "https://discord.com/api/webhooks/879775144342614097/" \
      "-lBTYBVecM-DPeQMgK7qyNaXwvwCKsLmwJ1CM26EMIiR8XwhatLctSjilPkZX-HC6bs5"

print(requests.post(url, data="wowowow"))
