
<%inherit file="/szablon.mako"/>

<h2> ${c.info['test_case_name']}  Test Case raport </h2>

% if c.info['timestamp']:
    Timestamp: <b> ${c.info['timestamp']} </b>
    <br/>
    Failures: <b> ${c.info['failures_count']} </b>
    <br/>
    Errors: <b> ${c.info['errors_count']} </b>
    <br/>
    Total test count: <b> ${c.info['tests_count']} </b>
    <br/>
    Time elapsed: <b> ${c.info['time_elapsed']} </b>
    <br/>
    <br/>
    <b>Log:</b>
    <br/>
    <pre class="shcode"> ${c.info['log']} </pre>
%else:
    There is no log yet.
%endif

<br/>
<br/>
<a href="/tasks${c.ret}">return</a>
