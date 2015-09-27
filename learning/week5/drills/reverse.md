{% vizexercise %}

{% title %}

Reverse the order of the bars

{% data %}

[{name: 'China', pop: 1393783836},
 {name: 'India', pop: 1267401849},
 {name: 'USA', pop: 322583006},
 {name: 'Indonesia', pop: 252812243}]

{% solution %}

function computeX(d, i) {
    return i * 20
}

function computeHeight(d, i) {
    return d.pop * (400 / 1393783836)
}

function computeY(d, i) {
    return 400 - computeHeight(d,i)
}

function computeColor(d, i) {
    return 'red'
}

var viz = _.map(data, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                color: computeColor(d, i)
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
     width="20"
     height="${d.height}"
     style="fill:${d.color};
            stroke-width:3;
            stroke:rgb(0,0,0)" />

{% output %}

<rect x="0"
      y="327.4457813413758"
     width="20"
     height="72.5542186586242"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="20"
      y="307.4223713410894"
     width="20"
     height="92.57762865891063"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="40"
      y="36.270183004188596"
     width="20"
     height="363.7298169958114"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="60"
      y="0"
     width="20"
     height="400"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />

{% endvizexercise %}
