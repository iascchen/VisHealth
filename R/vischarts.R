setwd("D:\\PythonWorkspaces\\VisHealth\\R")

# library("RJSONIO")
# bandjson = fromJSON("../data/jawboneup/users_band_start.json")

band <- read.csv("users_band_start.csv")
band$date <- as.POSIXlt( as.POSIXct( band$time , origin='1970-1-1' ) )
band$wday <- band$date$wday
band$mday <- band$date$mday
band$hour <- band$date$hour 
band$mon <- band$date$mon + 1

head(band)

# ================================
# Bar

bucketBar <- function( data , dateCol = "date" , valueCol = "steps" , statics = "sum", 
	bucketSize = "hour" , facetCol = NA , islog2 = FALSE , picTitle = NA){
	require("ggplot2")
	require("reshape2")

	date <- data[, dateCol]

	if( bucketSize == "hour" )
		data["sumby"] <- data[, dateCol]$hour
	else if( bucketSize == "mday" )
		data["sumby"] <- data[, dateCol]$mday
	else if( bucketSize == "wday" )
		data["sumby"] <- data[, dateCol]$wday
	else if( bucketSize == "mon" )
		data["sumby"] <- data[, dateCol]$mon + 1
	else if( bucketSize == "year" )
		data["sumby"] <- data[, dateCol]$year + 1900
	else if( bucketSize == "yday" )
		data["sumby"] <- data[, dateCol]$yday
	else {
		print ( "bucketSize MUST in hour, mday , wday , yday , mon, year" )
		return 
	}

	if( is.na(facetCol) )
		data.mtx <- tapply(data[ , valueCol ] , list( data$sumby ) , statics)
	else
		data.mtx <- tapply(data[ , valueCol ] , list(data[ , facetCol ] , data$sumby) , statics)

	data.mtx [is.na(data.mtx )]= 0
	
	if( islog2 ){
		data.mtx[ data.mtx == 0 ] = 1
		data.mtx <- log(data.mtx , 2)
	}

	# print("data.mtx : ")
	# print(data.mtx)

	m <- melt( data.mtx )
	if( is.na(facetCol) )
    	names(m) <- c( "sumby" , "values" )
    else
    	names(m) <- c( "facet" , "sumby" , "values" )

	pic <- ggplot(m, aes(x = sumby , y = values)) +
  		geom_bar(fill='lightblue', color='white', stat='identity' , binwidth = 1) +    		
  		theme_bw() + 
  		xlab( bucketSize ) +
  		ylab( valueCol )

  	if( is.na(facetCol) )
  		pic <- pic + 
  			ggtitle( paste( bucketSize , " Bar -- " , valueCol))
  	else
		pic <- pic + 
			facet_wrap(~facet, ncol = 7 ) + 
			ggtitle( paste(bucketSize , " Bar -- " , valueCol , " facet by " , facetCol ))

	if( ! is.na(picTitle) )
  		pic <- pic + ggtitle( picTitle )

  	pic
}

pic1 <- bucketBar( band , facetCol = "aerobic" , valueCol = "steps" , bucketSize = "hour")
ggsave(plot = pic1, filename = "steps_in_hour_by_aerobic.png" , height=5 , width=7)

pic2 <- bucketBar( band , facetCol = "wday" , valueCol = "calories" , bucketSize = "hour",
	picTitle = "bucketBar in weekday : mean calories, facet by hour")
ggsave(plot = pic2, filename = "calories_in_hour_by_wday.png", height=4 , width=14)

pic3 <- bucketBar( band , facetCol = "mday" , valueCol = "steps" , bucketSize = "hour" , 
	picTitle = "bucketBar in hour : Steps, facet by Day")
ggsave(plot = pic3, filename = "steps_in_hour_by_mday.png")

# ================================
# Heatmap

bucketHeatmap <- function( data , dateCol = "date" , valueCol = "steps" , statics = "sum", 
	islog2 = FALSE , picTitle = NA){
	require("ggplot2")
	require("reshape2")

	data["sumby"] <- data[, dateCol]$hour
	data["daystr"] <- format ( data[, dateCol] , "%Y-%m-%d")

	data.mtx <- tapply(data[ , valueCol ] , list( data$sumby , data$daystr ) , statics)
	data.mtx [is.na(data.mtx )]= 0
	
	if( islog2 ){
		data.mtx[ data.mtx == 0 ] = 1
		data.mtx <- log(data.mtx , 2)
	}

	# print("data.mtx : ")
	# print(data.mtx)
	
	m <- melt( data.mtx )
	names(m) <- c( "sumby" , "daystr" , "values" )

	# print(head(m))

  	pic <- ggplot(m, aes(x = sumby, y = daystr, fill= values)) +
  		theme_bw() + 
    	xlab("Hour") +
    	ylab("") +
    	scale_x_continuous(breaks = seq( 0, 24 , by = 3 )) +
    	geom_tile(color="white", size= 1 ) +
    	scale_fill_gradient(low='white', high='red' , guide="none") +
		ggtitle( paste( "Hour Heatmap -- " , valueCol))

	if( ! is.na(picTitle) )
  		pic <- pic + ggtitle( picTitle )

  	pic
}

pic4 <- bucketHeatmap( band , valueCol = "steps", picTitle = "Heatmap in hour : Steps" , islog2 = TRUE)
ggsave(plot = pic4, filename = "steps_in_hour_by_mday_heatmap.png")

# ================================
# calander heatmap

