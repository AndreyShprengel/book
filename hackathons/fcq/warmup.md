{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.

## How many unique subject codes?

{% lodash %}
// TODO: replace with code that computes the actual result
return _.size(_.compact(_.uniq(_.pluck(data, 'Subject'))))

{% endlodash %}

They are {{ result }} unique subject codes.

## How many computer science (CSCI) courses?

{% lodash %}
// TODO: replace with code that computes the actual result
return _.size(_.filter(data, function(c){return c.Subject == "CSCI"}))
{% endlodash %}

They are {{ result }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}
// TODO: replace with code that computes the actual result
var groups = _.groupBy(data, function(c){return c.Subject})
return _.mapValues(groups, function(group){return _.size(group)})
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What subset of these subject codes have more than 100 courses?

{% lodash %}
// TODO: replace with code that computes the actual result
var grps = _.groupBy(data, 'Subject')
var ret = _.pick(_.mapValues(grps, function(d){
    return d.length
}), function(x){
    return x > 100
})
return ret
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What subset of these subject codes have more than 5000 total enrollments?

{% lodash %}
// TODO: replace with code that computes the actual result
var grps = _.groupBy(data, 'Subject')
var enroll = _.mapValues(grps, function(group){
	var total = 0
	_.map(group, function(n){
			total += n.N.ENROLL
			
			return total
				}
				)
				return total})
return _.pick(enroll, function(x) {return x > 5000})
{% endlodash %}

<table>utn
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What are the course numbers of the courses Tom (PEI HSIU) Yeh taught?

{% lodash %}
// TODO: replace with code that computes the actual result
var courses = _.filter(data, function(c){
					
					return _.some(c.Instructors, function(t){ 
							
							return t.name == "YEH, PEI HSIU"})})
							
return _.pluck(courses, "Course")
{% endlodash %}

They are {{result}}.
