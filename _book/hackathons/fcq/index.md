{% data src="fcq.clean.json" %}
{% enddata %}

# FCQ

The objective of today's hackathon is to produce a data-driven report
to provide some insight into the FCQ data. We've prepared a slice of the dataset.
There are {{data.length}} records in this slice.

The first record looks like

{{data[0] | json}}

## Examples

Study the following examples of aggregate analysis across colleges based
on the `CrsPBAColl` field.

### How many courses have a valid college code?

{% lodash %}
return _.filter(data, function(d){
            return d['CrsPBAColl']
        })    
{% endlodash %}

The answer is {{ result.length }}.

## What are the unique college codes?

{% lodash %}
return _.compact(_.uniq(_.pluck(data, 'CrsPBAColl')))
{% endlodash %}

They are {{ result }}.

## What is the distribution of the courses across colleges?

{% lodash %}
var grps = _.groupBy(data, 'CrsPBAColl')
return _.mapValues(grps, function(d){
    return d.length
})
{% endlodash %}

{{ result | json}}

## What are the total student enrollments compared across colleges?

{% lodash %}
var grps = _.groupBy(data, 'CrsPBAColl')
return _.mapValues(grps, function(d){
    var enrollNumbers = _.pluck(d, 'N.ENROLL')
    return _.sum(enrollNumbers)
})
{% endlodash %}

{{ result | json}}
