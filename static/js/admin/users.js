// Auth - Admin Users Management
var umResetForm = function (data) {
	if (!data) {
		$('#umForm input[name=usertype]').eq(0).prop('checked', true);
		$('#inputName').val('');
		$('#inputUsername').val('');
		$('#inputPassword').val('');
		$('#inputPasswordConfirm').val('');
		$('#inputNotes').val('');
		$('#inputRole').val('ADMIN');
	}
	else {
		$('#umForm input[name=usertype][value=' + data.usertype + ']').prop('checked', true);
		$('#inputName').val(data.name);
		$('#inputUsername').val(data.username);
		$('#inputPassword').val('');
		$('#inputPasswordConfirm').val('');
		$('#inputNotes').val(data.notes);
		$('#inputRole').val(data.role);
	}
	$('#umForm .has-error').removeClass('has-error');
};

var umValidateForm = function () {
	var all_ok = true;
	
	if ($('#inputUsername').val() == '') {
		$('#inputUsername').parents('.form-group').addClass('has-error');
		all_ok = false;
	}
	
	if (($('#inputPassword').val() != '') && ($('#inputPassword').val() != $('#inputPasswordConfirm').val())) {
		$('#inputPassword').parents('.form-group').addClass('has-error');
		all_ok = false;
	}
	
	return all_ok;
};

$(function () {
	$('.newUserBtn').on('click', function () {
		umResetForm();
		$('#umForm').attr('action', $(this).data('url'));
		$('#UserModal').modal('show');
	});
	
	$('.modUser').on('click', function () {
		$('#umForm').attr('action', $(this).data('url'));
		
		$.ajax(
			$(this).attr('href')
		)
		.done( function (data) {
			umResetForm(data);
			$('#UserModal').modal('show');
		});
		
		return false;
	});
	
	$('#UserModal .saveBtn').on('click', function () {
		if (umValidateForm()) {
			$('#umForm').submit();
		}
	});
	
	$('.deleteUser').on('click', function () {
		var row = $(this);
		$.ajax(
			$(this).data('url'),
			{
				type: 'DELETE'
			}
		)
		.done( function (res) {
			if (res=='OK') {
				//code
				row.parents('tr').fadeOut();
			}
			else {
				window.alert("ERROR!");
			}
		});
		
		return false;
	});
});