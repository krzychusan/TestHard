
<%inherit file="/szablon.mako"/>\

<h2> Detailed info '${c.task['name']}'</h2>

<h4>Date:</h4> ${c.task['test_time']}<br><br>

<h4>Repository:</h4> 
Name: <a href="/repository/info?name=${c.task['repository']}"> ${c.task['repository']} </a> <br>
Url: ${c.info.url} <br>
Type: ${c.info.typ} <br><br>

<h4>Email:</h4> ${c.task['email']}<br><br>

<h4>Comment:</h4>
${c.task['comment']}<br><br>

${h.link_to('Return', url('/tasks'))}


