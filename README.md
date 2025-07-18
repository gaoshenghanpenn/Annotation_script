# Annotation_script
For annotation of human centromere genome sequence.
## Dependencies
Packages  | Version |
--------- | --------|
Python  | 3.12 |
numpy  | 1.22.3 |

## Usage
```Bash
python get1Didentity.py -i ./moddotplot_dir -o 1DModdotplot.bed
python stv_multiarray.py -i monomer_sequence.bed -o stv.bed
      -t is Sequence identity threshold, default 85.0
```
## Input format
### get1Didentity.py
```Bash
./Moddotplot
├── chm13_chr10:38568472-42561808.bed
├── chm13_chr1:121119216-127324115.bed
├── chm13_chr11:50037316-55697715.bed
├── chm13_chr12:33784923-37869922.bed
├── chm13_chr13:13315524-18076723.bed
├── chm13_chr14:9567419-13283570.bed
....
```
### stv_multiarray.py
#### monomer_sequence.bed
```Bash
NA20355_chrX_haplotype1-0000034:56735321-61774518       1105900 1106070 S3CXH1L.11      99.42   -       1105900 1106070 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1106071 1106241 S3CXH1L.10      99.42   -       1106071 1106241 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1106242 1106412 S3CXH1L.9       98.83   -       1106242 1106412 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1106413 1106579 S3CXH1L.8       96.41   -       1106413 1106579 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1106580 1106750 S3CXH1L.7       98.25   -       1106580 1106750 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1106751 1106921 S3CXH1L.6       96.49   -       1106751 1106921 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1106922 1107090 S3CXH1L.5       95.86   -       1106922 1107090 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1107091 1107276 S3CXH1L.4       90.32   -       1107091 1107276 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1107277 1107447 S3CXH1L.3       95.32   -       1107277 1107447 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1107448 1107618 S3CXH1L.2       97.08   -       1107448 1107618 0,0,0
NA20355_chrX_haplotype1-0000034:56735321-61774518       1107619 1107785 S3CXH1L.1       96.41   -       1107619 1107785 0,0,0
```
End-to-end operation is recommended here: https://github.com/logsdon-lab/Snakemake-HumAS-SD

## Contact
If you have any questions, please feel free to contact: Shenghan.Gao@PennMedicine.upenn.edu

