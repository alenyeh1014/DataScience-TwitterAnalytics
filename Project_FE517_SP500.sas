* Basic Statistical Analysis for each dataset;

%macro analysis (dsn= &dsn.);
proc univariate data = &dsn.;
	var close;
run;
	
%mend analysis;

%analysis (dsn = AAPL);
%analysis (dsn = GE);
%analysis (dsn = MS);
%analysis (dsn = SP500);


/* create example data: AAPL stock price */

%macro timeseries (dsnn = &dsnn.);
title "10Y &dsnn Close Price";
proc sgplot data =&dsnn.;
	series x = Date y = close ;
	xaxis label = 'Date'
	min = '01JAN2010'd max = '01DEC2018'd;
	run;
%mend timeseries;

%timeseries (dsnn=AAPL);
%timeseries (dsnn=GE);
%timeseries (dsnn=MS);
%timeseries (dsnn=SP500);


 /* create three moving average curves */
proc expand data=SP500 out=WORK.SMA_SP500 method=none;
id DATE;  convert CLOSE = SMA_short   / transout=(movave 50); convert CLOSE = SMA_long   / transout=(movave 200);
run;



PROC SQL;
CREATE TABLE test as 
SELECT date, close FROM SMA_SP500;
QUIT;



PROC SQL;
CREATE TABLE test_a as 
SELECT date, close, SMA_short FROM SMA_SP500
WHERE date >"16MAR2010"d;
QUIT;



PROC SQL;
CREATE TABLE test_b as 
SELECT date, close, SMA_long FROM SMA_SP500
WHERE date >"18OCT2010"d;
QUIT;



PROC SQL;
CREATE TABLE sma_plot AS
SELECT a.*, b.SMA_short FROM test a 
LEFT JOIN test_a b on a.date = b.date 
ORDER BY date;
QUIT;



PROC SQL;
CREATE TABLE sma_plotb AS
SELECT a.*, b.SMA_long FROM sma_plot a 
LEFT JOIN test_b b on a.date = b.date 
ORDER BY date;
QUIT;



Title "SMA_short v.s. SMA_long Closing Price";
proc sgplot data=Sma_plotb cycleattrs;
   series x=Date  y= Close / name ='Closing_Price'  legendlabel = 'Closing_Price';
   series x=Date  y=SMA_short  / name='SMA_short'   legendlabel="SMA_short(50)";
   series x=Date  y=SMA_long   / name='SMA_long'  legendlabel="SMA_long(200)";
   xaxis display=(nolabel) grid;
   yaxis label="Closing Price" grid;
 run;



DATA SMA_SP500b;
       SET SMA_SP500;
	   L1_short=lag1(SMA_short);
	   L1_long=lag1(SMA_long);
	   if date>="18OCT2010"d;
RUN;



PROC SQL;
CREATE TABLE buy_signal_SP500 AS
SELECT date, close, "buy" AS signal FROM SMA_SP500b
WHERE L1_short<L1_long AND SMA_short>=SMA_long;
QUIT;



PROC SQL;
CREATE TABLE sell_signal_SP500 AS
SELECT date, close, "sell" AS signal FROM SMA_SP500b
WHERE L1_short>L1_long AND SMA_short<=SMA_long;
QUIT;



PROC SQL;
CREATE TABLE signal_SP500 AS
SELECT * FROM buy_signal_SP500
UNION
SELECT * FROM sell_signal_SP500
ORDER BY date;
QUIT;

  

PROC SQL;
CREATE TABLE return_SP500a AS
SELECT date, close, 0 AS return_SMA FROM SMA_SP500
WHERE date<"22OCT2010"d;

CREATE TABLE return_SP500b AS
SELECT date, close, ((close-1183.079956)/1183.079956) AS return_SMA FROM SMA_SP500
WHERE date>="22OCT2010"d AND date<="12AUG2011"d;

CREATE TABLE return_SP500c AS
SELECT date, close, ((1178.810059-1183.079956)/1183.079956) AS return_SMA FROM SMA_SP500
WHERE date>"12AUG2011"d AND date<"31JAN2012"d;

CREATE TABLE return_SP500d AS
SELECT date, close, ((close-1312.410034)/1312.410034+(1178.810059-1183.079956)/1183.079956) AS return_SMA FROM SMA_SP500
WHERE date>="31JAN2012"d AND date<="28AUG2015"d;

CREATE TABLE return_SP500e AS
SELECT date, close, ((1988.869995-1312.410034)/1312.410034+(1178.810059-1183.079956)/1183.079956) AS return_SMA FROM SMA_SP500
WHERE date>"28AUG2015"d AND date<"21OCT2015"d;

CREATE TABLE return_SP500f AS
SELECT date, close, ((close-2021.150024)/2021.150024+(1988.869995-1312.410034)/1312.410034+(1178.810059-1183.079956)/1183.079956) AS return_SMA FROM SMA_SP500
WHERE date>="21OCT2015"d AND date<="11JAN2016"d;

CREATE TABLE return_SP500g AS
SELECT date, close, ((1923.670044-2021.150024)/2021.150024+(1988.869995-1312.410034)/1312.410034+(1178.810059-1183.079956)/1183.079956) AS return_SMA FROM SMA_SP500
WHERE date>"11JAN2016"d AND date<"25APR2016"d;

CREATE TABLE return_SP500h AS
SELECT date, close, ((close-2087.790039)/2087.790039+(1923.670044-2021.150024)/2021.150024+(1988.869995-1312.410034)/1312.410034+(1178.810059-1183.079956)/1183.079956) AS return_SMA FROM SMA_SP500
WHERE date>="25APR2016"d;

CREATE TABLE return_SP500i AS
SELECT * FROM return_SP500a
UNION
SELECT * FROM return_SP500b
UNION
SELECT * FROM return_SP500c
UNION
SELECT * FROM return_SP500d
UNION
SELECT * FROM return_SP500e
UNION
SELECT * FROM return_SP500f
UNION
SELECT * FROM return_SP500g
UNION
SELECT * FROM return_SP500h
ORDER BY date;

CREATE TABLE return_SP500 AS
SELECT *, ((close-1132.98999)/1132.98999) AS return_hold FROM return_SP500i;
QUIT;


Title1 "Return_SMA v.s. Return_hold of SP500";
proc sgplot data=Return_SP500 cycleattrs;
   series x=Date y= return_SMA / name ='Return_SMA'  legendlabel = 'Return_SMA';
   series x=Date y = return_hold   / name='Return_hold'   legendlabel="Return_hold";
   xaxis display=(nolabel) grid;
   yaxis label="Return Price" grid;
 run;




