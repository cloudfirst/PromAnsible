<?php
header('Content-Type: text/html; charset=utf-8');
$elements = explode('==========', substr(file_get_contents(__FILE__), __COMPILER_HALT_OFFSET__));
echo strtr(file_get_contents('demo.tpl'),
	array(
	'__DEMO__' => basename(__FILE__, '.php'),
	'__JS__' => $elements[1],
	'__JSPRE__' => htmlspecialchars($elements[1]),
	'__HTML__' => $elements[2],
	'__HTMLPRE__' => htmlspecialchars($elements[2]),
	)
);

__halt_compiler();
==========
$(function(){
    var cron =
        $('.example5')
        .jqCron()
        .jqCronGetInstance();
     
    $('.a5-enable').click(function(e){
        cron.enable();
        e.preventDefault();
    });
     
    $('.a5-disable').click(function(e){
        cron.disable();
        e.preventDefault();
    });
     
    $('.a5-toggle').click(function(e){
        if(cron.isDisabled())
            cron.enable();
        else
            cron.disable();
        e.preventDefault();
    });
});
==========
<div class="example5"></div>
<p style="margin-top:1em">
    <a href="#" class="a5-enable">Enable</a> 
    <a href="#" class="a5-disable">Disable</a> 
    <a href="#" class="a5-toggle">Toggle</a> 
</p>