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
    $('.example5-selector').jqCron({
        default_value: '30 2 1 * *',
        numeric_zero_pad: true,
        bind_to: $('.example5-span'),
        bind_method: {
            set: function($element, value) {
                $element.html(value);
            }
        }
    });
});
==========
<div class="example5-selector"></div>
<p><span class="example5-span"></span></p>