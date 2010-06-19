
<%inherit file="/szablon.mako"/>\

<h2> Detailed info '${c.task['name']}'</h2>

<h4>Date:</h4> ${c.task['test_time']}<br><br>

<h4>Repository:</h4> ${c.task['repository']}<br><br>

<h4>Email:</h4> ${c.task['email']}<br><br>

<h4>Comment:</h4>
${c.task['comment']}<br><br>

<h2> Repository info '<a href="#">${c.task['repository']}</a>'</h2>

${h.link_to('Return', url('/tasks'))}


