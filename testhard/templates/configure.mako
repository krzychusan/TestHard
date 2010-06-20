
<%inherit file="/szablon.mako"/>\

<h2> Configuration </h2>


<form name="config" method="POST" action="/configure/save">
<table border="1">
<tr>
    <th>Key</th>
    <th>Value</th>
</tr>
% if c.conf:
    % for (k,v) in c.conf.items():
    <tr>
        <td>${k}</td>
        <td><input name="${k}" type="text" value="${v}"></td>
    </tr>
    % endfor
%endif
</table>

<div class="buttonsdiv">
    <input type="submit" value="Submit" style="margin-left: 50px;" />
</div>
</form>

