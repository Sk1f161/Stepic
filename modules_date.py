from datetime import date, timedelta

y, m, d = map(int, input().split())
days = input()

day = timedelta(days=int(days))

result = date(y,m,d)+ day
print(result.strftime("%Y %-m %-d"))
