import wordcloud

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

newStr = ''

wordict = {}

for i in text:
    if i.isalpha():
        newStr += i.lower()
    else:
        newStr += " "

badList = ["a", "to", "the", "and", "or", "my", "i", "am", "is", ""]

for i in newStr.split(" "):
    if i not in badList:
        if i in wordict:
            wordict[i] += 1
        else:
            wordict[i] = 1

cloud = wordcloud.WordCloud(width=480, height=480, background_color="white")
cloud.generate_from_frequencies(wordict)
cloud.to_file("myfile.jpg")

