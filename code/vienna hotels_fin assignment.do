list in 1/10
describe
summarize

/// Task 5
/// check missing values
misstable summarize

/// Replace missing numeric values with column mean
ds, has(type numeric)
foreach var of varlist `r(varlist)' {
    quietly summarize `var'
    replace `var' = r(mean) if missing(`var')
}

///Replace missing string values with "Unknown"
ds, has(type string)
foreach var of varlist `r(varlist)' {
    replace `var' = "Unknown" if missing(`var')
}

///Task 6

/// a) Filter observations
keep if city == "Vienna" & price > 50 & rating > 4

/// b) Keep only useful variables
keep city neighbourhood price stars rating distance accommodation_type

/// c) Create new variables
gen price_per_star = price / stars
gen log_price = log(price)
gen near_center = distance < 2

list in 1/10

/// Task 3

/// List 
local preferred_neighbourhoods "Innere Stadt" "Alsergrund" "Leopoldstadt"
keep if inlist(neighbourhood, "Innere Stadt", "Alsergrund", "Leopoldstadt")

/// Dictionary
collapse (mean) avg_price = price, by(accommodation_type)
list

/// Task 8
describe
summarize avg_price

///Task 9
graph bar avg_price, over(accommodation_type)






