/*
 * Base generic functions
 */


/*
 *jQuery hack to add case insensitive contains() selector named :icontains
 */
jQuery.expr[":"].icontains = jQuery.expr.createPseudo(function(arg) {
    return function( elem ) {
        return jQuery(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
});

$('.btnLogin').on('click', function () {
	console.log('!!!!');
	$('#loginForm').submit();
	return false;
});

$('#loginForm input').on('keyup', function (ev) {
	var code = ev.which;
	if (code == 13) {
		$('#loginForm').submit();
	}
});

$('.panel-link').on('click', function () {
	window.location = $(this).attr('href');
});

