 ##############################################################################
 #                        Calendar Heatmap                                    #
 #                                by                                          #
 #                         Paul Bleicher                                      #
 # an R version of a graphic from:                                            #
 # http://stat-computing.org/dataexpo/2009/posters/wicklin-allison.pdf        #
 #  requires lattice, chron, grid packages                                    #
 ############################################################################## 

## calendarHeat: An R function to display time-series data as a calendar heatmap 
## Copyright 2009 Humedica. All rights reserved.

## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You can find a copy of the GNU General Public License, Version 2 at:
## http://www.gnu.org/licenses/gpl-2.0.html

calendarHeat <- function(dates, 
                         values, 
                         ncolors=99, 
                         color="r2g", 
                         varname="Values",
                         date.form = "%Y-%m-%d", ...) {
require(lattice)
require(grid)
require(chron)
if (class(dates) == "character" | class(dates) == "factor" ) {
  dates <- strptime(dates, date.form)
        }
caldat <- data.frame(value = values, dates = dates)
min.date <- as.Date(paste(format(min(dates), "%Y"),
                    "-1-1",sep = ""))
max.date <- as.Date(paste(format(max(dates), "%Y"),
                     "-12-31", sep = ""))
dates.f <- data.frame(date.seq = seq(min.date, max.date, by="days"))

# Merge moves data by one day, avoid
caldat <- data.frame(date.seq = seq(min.date, max.date, by="days"), value = NA)
dates <- as.Date(dates) 
caldat$value[match(dates, caldat$date.seq)] <- values

caldat$dotw <- as.numeric(format(caldat$date.seq, "%w"))
caldat$woty <- as.numeric(format(caldat$date.seq, "%U")) + 1
caldat$yr <- as.factor(format(caldat$date.seq, "%Y"))
caldat$month <- as.numeric(format(caldat$date.seq, "%m"))
yrs <- as.character(unique(caldat$yr))
d.loc <- as.numeric()                        
for (m in min(yrs):max(yrs)) {
  d.subset <- which(caldat$yr == m)  
  sub.seq <- seq(1,length(d.subset))
  d.loc <- c(d.loc, sub.seq)
  }  
caldat <- cbind(caldat, seq=d.loc)

#color styles
r2b <- c("#0571B0", "#92C5DE", "#F7F7F7", "#F4A582", "#CA0020") #red to blue                                                                               
r2g <- c("#D61818", "#FFAE63", "#FFFFBD", "#B5E384")   #red to green
w2b <- c("#045A8D", "#2B8CBE", "#74A9CF", "#BDC9E1", "#F1EEF6")   #white to blue
            
assign("col.sty", get(color))
calendar.pal <- colorRampPalette((col.sty), space = "Lab")
def.theme <- lattice.getOption("default.theme")
cal.theme <-
   function() {  
  theme <-
  list(
    strip.background = list(col = "transparent"),
    strip.border = list(col = "transparent"),
    axis.line = list(col="transparent"),
    par.strip.text=list(cex=0.8))
    }
lattice.options(default.theme = cal.theme)
yrs <- (unique(caldat$yr))
nyr <- length(yrs)
print(cal.plot <- levelplot(value~woty*dotw | yr, data=caldat,
   as.table=TRUE,
   aspect=.12,
 layout = c(1, nyr%%7),
   between = list(x=0, y=c(1,1)),
   strip=TRUE,
   main = paste("Calendar Heat Map of ", varname, sep = ""),
   scales = list(
     x = list(
               at= c(seq(2.9, 52, by=4.42)),
               labels = month.abb,
               alternating = c(1, rep(0, (nyr-1))),
               tck=0,
               cex = 0.7),
     y=list(
          at = c(0, 1, 2, 3, 4, 5, 6),
          labels = c("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                      "Friday", "Saturday"),
          alternating = 1,
          cex = 0.6,
          tck=0)),
   xlim =c(0.4, 54.6),
   ylim=c(6.6,-0.6),
   cuts= ncolors - 1,
   col.regions = (calendar.pal(ncolors)),
   xlab="" ,
   ylab="",
   colorkey= list(col = calendar.pal(ncolors), width = 0.6, height = 0.5),
   subscripts=TRUE
    ) )
panel.locs <- trellis.currentLayout()
for (row in 1:nrow(panel.locs)) {
    for (column in 1:ncol(panel.locs))  {
    if (panel.locs[row, column] > 0)
{
    trellis.focus("panel", row = row, column = column,
                  highlight = FALSE)
xyetc <- trellis.panelArgs()
subs <- caldat[xyetc$subscripts,]
dates.fsubs <- caldat[caldat$yr == unique(subs$yr),]
y.start <- dates.fsubs$dotw[1]
y.end   <- dates.fsubs$dotw[nrow(dates.fsubs)]
dates.len <- nrow(dates.fsubs)
adj.start <- dates.fsubs$woty[1]

for (k in 0:6) {
 if (k < y.start) {
    x.start <- adj.start + 0.5
    } else {
    x.start <- adj.start - 0.5
      }
  if (k > y.end) {
     x.finis <- dates.fsubs$woty[nrow(dates.fsubs)] - 0.5
    } else {
     x.finis <- dates.fsubs$woty[nrow(dates.fsubs)] + 0.5
      }
    grid.lines(x = c(x.start, x.finis), y = c(k -0.5, k - 0.5), 
     default.units = "native", gp=gpar(col = "grey", lwd = 1))
     }
if (adj.start <  2) {
 grid.lines(x = c( 0.5,  0.5), y = c(6.5, y.start-0.5), 
      default.units = "native", gp=gpar(col = "grey", lwd = 1))
 grid.lines(x = c(1.5, 1.5), y = c(6.5, -0.5), default.units = "native",
      gp=gpar(col = "grey", lwd = 1))
 grid.lines(x = c(x.finis, x.finis), 
      y = c(dates.fsubs$dotw[dates.len] -0.5, -0.5), default.units = "native",
      gp=gpar(col = "grey", lwd = 1))
 if (dates.fsubs$dotw[dates.len] != 6) {
 grid.lines(x = c(x.finis + 1, x.finis + 1), 
      y = c(dates.fsubs$dotw[dates.len] -0.5, -0.5), default.units = "native",
      gp=gpar(col = "grey", lwd = 1))
      }
 grid.lines(x = c(x.finis, x.finis), 
      y = c(dates.fsubs$dotw[dates.len] -0.5, -0.5), default.units = "native",
      gp=gpar(col = "grey", lwd = 1))
      }
for (n in 1:51) {
  grid.lines(x = c(n + 1.5, n + 1.5), 
    y = c(-0.5, 6.5), default.units = "native", gp=gpar(col = "grey", lwd = 1))
        }
x.start <- adj.start - 0.5

if (y.start > 0) {
  grid.lines(x = c(x.start, x.start + 1),
    y = c(y.start - 0.5, y.start -  0.5), default.units = "native",
    gp=gpar(col = "black", lwd = 1.75))
  grid.lines(x = c(x.start + 1, x.start + 1),
    y = c(y.start - 0.5 , -0.5), default.units = "native",
    gp=gpar(col = "black", lwd = 1.75))
  grid.lines(x = c(x.start, x.start),
    y = c(y.start - 0.5, 6.5), default.units = "native",
    gp=gpar(col = "black", lwd = 1.75))
 if (y.end < 6  ) {
  grid.lines(x = c(x.start + 1, x.finis + 1),
   y = c(-0.5, -0.5), default.units = "native",
   gp=gpar(col = "black", lwd = 1.75))
  grid.lines(x = c(x.start, x.finis),
   y = c(6.5, 6.5), default.units = "native",
   gp=gpar(col = "black", lwd = 1.75))
   } else {
      grid.lines(x = c(x.start + 1, x.finis),
       y = c(-0.5, -0.5), default.units = "native",
       gp=gpar(col = "black", lwd = 1.75))
      grid.lines(x = c(x.start, x.finis),
       y = c(6.5, 6.5), default.units = "native",
       gp=gpar(col = "black", lwd = 1.75))
       }
       } else {
           grid.lines(x = c(x.start, x.start),
            y = c( - 0.5, 6.5), default.units = "native",
            gp=gpar(col = "black", lwd = 1.75))
           }

 if (y.start == 0 ) {
  if (y.end < 6  ) {
  grid.lines(x = c(x.start, x.finis + 1),
   y = c(-0.5, -0.5), default.units = "native",
   gp=gpar(col = "black", lwd = 1.75))
  grid.lines(x = c(x.start, x.finis),
   y = c(6.5, 6.5), default.units = "native",
   gp=gpar(col = "black", lwd = 1.75))
   } else {
      grid.lines(x = c(x.start + 1, x.finis),
       y = c(-0.5, -0.5), default.units = "native",
       gp=gpar(col = "black", lwd = 1.75))
      grid.lines(x = c(x.start, x.finis),
       y = c(6.5, 6.5), default.units = "native",
       gp=gpar(col = "black", lwd = 1.75))
       }
       }
for (j in 1:12)  {
   last.month <- max(dates.fsubs$seq[dates.fsubs$month == j])
   x.last.m <- dates.fsubs$woty[last.month] + 0.5
   y.last.m <- dates.fsubs$dotw[last.month] + 0.5
   grid.lines(x = c(x.last.m, x.last.m), y = c(-0.5, y.last.m),
     default.units = "native", gp=gpar(col = "black", lwd = 1.75))
   if ((y.last.m) < 6) {
      grid.lines(x = c(x.last.m, x.last.m - 1), y = c(y.last.m, y.last.m),
       default.units = "native", gp=gpar(col = "black", lwd = 1.75))
     grid.lines(x = c(x.last.m - 1, x.last.m - 1), y = c(y.last.m, 6.5),
       default.units = "native", gp=gpar(col = "black", lwd = 1.75))
   } else {
      grid.lines(x = c(x.last.m, x.last.m), y = c(- 0.5, 6.5),
       default.units = "native", gp=gpar(col = "black", lwd = 1.75))
    }
 }
 }
 }
trellis.unfocus()
} 
lattice.options(default.theme = def.theme)
}

## Example of use: Plot financial data
## This code is not run.
if(FALSE) {

#create faux data; skip this to use data from a file or stock data
#ndays <- 1500   #set number of days
#dates <- as.POSIXlt(seq(Sys.Date()- ndays, Sys.Date() - 1, by="days"))
#vals <- runif(ndays, -100, 100)

#stock data:
stock <- "MSFT"
start.date <- "2006-01-12"
end.date <- Sys.Date()
quote <- paste("http://ichart.finance.yahoo.com/table.csv?s=",
                stock,
                "&a=", substr(start.date,6,7),
                "&b=", substr(start.date, 9, 10),
                "&c=", substr(start.date, 1,4), 
                "&d=", substr(end.date,6,7),
                "&e=", substr(end.date, 9, 10),
                "&f=", substr(end.date, 1,4),
                "&g=d&ignore=.csv", sep="")             
stock.data <- read.csv(quote, as.is=TRUE)

# Plot as calendar heatmap
calendarHeat(stock.data$Date, stock.data$Adj.Close, varname="MSFT Adjusted Close")
}