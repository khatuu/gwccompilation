def translate_shorthand(dict) :
    answer = input("(define a shorthand)")
    if answer in slangs.keys() :
        for key, value in dict.items() :
            print(value)

slangs() = {
"ttyl" : "talk to you later",
"omg" : "oh my gawd",
"wtf" : "what the fark",
"l8r" : "later"
}

translate_shorthand(slangs)
