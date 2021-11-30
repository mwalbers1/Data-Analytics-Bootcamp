# Correlation

# create scatter plot
plt <- ggplot(mtcars, aes(x=hp,y=qsec))
plt + geom_point()

cor(mtcars$hp, mtcars$qsec)

used_cars <- read.csv('used_car_data.csv', stringsAsFactors = F)
head(used_cars)

plt <- ggplot(used_cars, aes(x=Miles_Driven, y=Selling_Price))
plt + geom_point()

cor(used_cars$Miles_Driven, used_cars$Selling_Price)

# convert data frame into numeric matrix
used_matrix <- as.matrix(used_cars[,c("Selling_Price", "Present_Price", "Miles_Driven")])
cor(used_matrix)

# create linear model
lm(qsec ~ hp, mtcars)

# the linear regression model for our dataset would be qsec = -0.02hp + 20.56
summary(lm(qsec ~ hp, mtcars))

# create linear model
model <- lm(qsec ~ hp, mtcars)

# determine y-axis values from linear model
yvals <- model$coefficients['hp'] * mtcars$hp + model$coefficients['(Intercept)']

# plot scatter plot
plt <- ggplot(mtcars, aes(x=hp, y=qsec))
plt + geom_point() + geom_line(aes(y=yvals), color="red")

# multiple regression
lm(qsec ~ mpg + disp + drat + wt + hp, data=mtcars)
summary(lm(qsec ~ mpg + disp + drat + wt + hp, data=mtcars))

library(tidyverse)

head(mpg)

table(mpg$class, mpg$year)

# generate contingency table
tbl <- table(mpg$class, mpg$year)

# perform chi-squared test
chisq.test(tbl)
