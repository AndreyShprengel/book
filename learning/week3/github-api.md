# Github API

The objective is to learn how to use Github's API to pull in real data. Your need
to figure out how to compose an URL for accessing a particular API to grab the data
you want.

Github provides a wide range of APIs. We will focus on these three for now.

* [Issues API](https://developer.github.com/v3/issues/)
* [Users API](https://developer.github.com/v3/users/)
* [Repositories API](https://developer.github.com/v3/repos/)

Carefully go through the examples below.

### What is the data of the first issue?

{% githubapi %}
https://api.github.com/repos/bigdatahci2015/forum/issues/1
{% endgithubapi %}

The data is saved in `data`. It looks like below.

{{ data | json }}

### What is the title of the first issue?

{{ data.title }}

### Who created this issue?

{{ data.user.login }}


### What are the comments of this issue?

{% githubapi %}
https://api.github.com/repos/bigdatahci2015/forum/issues/1/comments
{% endgithubapi %}

The comments data look like

{{ data | json }}

There are {{ data.length }} comments.

{% lodash %}
return _.pluck(data, 'user.login')
{% endlodash %}

The github account names are {{ result }}.

# Exercises

Now it's your turn to answer the following questions using the real data.

### How many issues have been created to date in our class's forum repository?

{% githubapi %}
https://api.github.com/repos/bigdatahci2015/forum/issues {% endgithubapi %}

{% lodash %}
return _.size(data)
{% endlodash %}

There are {{ result}} issues

### What are the titles of these issues?
{% lodash %}
return _.pluck(data, 'title')
{% endlodash %}

{{ result |json}}

### How many repository have been created to date for our class?

Our class's Github organization is [bigdatahci2015](https://github.com/bigdatahci2015/).

{% githubapi %}
https://api.github.com/orgs/bigdatahci2015/repos{% endgithubapi %}

{% lodash %}

return _.size(data)
{% endlodash %}

There are {{result}} repos

{{data |json }}
return _.chain(data)
            .map(function(obj) {
                return [obj["name"], obj["forks_count"]];
            })

{{result | json}}

### How many public repositories does the user `doubleshow` have?

{% githubapi %}
https://api.github.com/users/doubleshow/repos
{% endgithubapi %}
{% lodash %}

return _.size(data)
{% endlodash %}

There are {{result}} repos


### How many public gists does the user `doubleshow` have?
{% githubapi %}
https://api.github.com/users/doubleshow
{% endgithubapi %}

{% lodash %}

return data["public_gists"] 
{% endlodash %}
There are {{result}} gists
