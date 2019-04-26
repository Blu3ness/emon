import datetime
import time
import os
from threading import Thread

import subprocess
import glob
import math

WORKLOAD = ['emon –s 30 -l0 –t0.1 -C "UNC_CBO_CACHE_LOOKUP.WRITE_MESI, UNC_CBO_CACHE_LOOKUP.READ_MESI,UNC_IMC_DRAM_IA_REQUESTS,UNC_IMC_DRAM_GT_REQUESTS,UNC_IMC_DRAM_IO_REQUESTS,UNC_IMC_DRAM_DATA_READS,UNC_IMC_DRAM_DATA_WRITES" -u -X -f Read_Write_MESI.csv', 'emon -s 30 -l0 –t0.1 -C "UNC_CBO_CACHE_LOOKUP.ANY_MESI, UNC_CBO_CACHE_LOOKUP.ANY_ES,UNC_IMC_DRAM_IA_REQUESTS,UNC_IMC_DRAM_GT_REQUESTS,UNC_IMC_DRAM_IO_REQUESTS,UNC_IMC_DRAM_DATA_READS,UNC_IMC_DRAM_DATA_WRITES" -u -X -f Any_Mesi_Any_ES.csv', 'emon -s 30 -l0 –t0.1 -C "UNC_CBO_IPQ_REJECTS.ANY, UNC_CBO_CACHE_LOOKUP.ANY_MESI,UNC_IMC_DRAM_IA_REQUESTS,UNC_IMC_DRAM_GT_REQUESTS,UNC_IMC_DRAM_IO_REQUESTS,UNC_IMC_DRAM_DATA_READS,UNC_IMC_DRAM_DATA_WRITES" -u -X -f Any_Mesi_Any_IPQ_Rejects.csv', 'emon -s 30  -l0 –t0.1 -C "UNC_CBO_ISMQ_REJECTS.ANY, UNC_CBO_CACHE_LOOKUP.ANY_MESI,UNC_IMC_DRAM_IA_REQUESTS,UNC_IMC_DRAM_GT_REQUESTS,UNC_IMC_DRAM_IO_REQUESTS,UNC_IMC_DRAM_DATA_READS,UNC_IMC_DRAM_DATA_WRITES" -u -X -f Any_Mesi_Any_ISMQ_Rejects.csv', 'emon -s 30 -l0 –t0.1 -C "UNC_CBO_IRQ_REJECTS.ANY, UNC_CBO_CACHE_LOOKUP.ANY_MESI,UNC_IMC_DRAM_IA_REQUESTS,UNC_IMC_DRAM_GT_REQUESTS,UNC_IMC_DRAM_IO_REQUESTS,UNC_IMC_DRAM_DATA_READS,UNC_IMC_DRAM_DATA_WRITES" -u -X -f Any_Mesi_Any_ISMQ_Rejects.csv']
CURRENT_DATE = datetime.datetime.now().strftime("%Y_%m_%d")
def preLoadEmon():
    subprocess.call(r'c:/Intel/sep/sep_var.cmd')

def emon():
    



threads = []

for i in range(0, 8):
    threads.append(Thread(target=emon))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

