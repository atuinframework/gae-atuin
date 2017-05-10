// Auth - Admin Users Management

var bindUsersAdmin = function () {
	var modal = $('#UserModal'),
		form = $('#umForm');
	
	$('.newUserBtn').on('click', function () {
		form.formtools('reset');

		form.attr('action', $(this).data('url'));
		modal.modal('show');
	});
		
	$('.modUser').on('click', function () {
		form.attr('action', $(this).data('url'));
		
		$.ajax(
			$(this).attr('href')
		)
		.done( function (data) {
			form.formtools('reset', data);
			modal.modal('show');
		});
		
		return false;
	});
		
	modal.find('.btnSave').on('click', function () {
		if (form.formtools('validate')) {
			var btn = $(this);
			btn.button('loading');
			$.ajax(
				form.attr('action'),
				{
					method: 'post',
					data: form.serialize()
				}
			)
			.done( function (data) {
				setTimeout("window.location.reload()", timeToRefresh);
				//console.log(data);
			})
			.fail( function (err) {
				alert(_t('Error'));
				btn.button('reset');
			});
		}
	});
		
	$('.deleteUser').on('click', function () {
		if (!window.confirm(_t('WARNING! Are you sure to delete the user?'))) {
			return false;
		}
		var row = $(this).closest('tr');
		$.ajax(
			$(this).data('url'),
			{
				method: 'DELETE'
			}
		)
		.done( function (res) {
			if (res=='OK') {
				row.slideUp();
			} else {
				alert(_t('Error'));
			}
		});
	});
}
