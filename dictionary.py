fandf = {
    'Khatu':15,
    'Helen':45,
    'Ricky':20,
    'Veronica':15,
    'Kayla':17,
    'Tammie':15,
    'Kylie':15,
    'Jonelle':18,
    'Joseph':18,
    'Mark':18,
    'Titan':18,
    'Tyler':18,
    'Nina':16,
    'Jaclyn':16,
    'Shannon':15,
    'Gina':16,
    'Cathy':18,
}

total_age = 0

for key,value in fandf.items():
    total_age = total_age + value

print(total_age / len(fandf))
