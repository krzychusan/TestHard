
<%inherit file="/szablon.mako"/>

<h2> Repositories </h2>

<form class="feedbackform" method="GET" action="/repository/doAdd">
<div class="fieldwrapper">
    <label for="name" class="styled">Name:</label>
    <div class="thefield">
        <input type="text" name="name" id="name" value="" size="30" />
    </div>
</div>

<div class="fieldwrapper">
    <label for="url" class="styled">Url:</label>
    <div class="thefield">
        <input type="text" name="url" id="url" value="" size="30" /><br />
        <span style="font-size: 80%">*Note: Please make sure it's correctly entered!</span>
    </div>
</div>

<div class="fieldwrapper">
    <label for="login" class="styled">Login:</label>
    <div class="thefield">
        <input type="text" name="login" id="login" value="" size="30" />
    </div>
</div>

<div class="fieldwrapper">
    <label for="password" class="styled">Password:</label>
    <div class="thefield">
        <input type="text" name="password" id="password" value="" size="30" />
    </div>
</div>

<div class="fieldwrapper">
    <label for="type" class="styled">Type:</label>
    <div class="thefield">
        <select name="type" id="type">
        % for typ in c.repTypes:
            <option value="${typ.typ}">${typ.typ}</option>
        % endfor
        </select>
    </div>
</div>

<div class="fieldwrapper">
    <label for="about" class="styled">Build commands:</label>
    <div class="thefield">
        <textarea name="build_cmd" id="about"></textarea>
    </div>
</div>

<div class="fieldwrapper">
    <label for="about" class="styled">Find tests command:</label>
    <div class="thefield">
        <textarea name="find_tests_cmd" id="about"></textarea>
    </div>
</div>

<div class="fieldwrapper">
    <label for="about" class="styled">Run test command:</label>
    <div class="thefield">
        <textarea name="run_test_cmd" id="about"></textarea>
    </div>
</div>

<div class="fieldwrapper">
    <label for="about" class="styled">Comment:</label>
    <div class="thefield">
        <textarea name="comment" id="about"></textarea>
</div>
</div>

<div class="buttonsdiv">
    <input type="submit" value="Submit" style="margin-left: 150px;" /> <input type="reset" value="Reset" />
</div>

</form>


