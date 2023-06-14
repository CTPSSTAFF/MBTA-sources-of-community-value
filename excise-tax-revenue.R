library(tidyverse)
library(openxlsx)

core <- read_csv("data/Core_Service_Area.csv")
extd <- read_csv("data/MBTA_Extended_Service_Area.csv")

core_service_area <- core$TOWN
extd_service_area <- extd$TOWN

revenue <- read.xlsx("data/MV_Act.xlsx")
revenue$Municipality <- str_to_upper(revenue$Municipality)

total_rev_core <- revenue %>% 
  filter(Municipality %in% core_service_area) %>%   ## only munis in core service area
  summarize(rev_2022 = sum(`2022`)) %>%             ## add up 2022 revenue
  as.double()

total_rev_extd <- revenue %>% 
  filter(Municipality %in% extd_service_area) %>%   ## only munis in extd service area
  summarize(rev_2022 = sum(`2022`)) %>%             ## add up 2022 revenue
  as.double()