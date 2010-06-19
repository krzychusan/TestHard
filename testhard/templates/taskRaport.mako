
<%inherit file="/szablon.mako"/>

<h2> ${c.task['name']} raport </h2>

% if c.task['log']:
    Failures: <b> ${c.task['failures_count']} </b>
    <br/>
    Errors: <b> ${c.task['errors_count']} </b>
    <br/>
    Total test count: <b> ${c.task['tests_count']} </b>
    <br/>
    <b> TEST LOG: </b>
    <br/>
    ${c.task['log']}
%else:
    There is no log yet.
%endif

<br/>
<br/>
<a href="/tasks">return</a>
