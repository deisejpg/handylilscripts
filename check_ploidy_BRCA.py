import gzip
from pathlib import Path

''' 
        This script checks whether the Illumina Basespace analysis performed 
    for the BRCA Ampliseq Panel was somatic or germline. The information
    is printed on the screen and can be used to rename the files accordingly.
    This script was used for the data order 393224 in June 2024.
'''

def check_variant_type(path):
    try:
        with gzip.open(path, "rt", encoding='utf-8') if path.endswith('.gz') else open(path, 'r', encoding='utf-8') as f:
            for line in f:
                if 'somatic' in line:
                    print(f"somatic in {path}")
                if 'diploid' in line:
                    print(f"germline in {path}")
    except UnicodeDecodeError as e:
        print(f"Error reading file {path}: {e}")
        return "Error"
    
def check_all_vcf_files(directory):
    pathlist = Path(directory).rglob('*.vcf.gz')
    for path in pathlist:
        check_variant_type(str(path))

current_directory = '.'
check_all_vcf_files(current_directory)
#screen output
#germline in 1192924B-4004_ds.bcc3b4bc4a5c463095dd56c54abc7b58\1192924B-4004_S2.genome.vcf.gz: ##FILTER=<ID=MultiAllelicSite,Description="Variant does not conform to diploid model">
#germline in 1192924B-4004_ds.bcc3b4bc4a5c463095dd56c54abc7b58\1192924B-4004_S2.vcf.gz: ##Pisces_cmdline=""-BamPaths /data/scratch/RunFolder/Analysis/Temp_03-VariantCalling/geminiBams/1192924B-4004_S2.bam -GenomePaths /data/scratch/RunFolder/Analysis/Genome/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta -gVCF True -OutFolder /data/scratch/RunFolder/Analysis/Temp_03.03-VariantCalling.VariantCalling/1192924B-4004 -i /data/scratch/RunFolder/Analysis/Temp_03.03-VariantCalling.VariantCalling/interval/1192924B-4004_S2.padded.intervals.picard -CallMNVs True -MaxMNVLength 3 -MaxGapBetweenMNV 1 -MinBaseCallQuality 20 -MaxVariantQScore 100 -MinVariantQScore 20 -CrushVcf True -MinDP 10 -ReportNoCalls True -Ploidy diploid -EnableSingleStrandFilter False -MinDPFilter 10 -MaxAcceptableStrandBiasFilter 0.5 -VariantQualityFilter 20 -MinVariantFrequencyFilter 0.2 -RMxNFilter 5,9,0.35 -MaxNumThreads 9 -ThreadByChr True -UseStitchedXD True""
#germline in 1192924B-4004_ds.bcc3b4bc4a5c463095dd56c54abc7b58\1192924B-4004_S2.vcf.gz: ##FILTER=<ID=MultiAllelicSite,Description="Variant does not conform to diploid model">
#somatic in 1192924B-4004_ds.dfd7aed20c2f465c9003927fb909c029\1192924B-4004_S2.genome.vcf.gz: ##Pisces_cmdline=""-BamPaths /data/scratch/RunFolder/Analysis/Temp_03-VariantCalling/geminiBams/1192924B-4004_S2.bam -GenomePaths /data/scratch/RunFolder/Analysis/Genome/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta -gVCF True -OutFolder /data/scratch/RunFolder/Analysis/Temp_03.03-VariantCalling.VariantCalling/1192924B-4004 -i /data/scratch/RunFolder/Analysis/Temp_03.03-VariantCalling.VariantCalling/interval/1192924B-4004_S2.padded.intervals.picard -CallMNVs True -MaxMNVLength 3 -MaxGapBetweenMNV 1 -MinimumFrequency 0.01 -MinBaseCallQuality 20 -MaxVariantQScore 100 -MinVariantQScore 20 -CrushVcf False -MinDP 10 -ReportNoCalls True -Ploidy somatic -EnableSingleStrandFilter False -MinDPFilter 10 -MaxAcceptableStrandBiasFilter 0.5 -VariantQualityFilter 30 -MinVariantFrequencyFilter 0.05 -RMxNFilter 3,6,0.20 -MaxNumThreads 9 -ThreadByChr True -UseStitchedXD True""

# Info used to decide whether the file was somatic or germline
# "-Ploidy" is either somatic or diploid
# ##fileformat=VCFv4.1
##fileDate=20220127
##source=Pisces 5.2.9.23
##Pisces_cmdline=""-BamPaths /data/scratch/RunFolder/Analysis/Temp_03-VariantCalling/geminiBams/1172808B-4004_S3.bam -GenomePaths /data/scratch/RunFolder/Analysis/Genome/Homo_sapiens/UCSC/hg19/Sequence/WholeGenomeFasta -gVCF True -OutFolder /data/scratch/RunFolder/Analysis/Temp_03.03-VariantCalling.VariantCalling/1172808B-4004 -i /data/scratch/RunFolder/Analysis/Temp_03.03-VariantCalling.VariantCalling/interval/1172808B-4004_S3.padded.intervals.picard -CallMNVs True -MaxMNVLength 3 -MaxGapBetweenMNV 1 -MinimumFrequency 0.01 -MinBaseCallQuality 20 -MaxVariantQScore 100 -MinVariantQScore 20 -CrushVcf False -MinDP 10 -ReportNoCalls True 
#-Ploidy somatic -EnableSingleStrandFilter False -MinDPFilter 10 -MaxAcceptableStrandBiasFilter 0.5 -VariantQualityFilter 30 -MinVariantFrequencyFilter 0.05 -RMxNFilter 3,6,0.20 -MaxNumThreads 9 -ThreadByChr True -UseStitchedXD True""
##VariantQualityRecalibration=VQR 5.2.9.23
