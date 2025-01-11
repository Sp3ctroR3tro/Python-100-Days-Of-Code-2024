
with open("./Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt", "r") as letter:
    current_letter = letter.read()

with open("./Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt", "r") as names:
    names = names.readlines()
    for name in names:
        name = name.strip()
        new_letter = current_letter.replace("[name]", name)
        with open(f"./Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letter_for_{name}.txt", "w") as finished_letter:
            finished_letter.write(new_letter)