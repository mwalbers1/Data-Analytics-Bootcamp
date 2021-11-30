
head(mpg)

plt <- ggplot(mpg, aes(x=class)) # import dataset into ggplot2
plt + geom_bar()  # plot a bar plot

# create summary table
mpg_summary <- mpg %>% group_by(manufacturer) %>% summarize(Vehicle_Count=n(), .groups = 'keep') 

# import dataset
plt <- ggplot(mpg_summary, aes(x=manufacturer, y=Vehicle_Count))

# plot a bar plot
plt + geom_col()

#plot bar plot with labels
plt + geom_col() + xlab("Manufacturing Company") + ylab("Number of Vehicles") +
theme(axis.text.x = element_text(angle=45,hjust=1))

#create summary table
mpg_summary <- subset(mpg, manufacturer=="toyota") %>%
  group_by(cyl) %>%
  summarize(Mean_Hwy=mean(hwy), .groups = 'keep')

#import dataset into ggplot
plt <- ggplot(mpg_summary, aes(x=cyl, y=Mean_Hwy))
plt + geom_line() + scale_x_discrete(limits=c(4,6,8)) + scale_y_continuous(breaks = c(15:30))

#scatter plot
#import dataset into ggplot2
plt <- ggplot(mpg, aes(x=displ,y=cty))

# add scatter plot with labels
plt + geom_point() + xlab("Engine Size (L)") + ylab("City Fuel-Efficiency (MPG)")

# visualize relationship between fuel efficiency and engine size, group by additional variables
plt <- ggplot(mpg, aes(x=displ,y=cty,color=class))
plt + geom_point() + labs(x="Engine Size (L)", y="City Fuel-Efficiency (MPG)", color="Vehicle Class")


plt <- ggplot(mpg, aes(x=displ,y=cty,size=class, color=class))
plt + geom_point() + labs(x="Engine Size (L)", y="City Fuel-Efficiency (MPG)", color="Vehicle Class")

# boxplot
plt <- ggplot(mpg,aes(y=hwy))
plt + geom_boxplot()

# create a set of boxplots that compares highway fuel efficiency for each car manufacturer
plt <- ggplot(mpg, aes(x=manufacturer,y=hwy))
plt + geom_boxplot() + theme(axis.text.x=element_text(angle=45,hjust=1))

# create heatmap to visualize the average highway fuel efficiency across vehicle class from 1999 to 2008
mpg_summary <- mpg %>% 
  group_by(class,year) %>%
  summarize(Mean_Hwy=mean(hwy), .groups = 'keep')
plt <- ggplot(mpg_summary, aes(x=class, y=factor(year), fill=Mean_Hwy))
plt + geom_tile() + labs(x="Vehicle Class", y="Vehicle Year", fill="Mean Highway (MPG)")

View(mpg)

# heatmap for difference in avg highway fuel efficiency across vehicle model from 1999 to 2008
mpg_summary <- mpg %>%
  group_by(model,year) %>%
  summarize(Mean_Hwy=mean(hwy), .groups = 'keep')
plt <- ggplot(mpg_summary, aes(x=model, y=factor(year), fill=Mean_Hwy))
plt + geom_tile() + labs(x="Vehicle Model", y="Vehicle Year", fill="Mean Highway (MPG)") +
  theme(axis.text.x = element_text(angle=90,hjust=1,vjust=.5))

# layering of additional plot
plt <- ggplot(mpg, aes(x=manufacturer, y=hwy)) # import dataset into ggplot
plt + geom_boxplot() +
  theme(axis.text.x=element_text(angle = 45, hjust=1)) +
  geom_point()

mpg_summary <- mpg %>% group_by(class) %>% summarize(Mean_Engine=mean(displ), .groups = 'keep') # create summary table
plt <- ggplot(mpg_summary, aes(x=class,y=Mean_Engine))
plt + geom_point(size=4) + labs(x="Vehicle Class", y="Mean Engine Size")

mpg_summary <- mpg %>% group_by(class) %>% summarize(Mean_Engine=mean(displ),SD_Engine=sd(displ), .groups = 'keep')
plt <- ggplot(mpg_summary, aes(x=class, y=Mean_Engine))
plt + geom_point(size=4) + labs(x="Vehicle Class", y="Mean Engine Size") +
  geom_errorbar(aes(ymin=Mean_Engine-SD_Engine, ymax=Mean_Engine+SD_Engine))

mpg_long <- mpg %>% gather(key="MPG_Type", value = "Rating", c(cty,hwy))
head(mpg_long)

plt <- ggplot(mpg_long, aes(x=manufacturer,y=Rating,color=MPG_Type))
plt + geom_boxplot() + theme(axis.text.x = element_text(angle=45, hjust=1))

plt <- ggplot(mpg_long, aes(x=manufacturer, y=Rating, color=MPG_Type))
plt + geom_boxplot() + facet_wrap(vars(MPG_Type)) +
  theme(axis.text.x = element_text(angle=45, hjust=1), legend.position = "none") +
  xlab("Manufacturer")

