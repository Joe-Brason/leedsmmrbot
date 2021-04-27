import datetime
date_string = "2021-04-12T00:00:00+00:00"
x = datetime.datetime.fromisoformat(date_string)
print(type(x))

a = "2021-03-23T00:00:00+00:00"
b = "2021-03-09T00:00:00+00:00"

print(a>b)