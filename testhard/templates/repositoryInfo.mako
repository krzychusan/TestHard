
<%inherit file="/szablon.mako"/>\

<h2> Detailed info '${c.info.name}' [<a href="/repository/edit?name=${c.info.name}">edit</a>]</h2>

<h4>Address:</h4> ${c.info.url}<br><br>
<h4>Typ:</h4> ${c.info.typ}<br><br>
% if c.info.login:
    <h4>Login:</h4> ${c.info.login}<br>
    <h4>Password:</h4> ${c.info.password}<br><br>
% else:
    <h4>Authorization not required</h4><br>
% endif

<h4>Comment:</h4>
<pre>${c.info.comment}</pre>

<h4>Build on server?:</h4>
${c.info.compileOnServer}<br><br>
<h4>Build commands:</h4>
<pre>${c.info.build_cmd}</pre>

<h4>Find test command:</h4>
<pre>${c.info.find_tests_cmd}</pre><br>
<h4>Run test command:</h4>
<pre>${c.info.run_test_cmd}</pre><br>

${h.link_to('Return', url('/repository'))}

