
<%inherit file="/szablon.mako"/>\

<p>
<h2> Add new task</h2>
<p>

<form class="feedbackform" method="GET" action="/repository/doAdd">
<div class="fieldwrapper">
    <label for="name" class="styled">Name:</label>
    <div class="thefield">
        <input type="text" name="name" id="name" value="" size="30" />
    </div>
</div>

<div class="fieldwrapper">
    <label for="repository" class="styled">Repository:</label>
    <div class="thefield">
        <select name="repository" id="repo">
        % for typ in c.repTypes:
            <option value="${typ.name}">${typ.name}</option>
        % endfor
        </select>
    </div>
</div>
<div class="fieldwrapper">
    <label for="date" class="styled">Date:</label>
    <div class="thefield">
        <input type="text" name="url" id="url" value="" size="30" /><br />
        <span style="font-size: 80%">*Note: Please make sure it's correctly entered!</span>
    </div>
</div>

<div class="fieldwrapper">
    <label for="email" class="styled">Email:</label>
    <div class="thefield">
        <input type="text" name="login" id="login" value="" size="30" />
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
