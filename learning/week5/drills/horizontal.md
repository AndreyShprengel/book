{% vizexercise %}

{% title %}

Display bars horizontally

{% data %}

[{name: 'China', pop: 1393783836},
 {name: 'India', pop: 1267401849},
 {name: 'USA', pop: 322583006},
 {name: 'Indonesia', pop: 252812243}]

{% solution %}

function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
    return 20
}

function computeWidth(d, i) {
    return 20 * i + 100
}

function computeY(d, i) {
    return 20 * i
}

function computeColor(d, i) {
    return 'red'
}

var viz = _.map(data, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i),
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
     width="${d.width}"
     height="${d.height}"
     style="fill:${d.color};
            stroke-width:3;
            stroke:rgb(0,0,0)" />

{% output %}

<rect x="0"
      y="0"
     width="300"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="0"
      y="20"
     width="272.79736274685854"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="0"
      y="40"
     width="69.43322149418297"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="0"
      y="60"
     width="54.415663993968145"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />

{% endvizexercise %}
