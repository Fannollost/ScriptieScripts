import pandas as pd
import csv


def writeToCSV(file_path, key_name, value_name, pairs):
    with open(file_path, 'w', newline='',  encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([key_name, value_name])
        for key,value in pairs.items():
            writer.writerow([key,value])

def writeOmitted(file_path):
    with open(file_path, 'w', newline='',  encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow("Omitted")
        for o in omitted:
            writer.writerow(o)


df = pd.read_csv("lsc22_metadata.csv")

df = pd.read_csv("lsc22_visual_concepts.csv")

vtags = {}
ctags = {}
omitted = []
for index, row in df.iterrows():
    print(index)
    tag = row["Tags"]
    if(type(tag)!= str):
        omitted.append(row["ImageID"])
        continue

    if(tag == "nan"):
        omitted.append(row["ImageID"])
        continue

    if(tag.lower() == "NaN"):
        omitted.append(row["ImageID"])
        continue

    caption = row["Caption"]
    concepts = caption.split(' ')
    cFilter = ['a', 'with', 'on', 'and', 'of', 'in', 'the', 'at', 'using']
    for c in concepts:
        if(c in cFilter):
            continue

        if(c not in ctags.keys()):
            ctags[c] = 1
        else:
            ctags[c] += 1

    tags = tag.split(',')
    for t in tags:
        if(t not in vtags.keys()):
            vtags[t] = 1
        else:
            vtags[t] += 1


filteredTags = {}
omittedTags = {}

for v in vtags:
    if vtags[v] > 10:
        filteredTags[v] = vtags[v]
        continue
    else:
        omittedTags[v] = vtags[v]

for c in ctags:
    if ctags[c] > 10:
        filteredTags[c] = ctags[c]
        continue
    else:
        omittedTags[c] = ctags[c]

print(filteredTags)
#writeToCSV('tags.csv',"Concept", "Occurance", vtags.update(ctags))
writeToCSV('filtered_tags.csv', "Concept", "Ocurrence", filteredTags)
writeOmitted('omitted.csv')
