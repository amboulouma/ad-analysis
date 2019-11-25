// set the dimensions and margins of the graph
var margin = {top: 20, right: 20, bottom: 30, left: 50},
width = 800 - margin.left - margin.right,
height = 500 - margin.top - margin.bottom;

// parse the date / time
var parseTime = d3.timeParse("%Y-%m-%d");

// set the ranges
var x = d3.scaleTime().range([0, width]);
var y0 = d3.scaleLinear().range([height, 0]);
var y1 = d3.scaleLinear().range([height, 0]);

// define the line
var valueline = d3.line()
.x(function(d) { return x(d.date); })
.y(function(d) { return y0(d.clicks); });
// define the line
var valueline2 = d3.line()
.x(function(d) { return x(d.date); })
.y(function(d) { return y1(d.impressions); });

// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("#chart").append("svg")
        .attr("align","center")
        .attr("width", width + margin.left + margin.right + 200)
        .attr("height", height + margin.top + margin.bottom)
        .call(d3.zoom().on("zoom", function () {
            svg.attr("transform", d3.event.transform)
         }))
    .append("g")
        .attr("transform","translate(" + margin.left + "," + margin.top + ")");

function draw(data, compaigns) {
    var data = data[compaigns];
    // format the data
    data.forEach(function(d) {
        d.date = parseTime(d.date);
        d.clicks = +d.clicks;
        d.impressions = +d.impressions;
    });

    // sort years ascending
    data.sort(function(a, b){
        return a["date"]-b["date"];
    })

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y0.domain([0, d3.max(data, function(d) { return Math.max(d.clicks); })]); 
    y1.domain([0, d3.max(data, function(d) { return Math.max(d.impressions); })]);

    // Add the valueline path.
    svg.append("path")
        .data([data])
        .style("stroke", "steelblue")
        .attr("class", "line")
        .attr("d", valueline);
    // Add the valueline path.
    svg.append("path")
        .data([data])
        .style("stroke", "red")
        .attr("class", "line")
        .attr("d", valueline2);  

    // Add the X Axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
    // Add the Y0 Axis
    svg.append("g")
        .style("fill", "steelblue")
        .attr("class", "Clicks")
        .call(d3.axisLeft(y0));
    // Add the Y1 Axis
    svg.append("g")
        .style("fill", "red")
        .attr("class", "Impressions")
        .attr("transform", "translate( " + width + ", 0 )")
        .call(d3.axisRight(y1));   
    }

// Get the data
d3.json("http://127.0.0.1:8000/fetch_data/", function(error, data) {
    if (error) throw error;
    // trigger render
    draw(data, "compaigns");
    });