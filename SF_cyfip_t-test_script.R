# !!! change to full path to your file. In case you use "\" in Mac, you may need to use "\\" instead of single "\" 
data <- read.csv('/home/stanislav/Documents/SF_CYFIP_P60.csv', dec = '.', sep = ',')
#check if data is opened correctly (as a table, with column names recognized correctly in the first row)
View(data)
#if data looks weird (maybe all the columns will appear merged into one), change "sep = ','" to "sep = '\t'" above

data$ROI <- as.factor(data$ROI) #just means that number of ROI should be treated as a factor, not a quantitative measure 

## Here I generate smaller table with values averaged per animal for every brain region separately 

data_averaged <- aggregate(.~Animal+Genotype+Brain_Region, data, mean) # average per all rows with the same Animal-Genotype-Brain_region combination
data_averaged <- subset(data_averaged, select = -c(ROI)) # removed info about ROI number as it is not needed
View(data_averaged)
# !!! change to full path to where you want to save the table with averaged values, if needed
write.csv(data_averaged,"/home/stanislav/Documents/SF_CYFIP_P60_averaged.csv")

## Statistical analysis. T-test (or Mann-Whitney U-Test) instead of ANOVA because you only compare two conditions.

results <- data.frame(Brain_region=rep("", 200), Parameter=rep("", 200), Test=rep("", 200), Value=rep(NA, 200),
                 stringsAsFactors=FALSE)       # generate an empty dataframe with excessive number of rows (R is not great)   
current_row = 1
for (i in levels(data_averaged$Brain_Region)) { #go over brain regions separately, one by one
  selected <- c(i)
  data_working <- data_averaged[data_averaged$Brain_Region %in% selected,] #Select data from single brain region
  for (j in colnames(data_averaged[4:12])) { # all your columns with MotiQ parameters, from 4 to 12 ecause I removed ROI column before
    norm_test <- by(data_working[[j]], INDICES = data_working$Genotype, FUN = shapiro.test) # test normality of distribution
    disp_test <- fligner.test(formula = data_working[[j]]~Genotype, data = data_working) # test homogeneity of dispersion
    if ((norm_test$Ctrl$p.value > 0.05) & (norm_test$KO$p.value > 0.05) & (disp_test$p.value > 0.05) ) { # If all tests are "passed", you can use T-test 
      t_test <- t.test(data_working[[j]] ~ Genotype, data = data_working, var.equal = TRUE) # T-test , check if Genotypes are different within the brain region by selected parameter
      results[current_row,] <- c(i,j,"T test",t_test$p.value) # adding to the Results dataframe info about current brain region, current parameter, type of test used, and whether there is significant difference
    } else { #If distribution in at least one group is not equal, of dispersion is not homogeneous 
      u_test <- wilcox.test(data_working[[j]] ~ Genotype, data = data_working) # Mann-Whitney U-test instead of T-Test
      results[current_row,] <- c(i,j,"Mann-Whitney",u_test$p.value) # adding to the Results dataframe info about current brain region, current parameter, type of test used, and whether there is significant difference
    }
    current_row = current_row + 1 
  }
}
View(results) # check if everything looks fine
results <- results[!apply(is.na(results) | results == "", 1, all),] # remove excessive empty rows
# !!! change to full path to where you want to save the table with results of statistical analysis
write.csv(results,"/home/stanislav/Documents/SF_CYFIP_P60_pvalues.csv")
