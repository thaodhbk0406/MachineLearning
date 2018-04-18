
with open('imagenet_comp_graph_label_strings.txt') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

Train_dataset=['Cat', 'Dog', 'Bear', 'Table', 'Chair', 'Electric fan', 'Computer Mouse', 'Computer keyboard', 'Screen', 'Cup', 'Water bottle', 'Telephone', 'Guitar', 'Chicken', 'Fish', 'Snake', 'Frog', 'Fence', 'Banana', 'Truck']
for i in range(0,1001):
	if(content[i] in Train_dataset):
		print(content[i])
		

# print(content) 
# result = open('result.txt', 'w')
# for line in content:
# 	result.write(line+'\n')

# result.close()
