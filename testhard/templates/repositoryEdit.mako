
<%inherit file="/szablon.mako"/>\

<h2> Edit ${c.info} </h2>

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
    <label for="build_cmd" class="styled">Build commands:</label>
    <div class="thefield">
        <textarea name="build_cmd" id="build_cmd"></textarea>
    </div>
</div>

<div class="fieldwrapper">
    <label for="find_tests" class="styled">Find tests command:</label>
    <div class="thefield">
        <textarea name="find_tests" id="find_tests"></textarea>
    </div>
</div>

<div class="fieldwrapper">
    <label for="run_test" class="styled">Run test command:</label>
    <div class="thefield">
        <textarea name="run_test" id="run_test"></textarea>
    </div>
</div>

<div class="fieldwrapper">
    <label for="comment" class="styled">Comment:</label>
    <div class="thefield">
        <textarea name="comment" id="comment"></textarea>
</div>
</div>

<div class="buttonsdiv">
    <input type="submit" value="Submit" style="margin-left: 150px;" /> <input type="reset" value="Reset" />
</div>

</form>

${h.link_to('Add', url('/repository/add'))}

