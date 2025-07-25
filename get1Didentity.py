import os
import numpy as np

import argparse

def main():
    parser = argparse.ArgumentParser(description="Annotation sequence identity for centromeres")
    parser.add_argument(
        "-i", "--input_bed_dir", help="A directory contains all moddotplot files", required=True
    )
    
    parser.add_argument(
        "-o", "--output_file", help="outfile bed file name", required=True
    )
    
    args = parser.parse_args()

    workdir = args.input_bed_path
    outfile = args.output_file

    
    files = os.listdir(workdir)
    
    outfile = open(outfile,'w')
    count = 1
    for file in files:
        print(file)
        file = file.replace('.bed', '')
        window = 5
        block_length = 5000
        remove_track = 3
        step = 1
        bed_file = workdir + '/' + file + '.bed'
        region = file.split(':')[-1].split('-')
        array_start = int(region[0])
        identity_vector = {}
        with open(bed_file,'r') as f:
            while True:
                line = f.readline()[:-1]
                if not line:
                    break
                if line.startswith('#'):
                    continue
                items = line.split('\t')
                if int(items[1]) not in identity_vector.keys():
                    identity_vector[int(items[1])] = [[int(items[4]),float(items[-1])]]
                else:
                    identity_vector[int(items[1])].append([int(items[4]),float(items[-1])])
    
        bins = []
        array_length = int(region[1]) - int(region[0])
        bin_number = array_length / block_length
        if bin_number > int(bin_number):
            bin_number = int(bin_number) + 1
        else:
            bin_number = int(bin_number)
        for i in range(bin_number):
            bins.append(i * block_length + 1)
    
        identity_matrix = {}
        for i in bins:
            identity_matrix[i] = {}
            for j in bins:
                identity_matrix[i][j] = 0
        
        for i in identity_vector.keys():
            for j in identity_vector[i]:
                identity_matrix[i][j[0]] = j[1]
                identity_matrix[j[0]][i] = j[1]
        
        bin_list = list(identity_matrix.keys())

        final_identity = []
        for i in range(0,len(bin_list),step):
            identity_list = []
            if (i + window) > len(bin_list):
                window = (len(bin_list) - i)
            remove_set = set()
            
            for j in range(window):
                for k in range(remove_track):
                    if j + k - int(((remove_track - 1) / 2)) < 0:
                        continue
                    if j + k - int(((remove_track - 1) / 2)) >= window:
                        continue
                    remove_set.add((j,j + k - int(((remove_track - 1) / 2))  ))
                
            for j in range(window):
                for k in range(window):
                    if (j,k) in remove_set:
                        continue
                    value = identity_matrix[bin_list[i + j]][bin_list[i + k]]
                    # if value != 0:
                    #     identity_list.append(value)
                    identity_list.append(value)
        
            if len(identity_list) == 0:
                continue
            mean_identity = np.mean(identity_list)
        
            final_identity.append([bin_list[i], bin_list[i] + step * block_length -1, mean_identity])
    
        for i in final_identity:
            outfile.write(file + '\t' + str(array_start + i[0]) + '\t' + str(array_start + i[1]) + '\t' + str(i[2]) + '\n')
        outfile.flush()
        count += 1
    outfile.close()





if __name__ == '__main__':
    main()
