#Run this if you are using this session for the first time - uncomment 
#source("https://bioconductor.org/biocLite.R")
#biocLite("DESeq")
library(DESeq)
#Alter working directory according to your data location 
setwd("/home/ngst/Desktop/diff_out/")
seqdata <- read.delim("/home//ngst/Desktop/diff_out/cuffdiff_genes.counts.matrix")
#Remove the first column so that the object only conatins numeric values 
countdata <- seqdata[,-(1:1)]
head(countdata)
#Deseq wants input object as a matrix
m <- as.matrix(countdata)
#Truncate float values 
storage.mode(m) = "integer"
#group together q1 and q2 
conds <- factor(c("1","2","1","2","2","1","1","2"))
cds <- newCountDataSet(m, conds)
#DESeq only needs relative library sizes
#estimate the size factors
cds <- estimateSizeFactors( cds )
sizeFactors( cds )
head(counts(cds,normalized=TRUE))
#This function obtains dispersion estimates for a count data set
cds <- estimateDispersions( cds ) 
plotDispEsts(cds)
dev.print(file = "dispersionEstimates1111.pdf")
cdsBlind = estimateDispersions(cds,method = c( "pooled", "pooled-CR", "per-condition", "blind" ))
vsd = varianceStabilizingTransformation(cdsBlind)
#test for differences between the two means 
#diff_means <- nbinomTest(cds , 1, 2 , pvals_only = TRUE)
select = order(rowMeans(counts(cds)), decreasing=TRUE)[1:30]
heatmap.2(exprs(vsd)[select,] )
#plotPCA(vsd)
#dev.print(file = "heatmap11.pdf!")
