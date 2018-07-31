import school_scores
lor = school_scores.get_all()

for s in lor:
    print(s["GPA"]["B"]["Verbal"])
