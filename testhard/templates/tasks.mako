
<%inherit file="/szablon.mako"/>

<h2> Tasks </h2>

${h.link_to('ALL', url('/'))} - ${h.link_to('Finished', url('/'))} - ${h.link_to('Unfinished', url('/'))}
<table border="1">
<tr>
    <th>No.</th>
    <th>Name</th>
    <th>Repository</th>
    <th>Date</th>
    <th>E-mail</th>
    <th>Result</th>
</tr>
% if c.tasks:
    % for task in c.tasks:
    <tr>
        <td>${c.tasks.index(task)}</td>
        <td>${task.name}</td>
        <td>${rep.url}</td>
        <td>${rep.typ}</td>
        <td>${rep.Auth}</td>
        <td><a href="/repository/remove?name=${rep.name}">remove</a></td>
    </tr>
    % endfor
%endif
</table>

