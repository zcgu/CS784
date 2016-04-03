import codecs


def read_file(file_name):
    f = codecs.open(file_name, 'r', errors='ignore')

    lines = []

    for line in f:
        line = unicode(line, errors='ignore')
        lines.append(line)

    return lines


