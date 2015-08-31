# Data

{% import './data.html' as data %}

There are {{ data.comments.length }} comments.

The raw data is in the JSON format and is shown below.

{{ data.comments | json }}
