import requests as r

save_def = list()
save_exp = list()
save = " "


def Word_Generator():
    global save
    res = r.get("https://random-word-api.vercel.app/api?words=1&type=capitalized")
    save = str(res.text[2:len(res.text) - 2])
    return str(res.text[2:len(res.text) - 2])


def Saving():
    a = input("Are you want to store this definitions(Y/N)")
    if a == 'Y':
        with open(f"{save}.txt", 'w') as file:
            for i in range(len(save_def)):
                file.write(f"{save}:{save_def[i]}\n")
                file.write(f"Example:{save_exp[i]}\n\n")
            print(f"Data stored in file name -->{save}<--")
    elif a == 'N':
        print("Data lost")
    else:
        print("Wrong input")


def Meaning():
    global save_def, save_exp
    word = Word_Generator()
    try:
        res = r.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        data = res.json()

        for entry in data:
            meanings = entry['meanings']
            for meaning in meanings:
                definitions = meaning['definitions']
                for definition in definitions:
                    save_def.append(definition['definition'])
                    print(f"{word}: {definition['definition']}")
                    if 'example' in definition:
                        save_exp.append(definition['example'])
                        print(f"Example: {definition['example']}")
                    else:
                        save_exp.append("---")
                        print(f"Example: ---")
                    print()
        if __name__ == "__main__":
            Saving()
    except Exception as e:
        print(f"Error:{e}")


if __name__ == "__main__":
    Meaning()
