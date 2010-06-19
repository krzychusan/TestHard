
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
        <td><a href="/tasks/info?name=${task['name']}">${task['name']}</a></td>
        <td>${task['test_time']}</td>
        <td>${task['email']}</td>
        <td>${task['repository']}</td>
        <td><a href="/tasks/showRaport?name=${task['name']}">
        % if task['failures_count'] is not None:
            %if int(task['failures_count']) > 0:
                <p style="color:red">Failed</p>
            %else:
                <p style="color:green">OK</p>
            %endif
        % else:
            <p style="color:gray">None</p>
        % endif
        </a>
        </td>
        <td><a href="/tasks/remove?name=${task['name']}">remove</a></td>
    </tr>
    % endfor
%endif
</table>

