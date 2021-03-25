// index.js 

/*
var dataset = [1,2,3,4,5];

d3.select('h1').style('color', 'blue').attr('class','heading').text('updated h1 tag');

d3.select('body').append('board').text('1');
d3.select('body').append('p').text('2');
d3.select('body').append('p').text('3');

d3.selectAll('board').style('color', 'red');

d3.select('body')
.selectAll('p')
.data(dataset)
.enter()//will take the items in the data set 1 by 1 and apply the operations for all of them
.append('p')
.text(function(d) {return d;});
*/

var bars = [80, 100, 50, 180, 50, 40, 30, 180 ,10];
var svgW = 500;
var svgH = 300;

var barP = 10;
var barW = (svgW/bars.length);

var svg = d3.select('svg').attr('width', svgW).attr('height', svgH);

var barChart = svg.selectAll('rect').data(bars).enter().append('rect')
.attr('y',function(d) {return svgH - d})
.attr('height', function(d) {return d})
.attr('width', barW - barP)
.attr('transform', function (d, i){
    var translate = [barW * i, 0];
    return "translate("+translate+")"; 
});

var text = svg.selectAll('text').data(bars).enter().append('text')
.text(function(d){return d;})
.attr('y', function(d){return svgH - d -2;})
.attr('x', function(d, i){return barW * i;})
.attr('fill','#A64C38');
