import datetime 

since = datetime.datetime(1970, 1, 1)
now = datetime.datetime.now()
seconds = (now - since).total_seconds()
scientific = "{:.2e}".format(seconds)

print(f"Seconds since January 1, 1970: {seconds:,.4f} or {scientific} in scientific notation")
print(now.strftime("%b %d %Y"))