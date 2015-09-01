# Analysis

{% import './data.html' as data %}

After completing the warmup exercises, your task is to do four more slightly
more challenges analyses.

## How many students like sushi as their favorite food?

{% lodash %}
return  _.size(_.filter(_.pluck(data.comments, 'body'), function(n){

return _.last(n.toLowerCase().split(" ")) == 'sushi'}
	))
{% endlodash %}

The answer is {{result}}.

## Who are the students liking Python the most?

{% lodash %}
return _.size(_.filter(_.pluck(data.comments, 'body'), function(n){
return (n.toLowerCase().match(/.*python.*/))}))
	
{% endlodash %}

Their names are {{result}}.

## Are there more Javascript lovers or Java lovers?

{% lodash %}
return "[answer]"
{% endlodash %}

The answer is {{result}}.

## Who like the same food as `kjblakemore`?

{% lodash %}
return "[answer]"
{% endlodash %}

Their names are {{result}}.
