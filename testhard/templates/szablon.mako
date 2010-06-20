<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
        <meta name="keywords" content="">
        <meta name="description" content="">
        <title>TestHard</title>
        ${h.stylesheet_link('/template.css')}
    </head>

<body>
    <div id="doc4" class="yui-t1">
        <div id="hd">
            <h1> TestHard </h1>
        </div>
        <div id="bd">
            <div id="yui-main">
                <div class="yui-b">
                   ${next.body()}
                </div>
            </div>
            <div class="yui-b">
                <ul>
                    <li>${h.link_to('Main page', url('/'))}</li>
                    <li>${h.link_to('Repository', url('/repository'))}</li>
                    <li>${h.link_to('Run', url('/run'))}</li>
                    <li>${h.link_to('Tasks', url('/tasks'))}</li>
                    <li>${h.link_to('Configure', url('/configure'))}</li>
                </ul>
            </div>
        </div>
        <div id="ft">
            <p>All rights reserved 2010</p>
        </div>
    </div>
</body>
</html>

