import json
import codecs

f = codecs.open('stage1/stage1_2_output', 'r', errors='ignore')
attribute_list = eval(f.read())
# print attribute_list

top_ten = []
for i in range(0, 10):
    top_ten.append(attribute_list[i][0])
print top_ten

# print some values
for attribute in top_ten:

    f = codecs.open('stage1/elec_pairs_stage1.txt', 'r', errors='ignore')

    count = 0

    for line in f:
        line = unicode(line, errors='ignore')
        line_split = line.split('?')

        json1 = json.loads(line_split[2])   # json for product 1

        if attribute in json1:
            text = json1[attribute]
            print attribute + ": " + text[0]
            count += 1

        if count == 30:
            break

# length
for attribute in top_ten:

    f = codecs.open('stage1/elec_pairs_stage1.txt', 'r', errors='ignore')

    total = 0.0
    count = 0.0
    maximum = 0
    minimum = 10000

    id_list = []

    for line in f:
        line = unicode(line, errors='ignore')
        line_split = line.split('?')

        json1 = json.loads(line_split[2])   # json for product 1
        json2 = json.loads(line_split[4])   # json for product 2

        if line_split[1] not in id_list:
            id_list.append(line_split[1])
            if attribute in json1:
                text = json1[attribute][0]

                count += 1
                total += len(text)
                maximum = max(maximum, len(text))
                minimum = min(minimum, len(text))

        if line_split[3] not in id_list:
            id_list.append(line_split[3])
            if attribute in json2:
                text = json2[attribute][0]

                count += 1
                total += len(text)
                maximum = max(maximum, len(text))
                minimum = min(minimum, len(text))

    print attribute + ", " + str(total / count) + ', ' + str(maximum) + ', ' +str(minimum)
    print count
