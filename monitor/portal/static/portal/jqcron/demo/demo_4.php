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
    $('.example4-selector').jqCron({
        default_value: '30 2 1 * *',
        bind_to: $('.example4-span'),
        bind_method: {
            set: function($element, value) {
                $element.html(value);
            }
        }
    });
});
==========
<div class="example4-selector"></div>
<p><span class="example4-span"></span></p>