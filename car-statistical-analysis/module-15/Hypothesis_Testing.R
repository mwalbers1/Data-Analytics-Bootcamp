
population_table <- read.csv('used_car_data.csv', check.names = F, stringsAsFactors = F)
plt <- ggplot(population_table, aes(x=log10(Miles_Driven)))
plt + geom_density()

library(dplyr)
sample_table <- population_table %>% sample_n(50)

# use log10 transformation to make the mileage data more normal
plt <- ggplot(sample_table, aes(x=log10(Miles_Driven)))
plt + geom_density()

# compare sample versus population means
t.test(log10(sample_table$Miles_Driven), mu=mean(log10(population_table$Miles_Driven)))

sample_table <- population_table %>% sample_n(50)
sample_table2 <- population_table %>% sample_n(50)

t.test(log10(sample_table$Miles_Driven), log10(sample_table2$Miles_Driven))

mpg_data <- read.csv('mpg_modified.csv')
mpg_1999 <- mpg_data %>% filter(year==1999)
mpg_2008 <- mpg_data %>% filter(year==2008)

#compare the mean difference between two samples
t.test(mpg_1999$hwy,mpg_2008$hwy,paired = T)

# The p-value is above the assumed significance level. Therefore, we would state that there is not 
# enough evidence to reject the null hypothesis and there is no overall difference in fuel efficiency
# between vehicles manufactured in 1999 versus 2008.

mtcars_filt <- mtcars[,c("hp","cyl")]
mtcars_filt$cyl <- factor(mtcars_filt$cyl)
aov(hp ~ cyl, data = mtcars_filt) # compare means across multiple levels
summary(aov(hp ~ cyl, data = mtcars_filt))
