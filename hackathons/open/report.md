# Report

Use only Javascript and SVG to produce a data analysis / visualization report.

# Authors

This report is prepared by
* [Full name](link to github account)
* [Full name](link to github account)
* [Full name](link to github account)

<a name="top"/>
<div id="autonav"></div>

{% data src="../fcq/fcq.clean.json" %}
{% enddata %}

# (Question 1)
{% viz %}

{% title %}

What is the average GPA across colleges?

{% solution %}
var groups=_.groupBy(data, function(group){
	return group['CrsPBAColl']
})
var avgJson=_.mapValues(groups, function(group){
    return _.sum(group, function(e){
    	return e["AVG_GRD"]
    })/_.size(group)
})
var keys=_.keys(avgJson)
var avgList=_.map(keys, function(key){
	return {"name": key, "AvgGPA": avgJson[key]}
})
console.log(avgList)

function computeX(d, i) {
    return 50*i
}

function computeHeight(d, i) {
    return d['AvgGPA']*70
}

function computeWidth(d, i) {
    return 20 
}

function computeY(d, i) {
    return 400-d['AvgGPA']*70
}

function computeColor(d, i) {
    return 'red'
}

var viz = _.map(avgList, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i),
                color: computeColor(d, i),
                label: d
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
      width="${d.width}"
      style="fill:${d.color};
             stroke-width:3;
             stroke:rgb(0,0,0)" />
<text x="${d.x}" y="${d.y}">${d.label.name}</text>
{% endviz %}


Use the warmup exercise as the template to produce an answer here.

# (Question 2)

{% viz %}

{% title %}
What is the enrollment across colleges?

{% solution %}

var groups = _.groupBy(data, function(d){
    return d['CrsPBAColl']
})

var count = _.mapValues(groups, function(g) {
    return _.sum(_.pluck(g, 'N.ENROLL'))
})

var keys = _.keys(count)

var final = _.map(keys, function(key) {
    return {"name": key, "enroll": count[key]}
})

console.log(final)

/* SVG Functions */
function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
    return 20
}

function computeWidth(d, i) {
    return d.enroll / 200
}

function computeY(d, i) {
    return 35 * i
}

function computeColor(d, i) {
    return 'teal'
}

function computeLabel(d, i) {
    return d.name
}

function computeLabel2(d, i) {
	return d.enroll
}

var viz = _.map(final, function(d, i){
    return {
        x: computeX(d, i),
        y: computeY(d, i),
        height: computeHeight(d, i),
        width: computeWidth(d, i),
        color: computeColor(d, i),
        label: computeLabel(d, i),
        count: computeLabel2(d, i)
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
      width="${d.width}"
      style="fill:${d.color};
             stroke-width:1;
             stroke:rgb(0,0,0)" />
<text x="${d.width + 8}" y="${d.y + 17}">
    ${d.label}: ${d.count}
</text>
{% endviz %}

{% viz %}

{% title %}
What is the average instructor rating across CS classes?

{% solution %}

var groups = _.filter(data, function(d){
    if (d.Subject === "CSCI") 
      return d
})

groups = _.groupBy(groups, function(n) {
  return n.CourseTitle
})

var count = _.mapValues(groups, function(g) {
    return _.sum(_.pluck(g, 'AvgInstructor')) / g.length
})

var keys = _.keys(count)

var final = _.map(keys, function(key) {
    return {"name": key, "rating": count[key]}
})

console.log(count)

/* SVG Functions */
function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
    return 10
}

function computeWidth(d, i) {
    return d.rating * 10
}

function computeY(d, i) {
    return 25 * i
}

function computeColor(d, i) {
    return 'green'
}

function computeLabel(d, i) {
    return d.name
}

function computeLabel2(d, i) {
  return d.rating
}

var viz = _.map(final, function(d, i){
    return {
        x: computeX(d, i),
        y: computeY(d, i),
        height: computeHeight(d, i),
        width: computeWidth(d, i),
        color: computeColor(d, i),
        label: computeLabel(d, i),
        count: computeLabel2(d, i)
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
      width="${d.width}"
      style="fill:${d.color};
             stroke-width:0;
             stroke:rgb(0,0,0)" />
<text x="${d.width + 8}" y="${d.y + 12}">
    ${d.label}: ${d.count}
</text>
{% endviz %}
