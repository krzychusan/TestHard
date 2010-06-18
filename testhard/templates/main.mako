
<%inherit file="/szablon.mako"/>\

<p>
<h2> TestHard</h2>
TestHard is a distributed testing framework written in python. It uses Pylons as a web framework together with mako templates.
</p>


<p>
<h2> Statistics</h2>
Scheduled tests:<br>
${ c.taskCount }
<br>
Repositories:<br>
${ c.repCount }
<br>
</p>
