import itertools
input_text = open("input.txt", "r").read().split("\n")

output_unsorted = []
for text in input_text:
    if "." in text:
        output_unsorted.append(text)

print(output_unsorted)

output_majorsorted = []
index = 0
added = 0
while added != len(output_unsorted):
    major = []
    for i in output_unsorted:
        if int(i.split(".")[0]) == index:
            major.append(i)
    if len(major) > 0:
        output_majorsorted.append(major)
        added = added + len(major)
    index = index + 1

print(output_majorsorted)

output_minorsorted = []
added = 0
while added != len(output_unsorted):

    for major in output_majorsorted:
        # We have a list of numbers we have to sort by their second number 20.2.12
        minor = []
        index = 0

        while len(minor) != len(major):
            for i in major:
                if int(i.split(".")[1]) == index:
                    # The middle number is the same as the index
                    minor.append(i)
            # We went through the entire list and added everything with the middle number equaling the index
            index = index + 1

        # minor has been built
        output_minorsorted.append(minor)
        added = added + len(minor)

print(output_minorsorted)

added = 0
output_sorted = []
while added != len(output_unsorted):

    for minor in output_minorsorted:
        # We have a list of numbers we have to sort by their second number 20.2.12
        patch = []
        index = 0

        while len(minor) != len(patch):
            for i in minor:
                if "+" in i:
                    compare = i[i.index(".",3)+1:i.index("+")]
                elif "-" in i:
                    compare = i[i.index(".",3)+1:i.index("-")]
                else:
                    compare = i[i.index(".",3)+1]
                if int(compare) == index:
                    patch.append(i)
            # We went through the entire list and added everything with the middle number equaling the index
            index = index + 1

        # minor has been built
        output_sorted.append(patch)
        added = added + len(patch)

print(output_sorted)
