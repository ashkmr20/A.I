import numpy as np

def read_data(input_file_dir):
	'''
	INPUT : input_file_dir: The input file to be read
	OUTPUT : The data arranged in a 3d numpy array - (image, rows, cols)
	'''
		
	data_list = []
	label_list = []
	examples_count = 0
	with open(input_file_dir, 'r+') as file:
		for line in file:
			line = line.rstrip('\n')
			line = line.lstrip()
			digits = [int(d) for d in str(line)]
			if(len(digits) == 1):
				label_list += [digits]
				examples_count += 1
				continue
			data_list += [digits]

	data_array = np.array(data_list)
	labels = np.array(label_list)
	data = np.zeros((examples_count, 32,32))
	for i in np.arange(examples_count):
		data[i,:,:] = data_array[i*32:(i+1)*32 ,:]
	found_labels = []

	unique_labels = np.unique(labels)

	return data,labels














