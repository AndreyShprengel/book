{% data src="birdstrikes.json" %}
{% enddata %}

# Report

As a team, answer a subset of the questions submitted during the hackathon.
But instead of using Tableau, you will need to write Javascript/Lodash code
to derive your answers. Similar to before, each team member is responsible for
one question. But everyone should work together to come up with a good solution.
Your answer should consist of Lodash code and a brief writeup.
Utilize `_.map`, `_.filter`, `_.group` ...etc. Do not se any for loop.

This time, the data is not already prepared for you in a nice JSON format. You
will need to do it on your own, replacing the placeholder `birdstrike.json` with
real data.

# (What phase of flight do strikes occour most often) by (Andrey Shprengel)

{% lodash %}
grps = _.groupBy(data, "When: Phase of flight")
grps = _.pick(grps, function(value, key){return key != ""})
grps =  _.mapValues(grps, function(value, key){
	return _.size(value)})
grps = _.pairs(grps)
grps = _.sortBy(grps, function(n){
	return n[1]}).reverse()
return grps
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# What are the top 5 bird species that are involved? (Caleb Hsu)

{% lodash %}
var species = _.groupBy(data, 'Wildlife: Species')
var birds = _.mapValues(species, function(s) {
    return s.length
})
var clean = _.pick(birds, function(value, key) {
    return key[0] != "U"
})

return _.sortBy(_.pairs(clean), function(c) {
    return c[1]
}).reverse().slice(0, 5)

{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# (How many flights were canceled by birdstrikes?) by (Andrew Linenfelser)
{% lodash %}
var group = _.groupBy(data, 'Effect: Impact to flight')
var types = _.pairs(_.mapValues(group, function(m){
	return m.length
}))

var sort = _.sortBy(types, function(f){
	return f[1]
})
var p = _.pullAt(sort, 4, 5)
console.log(sort)

var total = _.sum(sort, function(t){
	return t[1]
	})
return total
{% endlodash %}
There were: {{result}} cancellations due to bird strikes

# What type of aircraft has the most instances of damaged caused by bird strikes? (Zhili Yang)

{% lodash %}
var filter=_.filter(data, function(air){
    return air['Effect: Indicated Damage'] == "Caused damage"
})
var groups=_.groupBy(filter, function(air){
    return air['Aircraft: Type']
})
var maxGroups=_.mapValues(groups, function(g){
    return _.size(g)
})
var maxType=_.pick(maxGroups, function(g){
    return g == _.max(maxGroups)
})
console.log(maxType);
return maxType
{% endlodash %}
{{result | json}}

# What states cost the airlines the most money? (Cost and location) by Andrew Berumen

{% lodash %}
var groups =  _.groupBy(data, 'Origin State')
var statesCost = _.mapValues(groups, function(d){
	var cost = _.pluck(d, 'Cost: Total $')
	return  _.sum(cost)
})

return statesCost
{% endlodash %}
{{result | json}}
