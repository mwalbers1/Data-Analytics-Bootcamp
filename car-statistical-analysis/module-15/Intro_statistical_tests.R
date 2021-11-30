# Introduction to Statistical Tests

# visualize distribution using density plot
ggplot(mtcars,aes(x=wt)) + geom_density()

# quantitative test for normality
shapiro.test(mtcars$wt)