labelMon <- c("JAN","FEB","MAR","APR","MAY","JUN","JUL", "AUG","SEP","OCT","NOV","DEC")
# labelMon <- c("一月","二月","三月","四月","五月","六月","七月", "八月","九月","十月","十一月","十二月")
labelWeek <- c("Mon", "Tue", "Wed", "Thu", "Fri", "Sat" , "Sun")
# labelWeek <- c("周一","周二","周三","周四","周五","周六","周日")

calendarHeatmap <- function( data , dateCol = "date" , valueCol = "steps" , statics = "sum",
	islog2 = FALSE , picTitle = NA , isguide = FALSE ){
	require("ggplot2")
	require("reshape2")

	data["daystr"] <- format ( data[, dateCol] , "%Y-%m-%d")

	data.mtx <- tapply(data[ , valueCol ] , list( data$daystr ) , statics)
	data.mtx [is.na(data.mtx )]= 0
	
	if( islog2 ){
		data.mtx[ data.mtx == 0 ] = 1
		data.mtx <- log(data.mtx , 2)
	}

	m <- melt( data.mtx )
	names(m) <- c( "daystr" , "values" )

	m$date <- strptime ( m$daystr , format="%Y-%m-%d" )

	m$mday = m$date$mday

	m$month <- m$date$mon + 1
	m$monthf <- factor(m$month , levels=as.character(1:12), labels=labelMon, ordered=TRUE)

	m$weekday = m$date$wday
	m$weekday[ m$weekday == 0 ] = 7
	m$weekdayf <- factor( m$weekday ,levels=c(1:7), labels=labelWeek,ordered=TRUE)

	m$week <-  as.numeric(format( m$date ,"%W"))

	print(head(m))

  	pic <- ggplot(m, aes( weekdayf, week, fill = values)) +
  		geom_tile(color="white", size= 1 ) +
  		# facet_wrap(~ monthf ,nrow=3) +
  		theme_bw() + 
  		xlab("") +
  		ylab("Week of Year") +
		scale_y_reverse() +
    	geom_text(aes(label = round( mday , 2 ) ) , vjust = 1)

    if( isguide )
      	pic <- pic + scale_fill_gradient(limits=c(0, max(m$values)), low='white', high='red')
    else
        pic <- pic + scale_fill_gradient(limits=c(0, max(m$values)), low='white', high='red' , guide="none")

	if( ! is.na(picTitle) )
  		pic <- pic + ggtitle( picTitle )

  	pic
}

pic6 <- calendarHeatmap( band , valueCol = "steps", picTitle = "Heatmap in hour : Steps" , islog2 = FALSE)
ggsave(plot = pic6, filename = "steps_in_hour_by_calendarheatmap.png")

calendarHeatmap1 <- function( data , dateCol = "date" , valueCol = "steps" , statics = "sum", 
	color = "r2g", islog2 = FALSE , picTitle = NA){
	require("ggplot2")
	require("reshape2")

	source( "calendarHeat.R" )

	data["daystr"] <- format ( data[, dateCol] , "%Y-%m-%d")

	data.mtx <- tapply(data[ , valueCol ] , list( data$daystr ) , statics)
	data.mtx [is.na(data.mtx )]= 0
	
	if( islog2 ){
		data.mtx[ data.mtx == 0 ] = 1
		data.mtx <- log(data.mtx , 2)
	}

	m <- melt( data.mtx )
	names(m) <- c( "daystr" , "values" )
	m$date <- strptime ( m$daystr , format="%Y-%m-%d" )

	pic <- calendarHeat(dates = m$date, values = m$values, statics = "sum" , ncolors=99, color=color, 
		varname="Values", date.form = "%Y-%m-%d")
	pic
}

png(file = "year_calendar.png", bg = "transparent")
	calendarHeatmap1( band , valueCol = "steps", picTitle = "Heatmap in hour : Steps" , islog2 = TRUE , color = "r2g")
dev.off()

# ================================
# sleep quality

setwd("D:\\PythonWorkspaces\\VisHealth\\R")
trends.daily <- read.csv("users_trends-day.csv" , as.is=TRUE)
names( trends.daily )
sleeps <- trends.daily[ , c( "datestr" , "s_light" , "s_deep" , "s_duration" ) ]
sleeps.clean <- subset( sleeps , ! (is.na( s_duration ) | is.na( s_deep ) | ( s_duration == 0) | ( s_deep == 0) 
	| ( s_deep == "None" ) | ( s_duration == "None" ) ) )
sleeps.clean$q <- as.numeric(sleeps.clean$s_deep) / as.numeric(sleeps.clean$s_duration)

sleeps.clean$date <- strptime ( sleeps.clean$datestr , format="%Y%m%d" )

sleeps.clean$s_light <- as.numeric( sleeps.clean$s_light )
sleeps.clean$s_deep <- as.numeric( sleeps.clean$s_deep )
sleeps.clean$s_duration <- as.numeric( sleeps.clean$s_duration )
sleeps.clean <- subset( sleeps.clean , s_light > 0.1  )

pic7 <- bucketBar( sleeps.clean , valueCol = "q" , bucketSize = "mday", statics = "mean")
ggsave(plot = pic7, filename = "sleep_q_bar.png")

pic8 <- calendarHeatmap(  sleeps.clean , valueCol = "q", picTitle = "Heatmap of deep sleep percent" , islog2 = FALSE , isguide = TRUE)
ggsave(plot = pic8, filename = "sleep_q_calendarheatmap.png")

# add them in one page

library(gridExtra) 
g1 <- tableGrob(summary( sleeps.clean[,2:5], digits = 2 ))
g2 <- arrangeGrob(g1, pic7, ncol=2)

png(file = "sleep_q_all.png", bg = "transparent" , width = 800, height = 800, units = "px")
	grid.arrange(pic8, g2,  ncol=1, main="Sleeps")
dev.off()
