{% vizexercise %}

{% title %}

Compare attack and defense points side by side

{% data %}
[
  {
    "Name": "Squirtle",
    "Type": "WATER",
    "HP": 44,
    "Attack": 48,
    "Defense": 65,
    "Special Attack": 50,
    "Special Defense": 64,
    "Speed": 43
  },
  {
    "Name": "Mega Charizard Y",
    "Type": "FLYING",
    "HP": 78,
    "Attack": 104,
    "Defense": 78,
    "Special Attack": 159,
    "Special Defense": 115,
    "Speed": 100
  },  
  {
    "Name": "Charmander",
    "Type": "FIRE",
    "HP": 39,
    "Attack": 52,
    "Defense": 43,
    "Special Attack": 60,
    "Special Defense": 50,
    "Speed": 65
  },  
  {
    "Name": "Mega Venusaur",
    "Type": "GRASS",
    "HP": 80,
    "Attack": 100,
    "Defense": 123,
    "Special Attack": 122,
    "Special Defense": 120,
    "Speed": 80
  },  
  {
    "Name": "Venusaur",
    "Type": "GRASS",
    "HP": 80,
    "Attack": 82,
    "Defense": 83,
    "Special Attack": 100,
    "Special Defense": 100,
    "Speed": 80
  },    
  {
    "Name": "Ivysaur",
    "Type": "GRASS",
    "HP": 60,
    "Attack": 62,
    "Defense": 63,
    "Special Attack": 80,
    "Special Defense": 80,
    "Speed": 60
  },    
  {
    "Name": "Bulbasaur",
    "Type": "GRASS",
    "HP": 45,
    "Attack": 49,
    "Defense": 49,
    "Special Attack": 65,
    "Special Defense": 65,
    "Speed": 45
  }  
]
{% solution %}

function computeX(d, i) {
    return 0
}

function computeWidth(d, i) {
    return i * 10 + 10
}

function computeY(d, i) {
    return i * 20
}

function computeColor(d, i) {
    return 'red'
}

var viz = _.map(data, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
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
<g transform="translate(120 ${d.y})">
    <rect
         x="-${d.width}"
         width="${d.width}"
         height="20"
         style="fill:${d.color};
                stroke-width:1;
                stroke:rgb(0,0,0)" />
</g>

{% output %}

<g transform="translate(120 0)">
    <rect
         x="-48"
         width="48"
         height="20"
         style="fill:red;
                stroke-width:1;
                stroke:rgb(0,0,0)" />
    <rect
         x="0"
         width="65"
         height="20"
         style="fill:blue;
                stroke-width:1;
                stroke:rgb(0,0,0)" />

    <text transform="translate(0 15)">
        Squirtle
    </text>
</g>
<g transform="translate(120 20)">
    <rect
         x="-104"
         width="104"
         height="20"
         style="fill:red;
                stroke-width:1;
                stroke:rgb(0,0,0)" />
    <rect
         x="0"
         width="78"
         height="20"
         style="fill:blue;
                stroke-width:1;
                stroke:rgb(0,0,0)" />

    <text transform="translate(0 15)">
        Mega Charizard Y
    </text>
</g>
<g transform="translate(120 40)">
    <rect
         x="-52"
         width="52"
         height="20"
         style="fill:red;
                stroke-width:1;
                stroke:rgb(0,0,0)" />
    <rect
         x="0"
         width="43"
         height="20"
         style="fill:blue;
                stroke-width:1;
                stroke:rgb(0,0,0)" />

    <text transform="translate(0 15)">
        Charmander
    </text>
</g>
<g transform="translate(120 60)">
    <rect
         x="-100"
         width="100"
         height="20"
         style="fill:red;
                stroke-width:1;
                stroke:rgb(0,0,0)" />
    <rect
         x="0"
         width="123"
         height="20"
         style="fill:blue;
                stroke-width:1;
                stroke:rgb(0,0,0)" />

    <text transform="translate(0 15)">
        Mega Venusaur
    </text>
</g>
<g transform="translate(120 80)">
    <rect
         x="-82"
         width="82"
         height="20"
         style="fill:red;
                stroke-width:1;
                stroke:rgb(0,0,0)" />
    <rect
         x="0"
         width="83"
         height="20"
         style="fill:blue;
                stroke-width:1;
                stroke:rgb(0,0,0)" />

    <text transform="translate(0 15)">
        Venusaur
    </text>
</g>
<g transform="translate(120 100)">
    <rect
         x="-62"
         width="62"
         height="20"
         style="fill:red;
                stroke-width:1;
                stroke:rgb(0,0,0)" />
    <rect
         x="0"
         width="63"
         height="20"
         style="fill:blue;
                stroke-width:1;
                stroke:rgb(0,0,0)" />

    <text transform="translate(0 15)">
        Ivysaur
    </text>
</g>
<g transform="translate(120 120)">
    <rect
         x="-49"
         width="49"
         height="20"
         style="fill:red;
                stroke-width:1;
                stroke:rgb(0,0,0)" />
    <rect
         x="0"
         width="49"
         height="20"
         style="fill:blue;
                stroke-width:1;
                stroke:rgb(0,0,0)" />

    <text transform="translate(0 15)">
        Bulbasaur
    </text>
</g>

{% endvizexercise %}
