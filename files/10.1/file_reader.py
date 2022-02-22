# file_name = 'text_files/pi_digeits.txt'
# with open(file_name) as file_ob:
#     # content = file_ob.read()
#     lines = file_ob.readlines()
#     print(lines, "is lines")
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#     print(pi_string, "is read")

file_name = 'text_files/review.txt'
with open(file_name) as review:
    # print(review, "is vvv")
    for line in review:
        line = line.rstrip().replace('Python', "C")
        print(line, "is review")

