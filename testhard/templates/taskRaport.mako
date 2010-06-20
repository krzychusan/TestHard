
<%inherit file="/szablon.mako"/>

<h2> ${c.task['name']} raport </h2>

% if c.task['timestamp']:
    Timestamp: <b> ${c.task['timestamp']} </b>
    <br/>
    Failures: <b> ${c.task['failures_count']} </b>
    <br/>
    Errors: <b> ${c.task['errors_count']} </b>
    <br/>
    Total test count: <b> ${c.task['tests_count']} </b>
    <br/>
    <br/>
    <b>Logs and unit results:</b>
    <br/>
    % for file in c.testCases:
    %   if file['failures'] + file['errors'] > 0: 
            <a style="color:red" href="/tasks/raportCase?name=${file['name']}&task=${c.task['name']}">
            ${file['name']} </a><br/>
    %   else:
            <a style="color:green;" href="/tasks/raportCase?name=${file['name']}&task=${c.task['name']}">
            ${file['name']} </a><br/>
    %   endif
    % endfor
%else:
    There is no log yet.
%endif

<br/>
<br/>
<a href="/tasks">return</a>
