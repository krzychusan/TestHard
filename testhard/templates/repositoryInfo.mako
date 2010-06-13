
<%inherit file="/szablon.mako"/>\

<h2> Detailed info ${c.info.name}</h2>

% if c.repos:
    % for rep in c.repos:
    <tr>
        <td>${c.repos.index(rep)}</td>
        <td><a href="/repository/info?name=${rep.name}">${rep.name}</a></td>
        <td>${rep.url}</td>
        <td>${rep.typ}</td>
        <td>${rep.Auth}</td>
        <td><a href="/repository/remove?name=${rep.name}">remove</a></td>
    </tr>
    % endfor
%endif

${h.link_to('Return', url('/repository'))}

