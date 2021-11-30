
g <- T

disney_characters <- c("mickey", "donald")
presidents <- c("obama", "clinton")
combined <- c(disney_characters, presidents)

for (x in combined) {
  print(x)
}

numeric_vector <- 1:length(combined)
square_vector <- numeric_vector**2

random_list <- list("movies"=c("Star Wars", "Titanic"),
                    "states"=c("California", "New York"))

random_list["states"]
random_list$movies
random_list$states

typeof(numeric_vector)

# months of year
months <- c("Jan", "Feb")

# Avg rainfall/precipitation in NYC
precip <- c(3.6, 4.5)

# Assign months to precip as names
names(precip) <- months

print(precip)
print(names(precip))
feb_precip <- precip["Feb"]
print(feb_precip)

# summary statistics
precip_summary <- summary(precip)

precip_summary["Mean"]

# piping

library('dplyr')

precip %>% summary

precip %>% length()
length(precip)

yearly_precip <- precip %>% sum()
print(yearly_precip)

precip_values = c(3.6, 4.5)
precip_values %>% sum()

precip %>% sum()
