# with open("input.txt", "r") as file:
#     print(file)
#     for i in file:
#         print(i)

# with open("input.txt", "r") as file:
#     print(file.read())


# with open("input.txt", "r") as file:
#     print(file.readline())


# with open("input.txt", "r") as file:
#     print(file.readlines())


# with open("input.txt", "r") as file:
#     lines = file.readlines()
#     lines = list(map(lambda x: x.replace("\n", ""), lines))
#     print(lines)
#     for line in lines:
#         print(line)


# with open("input.txt", "r") as file:
#     lines = file.readlines()
#     lines = list(map(lambda x: x.replace("\n", ""), lines))
#     lines.reverse()
#     with open("output.txt", "w") as op_file:
#         for l in lines:
#             op_file.write(l + "\n")


# with open("input.txt", "w") as input_file:
#     input_file.writelines(list(map(lambda x: str(x) + "\n", list(range(3, 10)))))

# with open("input.txt","r") as input_file:
#     lines = input_file.readlines()
#     with open("output.txt","w") as output_file:
#         output_file.write(f"Total: {str(sum([int(i.replace("\n", "")) for i in lines]))}")

# with open("output.txt","r") as output_file:
#     print(output_file.read())  
    

