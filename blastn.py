# ~/anaconda3/bin/python3.7
import os
import multiprocessing as mul

query_path = '/home/luotao/fungi/workspace/tmp/fa/'


subjet_path = '/home/luotao/zasha_and_rfam/zsrf_db/RFAM_14.6'

cpu = 5

#/home/luotao/fungi/fna_data/fna/lssfungi  #lssfungi
#/home/luotao/fungi/fna_data/all   #fungi
#/home/luotao/genome_oil/bldb/all
#/home/luotao/zasha_and_rfam/zsrf_db/zs_and_rf
query_list = os.listdir(query_path)



out_path = '/home/luotao/fungi/workspace/tmp/out/'
out_list = os.listdir(out_path)



def blast(name):
    if '.fa' == name[-3:] and name.replace('fa','out') not in out_list:
        os.system(''.join(['blastn ',
                           "-strand 'plus' "
                          f'-query {query_path+name} ',
                          f'-db {subjet_path} ', 
                           '-line_length 2000000 ',
                          f'-out {out_path+name[:-3]}.out ',
                           '-num_descriptions 50 '
                           '-evalue 1 ']))
                           
#-strand 'plus'      

if __name__ == '__main__':
    pool = mul.Pool(cpu)
    pool.map(blast,query_list)
    pool.close()
    pool.join()
    #JAALLR010004744.1+4_171_225.fa

                         
                         
                         



#makeblastdb -in /home/luotao/fungi/fna_data/all.fna -dbtype nucl -input_type fasta -out /home/luotao/fungi/fna_data/all
#blastn -task blastn -query /home/luotao/oil_meta/genome/all2/LZQO01000001.1_3425_3465.fa -db /home/luotao/oil_meta/genome/bldb/all_fasta -out /home/luotao/oil_meta/genome/out1.1.out -window_masker_taxid queryLZQO01000001.1_3425_3465 