# Warmup

Complete this warmup exercise to get an idea how to put all the different pieces
together to generate an end-to-end data analysis viz report.

<a name="top"/>
<div id="autonav"></div>

{% data src="../fcq/fcq.clean.json" %}
{% enddata %}

{% viz %}

{% title %}

What is the distribution of courses across colleges?

{% solution %}

var groups = _.groupBy(data, function(d){
    return d['CrsPBAColl']
})

// TODO: add real code to convert groups (which is an object) into an array like below
// This array should have a lot more elements.
var counts = _.mapValues(groups, function(n){return _.size(n)})
var counts = _.map(counts, function(value,key){return {"name": key , "value": value}})

console.log(counts)

// TODO: modify the code below to produce a nice vertical bar charts

function computeLabel(d, i){
	return d.name
}

function computeX(d, i) {
    return i * 20 + (i * 20)/2
}

function computeHeight(d, i) {
	return d.value/10
}

function computeWidth(d, i) {
    return 20 * i + 100
}

function computeY(d, i) {
    return 323.7 - d.value/10
}

function computeColor(d, i) {
    return 'red'
}

var viz = _.map(counts, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i),
                color: computeColor(d, i),
                label: computeLabel(d,i)
            }
         })
console.log(viz)

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')

{% template %}

<rect x="${d.x}"
      y="${d.y}"
      height="${d.height}"
      width="20"
      style="fill:${d.color};
             stroke-width:3;
             stroke:rgb(0,0,0)" />
<text transform="translate(${d.x} 340)">
        ${d.label}
    </text>

{% endviz %}
