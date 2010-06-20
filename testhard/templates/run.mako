
<%inherit file="/szablon.mako"/>\
<head>
<script language="JavaScript" src="ts_picker.js">
//Script by Denis Gritcyuk: tspicker@yahoo.com
//Submitted to JavaScript Kit (http://javascriptkit.com)
//Visit http://javascriptkit.com for this script
</script>
</head>

<p>
<h2> Add new task</h2>
<p>

<form class="feedbackform" name="addRun" method="GET" action="/run/addRun">
<div class="fieldwrapper">
    <label for="name" class="styled">Name:</label>
    <div class="thefield">
        <input type="text" name="name" id="name" value="" size="30" />
    </div>
</div>

<div class="fieldwrapper">
    <label for="repository" class="styled">Repository:</label>
    <div class="thefield">
        <select name="repo" id="repo">
        % for typ in c.repTypes:
            <option value="${typ.name}">${typ.name}</option>
        % endfor
        </select>
    </div>
</div>
<div class="fieldwrapper">
    <label for="date" class="styled">Date:</label>
    <div class="thefield">
        <input type="Text" name="timestamp" value=""><a href="javascript:show_calendar('document.addRun.timestamp', document.addRun.timestamp.value);"><img src="cal.gif" width="16" height="16" border="0" alt="Click Here to Pick up the timestamp"></a>
        <br><span style="font-size: 80%">*Note: Use graphical tool if you are unsure of format.</span>
    </div>
</div>

<div class="fieldwrapper">
    <label for="email" class="styled">Email:</label>
    <div class="thefield">
        <input type="text" name="email" id="email" value="" size="30" />
    </div>
</div>

<div class="fieldwrapper">
    <label for="about" class="styled">Comment:</label>
    <div class="thefield">
        <textarea name="comment" id="about"></textarea>
    </div>
</div>

<div class="buttonsdiv">
    <input type="submit" value="Add" style="margin-left: 150px;" /> <input type="reset" value="Reset" />
</div>

</form>
