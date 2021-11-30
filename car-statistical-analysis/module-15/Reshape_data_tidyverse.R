demo_table <- read.csv(file = 'demo.csv', check.names = F, stringsAsFactors = F)

# add columns to original data frame
demo_table <- demo_table %>% mutate(Mileage_per_Year=Total_Miles/(2020-Year),IsActive=TRUE) 


# jsonlite library for reading json files
library(jsonlite)
demo_table2 <- fromJSON(txt='demo.json')

#create summary table
summarize_demo <- demo_table2 %>% group_by(condition) %>% summarize(Mean_Mileage=mean(odometer), .groups = 'keep') 

#create summary table with multiple columns
summarize_demo <- demo_table2 %>% group_by(condition) %>% summarize(Mean_Mileage=mean(odometer),Maximum_Price=max(price),Num_Vehicles=n(), .groups = 'keep')

# reshaping data
demo_table3 <- read.csv('demo2.csv',check.names = F,stringsAsFactors = F)

long_table <- demo_table3 %>%
  gather(key = "Metric",value = "Score", buying_price:maintainence_cost)

View(long_table)

wide_table <- long_table %>% spread(key = "Metric", value = "Score")
View(wide_table)

View(demo_table3)

table <- demo_table3[,(colnames(wide_table))]
all.equal(table, wide_table)
