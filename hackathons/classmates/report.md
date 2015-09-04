{% import './data.html' as data %}

# Report

As a class, we brainstormed and came up with a long list of further questions we can ask based
on the "self-introduction" data. Out of these questions, our team chose to tackle on
the following:

# (who changed their comment?)

{% lodash %}
return _.pluck(_.pluck(_.filter(data.comments, function(n){
return (n.created_at != n.updated_at)}), 'user'),'login')
{% endlodash %}

Their names are {{result | json}}.



# Who has the oldest account?

{% lodash %}
return _.pluck(_.sortBy(data.comments, function(comment){
	return comment.user.id;
}), 'user.login');
{% endlodash %}

{{result | json}}


# Who wrote the most for thier comment

{% lodash %}
return _.pluck(_.sortBy(data.comments, function(comment){
		return _.size(comment.body.split(""));
		}).reverse(), 'user.login');

{% endlodash %}

{{result | json}}

# When did people post comments?

{% lodash %}
var counts = _.groupBy(_.map(_.pluck(data.comments, 'created_at'), function(r) {
    return parseInt(r.slice(9, 10));
}), function(i) {
    return i;
});
var vals = [];
for (i = 0; i < 8; i++) {
    try {
        vals.push(counts[i].length);
    } catch(err) {
        vals.push(0);
    }
}
return vals;
{% endlodash %}

{{result }}

We can visualize this...

<svg style="width:100%;">
{% for row in result %}
<rect x="{{ 25 * (loop.index - 1) }}" y="{{ 100 - ((100 * row) / 20) }}" width="20" height="{{ ((100 * row) / 20) }}" style="fill:#5DA5DA;stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>
