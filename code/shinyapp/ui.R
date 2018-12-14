library(shiny)
library(ggplot2)

dataset <- read.csv('HRDataset_v9.csv') 

fluidPage(
  
  titlePanel("Human Resources Data Explorer"),
  
  sidebarPanel(
    
    sliderInput('sampleSize', 'Sample Size', min=1, max=nrow(dataset),
                value=min(100, nrow(dataset)), step=30, round=0),
    
    selectInput('x', 'X', names(dataset)),
    selectInput('y', 'Y', names(dataset), names(dataset)[[2]]),
    selectInput('color', 'Color', c('None', names(dataset))),
    
    checkboxInput('smooth', 'Smooth'),
    
    selectInput('facet_row', 'Facet Row', c(None='.', names(dataset))),
    selectInput('facet_col', 'Facet Column', c(None='.', names(dataset)))
  ),
  
  mainPanel(
    plotOutput('plot')
  )
)