# Template Engine

In the intro class, you made bar charts by writing plain `<svg>` tags. Imagine
having to do that for lots and lots of data points! No way.

This week, your learning task is to learn how to utilize a template engine to
automate the creation of svg-based data visualization. Fortunately, gitbook has
a template engine built-in already, which is
[nunjuncks](https://mozilla.github.io/nunjucks/). Below are working examples how
to utilize the [for](https://mozilla.github.io/nunjucks/templating.html#for) tag
to render a whole bunch of elements.

## A list of numbers

{% set numbers = [1,2,3,4,5,6,7] %}
{% for number in numbers %}
<li>{{number}}</li>
{% endfor %}

## An array of rectangles
The rectangles below are also generated using the tag.

{% set numbers = [1,2,3,4,5,6,7] %}
<svg width="500" height="200">
{% for number in numbers %}
    <rect x="{{loop.index * 20}}" width="20" height="100" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>

# Challenges

Now it's your team's turn to work together to complete the challenges below.

## 1D Data

### A list of numbers

Draw negative numbers in red and positive numbers in green.

{% set numbers = [43,21,-13,32,20,5,-8,29,9] %}
{% for number in numbers %}
{% if number < 0 %}
<li><font color="red">{{number}}</font></li>
{%else%}
<li><font color="green">{{number}}</font></li>
{%endif%}
{% endfor %}

(Hint: use the [if tag](https://mozilla.github.io/nunjucks/templating.html#if))

### Bar Chart

{% set numbers = [43,21,32,20,5,29,9] %}

* Below should be a bar chart to display the data: {{ numbers }}
* There should be some gaps between the bars.

<svg width="500" height="200">
{% for number in numbers %}
    <rect x="{{loop.index * 20 +loop.index * 10}} " width="20" height="{{number}}" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>

### Bar Chart (Horizontal)

{% set numbers = [43,21,32,20,5,29,9] %}

* Same as the previous, but bars are horizontal.

<svg width="500" height="200">
{% for number in numbers %}
    <rect y="{{loop.index * 20 + loop.index * 10}}" width="{{number}}" height="20" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>

## 2D Data

### Table

{% set data = [[10,15],[20,12],[31,42],[12,52],[33,24]]%}

* Draw a table to display the data, using `<table>`, `<tr>`, `<td>`
* You will need to create a nested for loop.

<table>
    {% for rows in data %}
        <tr>
            {% for number in rows %}
             <td>{{number}}</td>
             {% endfor %}
        </tr>
    {% endfor %}
</table>


### X-Y Plot

{% set data = [[10,15],[20,12],[31,42],[12,52],[33,24]]%}

* Plot the data using `<circle>` to represent each data point.
* Scale the data to nicely occupy the display area

<svg width="500" height="200" style="border:1px solid grey">
{% for point in data %}
    <circle cx="{{point[0] * 14}}" cy="{{point[1] * 3}}" r="2" stroke="black" stroke-width="3" fill="red" />
{% endfor %}
</svg>

### X-Y Plot (Colored)

{% set data = [[10,15,4],[20,12,2],[31,42,6],[12,52,1],[33,24,6]]%}

Now each data point has three values. Extend the previous solution. Use _size_
of the circle to represent the third value.

<svg width="500" height="200" style="border:1px solid grey">
{% for point in data %}
    <circle cx="{{point[0] * 14}}" cy="{{point[1] * 3 }}" r="{{point[2]}}" stroke="black" stroke-width="3" fill="red" />
{% endfor %}
</svg>
