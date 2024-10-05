def markdown_to_blocks(text):
    temp_list = text.split("\n\n")
    output_list = []
    for line in temp_list:
        if line == "":
            continue
        stripped_line = line.strip()
        output_list.append(stripped_line)
    return output_list
    