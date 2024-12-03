//Define data
let data = [
  { Country: 'China'    , Deaths: 651699 },
  { Country: 'Haiti'    , Deaths: 318278 },
  { Country: 'Japan'   , Deaths: 167246 },
  { Country: 'Iran', Deaths: 155076 },
  { Country: 'Turkey'  , Deaths: 148459 },
  { Country: 'Pakistan'  , Deaths: 143734 },
  { Country: 'Italy'  , Deaths: 143734 },
  { Country: 'Turkmenistan'  , Deaths: 110411 },
  { Country: 'Peru'  , Deaths: 70148 },
  { Country: 'India'  , Deaths: 54426 }
];

let 
  width = 1000,
  height = 400;

let margin = {
  top:30,
  bottom: 50,
  left: 100,
  right:30
}

// Make a canvas for the picture
let svg = d3.select('body')
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .style('background', 'white')

// Define the scale
let yScale = d3.scaleLinear() // for the continous data
              .domain([0,700000]) //the data
              .range([height - margin.bottom, margin.top])

let xScale = d3.scaleBand()
              .domain(data.map(d => d.Country))
              .range([margin.left, width - margin.right])
              .padding(0.5);

// Draw the axis
let yAxis = svg.append('g')
            .call(d3.axisLeft().scale(yScale))
            .attr('transform', `translate(${margin.left},0)`)

let xAxis  = svg.append('g')
            .call(d3.axisBottom().scale(xScale))
            .attr('transform', `translate(0,${height-margin.bottom})`)

//Draw the labels

svg.append('text')
  .attr('x', width/2)
  .attr('y', height - 15)
  .text('Country')
  .style('text-anchor', 'middle')

svg.append('text')
  .attr('x', 0 - height/2)
  .attr('y', 25)
  .text('Deaths')
  .attr('transform', 'rotate(-90)')

//Draw the bars
bar = svg.selectAll('rect')
      .data(data)
      .enter()
      .append('rect')
      .attr('x', d => xScale(d.Country))
      .attr('y', d => yScale(d.Deaths))
      .attr('width', xScale.bandwidth())
      .attr('height', d => height - margin.bottom - yScale(d.Deaths))
      .attr('fill', 'darkblue')


// Add labels on top of bars
svg.selectAll('.bar-label')
    .data(data)
    .enter()
    .append('text')
    .attr('x', d => xScale(d.Country) + xScale.bandwidth() / 2)
    .attr('y', d => yScale(d.Deaths) - 5)
    .text(d => d.Deaths.toLocaleString())
    .attr('text-anchor', 'middle')
    .style('font-size', '10px')
    .style('fill', 'black')
