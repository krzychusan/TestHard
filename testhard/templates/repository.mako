
<%inherit file="/szablon.mako"/>\

<h2> Repositories </h2>

<table border="1">
<tr>
    <th>No.</th>
    <th>Name</th>
    <th>Url</th>
    <th>Type</th>
    <th>Auth</th>
    <th>remove</th>
</tr>
% if c.repos:
    % for rep in c.repos:
    <tr>
        <td>${c.repos.index(rep)}</td>
        <td>${rep.name}</td>
        <td>${rep.url}</td>
        <td>${rep.typ}</td>
        <td>${rep.Auth}</td>
        <td><a href="/repository/remove?name=${rep.name}">remove</a></td>
    </tr>
    % endfor
%endif
</table>

${h.link_to('Add', url('/repository/add'))}
