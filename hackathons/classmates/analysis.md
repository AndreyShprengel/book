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
return _.pluck(_.pluck(_.filter(data.comments, function(n){
return (n.body.toLowerCase().match(/.*python.*/))}), 'user'),'login')
	
{% endlodash %}

Their names are {{result | json}}.

## Are there more Javascript lovers or Java lovers?

{% lodash %}
java =  _.size(_.filter(data.comments, function(n){
return (n.body.toLowerCase().match(/.*java\r\.*/))}))

javascript =  _.size(_.filter(data.comments, function(n){
return (n.body.toLowerCase().match(/.*javascript.*/))}))
if (java > javascript) { return "java"}
else{return "javascript"}
{% endlodash %}

The answer is {{result}}.

## Who like the same food as `kjblakemore`?

{% lodash %}
food = _.last(_.pluck(_.filter(data.comments , function(n){ return n.user.login == 'kjblakemore'}),'body')[0].toLowerCase().split("food: "))
return _.pluck(_.pluck(_.filter(data.comments, function(n){
return (_.last(n.body.toLowerCase().split("food: "))== food)}), 'user'),'login')
{% endlodash %}
  
Their names are {{result | json}}.
