
<%inherit file="/szablon.mako"/>

<h2> Tasks </h2>

${h.link_to('ALL', url('/'))} - ${h.link_to('Finished', url('/'))} - ${h.link_to('Unfinished', url('/'))}
<table border="1">
<tr>
    <th>No.</th>
    <th>Name</th>
    <th>Date</th>
    <th>E-mail</th>
    <th>Repository</th>
    <th>Result</th>
    <th></th>
</tr>
% if c.tasks:
    % for task in c.tasks:
    <tr>
        <td>${c.tasks.index(task)}</td>
        <td>${task['name']}</td>
        <td>${task['test_time']}</td>
        <td>${task['email']}</td>
        <td>${task['repository']}</td>
        % if task['failures_count']:
            %if int(task['failures_count']) > 0:
                <td style="color:red">Failed</td>
            %else:
                <td style="color:green">OK</td>
            %endif
        % else:
            <td style="color:gray">None</td>
        % endif
        <td><a href="/tasks/remove?name=${task['name']}">remove</a></td>
    </tr>
    % endfor
%endif
</table>

