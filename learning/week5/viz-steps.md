# Data to Viz in Four Steps

This week's learning objective is to become familiar with the basic
four-step process of going from data to visualization.

* Load Data
* Template
* Map
* Populate

Study the following example carefully.

### Step 1: Load Data

{% set data = {} %}

{% lodash %}

data.countries = [{name: 'China', pop: 1393783836},
 {name: 'India', pop: 1267401849},
 {name: 'USA', pop: 322583006},
 {name: 'Indonesia', pop: 25281224}]

{% endlodash %}

### Step 2: Template

For each data point, think about how we want to visualize it. In particular, we
define how to map a data attribute to a visual attribute. In this simplest
example, we are mapping the _order_ (_i_-th) data attribute to the _x_ visual attribute
of a rectangle.

{% template name='foo' %}

<rect x="${d.x}"
     width="20"
     height="100"
     style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />

{% endtemplate %}

There is a special object `template` that holds user-defined template strings.
Note that a name of this particular template string is set to be `foo`. The
content of the string can be accessed by `template.foo` in a code block.

### Step 3: Map

Next, for each data point, we want to map it to a _viz_ object that defines
the attribute values we like to populate the template with. In this simplest
example, there's only one attribute, _x_.

{% lodash %}

function computeX(d, i) {
    return i * 20
}

data.viz = _.map(data.countries, function(d, i){
        return {
            x: computeX(d, i)
        }    
    })

{% endlodash %}

We obtain the following array of data objects.
{{ data.viz | json }}

### Step 4: Populate

The final step is to populate the template with the viz data calculated earlier.

{% lodash %}

// compile the template.foo into a template function
var compiled = _.template(template.foo)

var result = _.map(data.viz, function(d){
        // invoke the compiled template function on each viz data
        return compiled({d: d})
    })
return result.join('\n')
{% endlodash %}

The resulting svg tags are rendered as below

{{ result | svg }}

# Your Turn

Now it is your turn. The following exercises are incomplete. Your learning
task is to add code to complete each exercise.

## Exercise 1. Use the height of each bar to represent population

### Step 1: Import Data

{% set data = {} %}

{% lodash %}

data.countries = [{name: 'China', pop: 1393783836},
 {name: 'India', pop: 1267401849},
 {name: 'USA', pop: 322583006},
 {name: 'Indonesia', pop: 25281224}]

{% endlodash %}

### Step 2: Define Mappers

{% lodash %}

function computeX(d, i) {
    return i * 20
}

function computeHeight(d, i){
    // TODO: fix this to return the correct height
    return 10 + i * 50
}

data.viz = _.map(data.countries, function(d, i){
        return {
            x: computeX(d, i),
            height: computeHeight(d, i)
        }    
    })

{% endlodash %}

### Step 3: Template

{% template name='foo' %}

<rect x="${d.x}"
     width="20"
     height="${d.height}"
     style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />

{% endtemplate %}

### Step 4: Populate

{% lodash %}

// compile the template.foo into a template function
var compiled = _.template(template.foo)

var result = _.map(data.viz, function(d){
        // invoke the compiled template function on each viz data
        return compiled({d: d})
    })
return result.join('\n')
{% endlodash %}

The resulting svg tags are rendered as below

{{ result | svg }}

## Exercise 2. Use both the height and width of each bar to represent population

### Step 1: Import Data

{% set data = {} %}

{% lodash %}

data.countries = [{name: 'China', pop: 1393783836},
 {name: 'India', pop: 1267401849},
 {name: 'USA', pop: 322583006},
 {name: 'Indonesia', pop: 25281224}]

{% endlodash %}

### Step 2: Define Mappers

{% lodash %}

function computeX(d, i) {
    return i * 20
}

function computeHeight(d, i){
    // TODO: fix this to return the correct height
    return 10 + i * 50
}

// TODO: add a new mapper function for width

data.viz = _.map(data.countries, function(d, i){
        // TODO: add a new attribute to each viz object
        return {
            x: computeX(d, i),
            height: computeHeight(d, i)
        }    
    })

{% endlodash %}

### Step 3: Template

(TODO: add template variables for width and height)
{% template name='foo' %}

<rect x="${d.x}"
     width="20"
     height="20"
     style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />

{% endtemplate %}

### Step 4: Populate

{% lodash %}

// compile the template.foo into a template function
var compiled = _.template(template.foo)

var result = _.map(data.viz, function(d){
        // invoke the compiled template function on each viz data
        return compiled({d: d})
    })
return result.join('\n')
{% endlodash %}

The resulting svg tags are rendered as below

{{ result | svg }}
