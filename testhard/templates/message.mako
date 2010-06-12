
<%inherit file="/szablon.mako"/>\

${c.message}
<br>
% if c.link:
<a href="${c.link}">Return</a>
% else:
<a href="/">Return</a>
% endif

