// Auth - Admin Users Management

function bindAdminUsers() {
	var umResetForm = function (data) {
		if (!data) {
			$('#umForm input[name=usertype]').eq(0).prop('checked', true);
			$('#inputName').val('');
			$('#inputUsername').val('');
			$('#inputPassword').val('');
			$('#inputPasswordConfirm').val('');
			$('#inputNotes').val('');
			$('#inputRole').val('ADMIN');
			$('#inputEmail').val('');
			$('#inputBirthday').val('');
			$('#inputActiveUntil').val('');
			$('#inputGender').val('m');
		}
		else {
			$('#umForm input[name=usertype][value=' + data.usertype + ']').prop('checked', true);
			$('#inputName').val(data.name);
			$('#inputUsername').val(data.username);
			$('#inputPassword').val('');
			$('#inputPasswordConfirm').val('');
			$('#inputNotes').val(data.notes);
			$('#inputEmail').val(data.email);
			$('#inputRole').val(data.role);
			if (data.birthday) {
				$('#inputBirthday').val(moment(data.birthday).format('DD/MM/YYYY'));
			} else {
				$('#inputBirthday').val('');
			}
			if (data.activeuntil) {
				$('#inputActiveUntil').val(moment(data.activeuntil).format('DD/MM/YYYY'));
			} else {
				$('#inputActiveUntil').val('');
			}
			$('#inputGender').val(data.gender);
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
		
		//Controllo sulla corretta sintassi del campo email, se inserito 
		$('#inputEmail').parents('.form-group').removeClass('has-error');
		if ($('#inputEmail').val() != '' && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test($('#inputEmail').val()) == false) {			
			$('#inputEmail').parents('.form-group').addClass('has-error');
			all_ok = false;
		}
		
		return all_ok;
	};
	
	var ULMSearch = function (url, q) {
		$.ajax(
			url,
			{
				data: {
					q: q
				}
			}
		)
		.done( function (res) {
			$('#ULMSearchResults').empty();
			$.each(res.results, function () {
				u = this;
				var elem = $('<div />')
									.addClass('col-md-4 addLink')
									.append(
										$('<a />')
											.attr('href', '#')
											.append(
												$('<span />')
													.addClass('fa fa-plus-circle')
													.text(' '),
												(' ' + u.name + ' (' + u.linked_users_num + ')')
											)
									)
									.data('user', u);
				$('#ULMSearchResults').append(elem);
			});
		});
	};
	ULMSearch.start = function (url, q) {
		if (ULMSearch.timeoutID) {
			window.clearTimeout(ULMSearch.timeoutID);
		}
		ULMSearch.timeoutID = window.setTimeout(ULMSearch, 400, url, q);
	}
	
	var updateUserSearch = function (q) {
		if (q.length > 2) {
			//search
			$('.searchable').parents('.userRow').show();
			$(".searchable:not(:icontains(" + q + "))").parents('.userRow').hide();
		} else {
			$('.searchable').parents('.userRow').show();
		}
	}
	
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
			if (!window.confirm('ATTENZIONE! Cancellare l\'utente??')) {
				return false;
			}
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
		
		$('#btnAdd1m').on('click', function (e) {
			var m = moment();
			m.add('month', 1);
			$('#inputActiveUntil').val(m.format('DD/MM/YYYY'));
			return false;
		});
		
		$('#btnAdd6m').on('click', function (e) {
			var m = moment();
			m.add('month', 6);
			$('#inputActiveUntil').val(m.format('DD/MM/YYYY'));
			return false;
		});
		
		$('#btnAdd1y').on('click', function (e) {
			var m = moment();
			m.add('year', 1);
			$('#inputActiveUntil').val(m.format('DD/MM/YYYY'));
			return false;
		});
		
		$('.btnLinkUsers').on('click', function () {
			var btn = $(this);
			$('#UserLinksModal').modal('show');
			$('#ULMSearchResults').empty();
			$('#ULMLinkedUsersContainer').empty();
			$('#ULMViewedBy').empty();
			$('#ULMViews').empty();
			$('#UMLForm').attr('action', btn.data('url-save'));
			$.ajax(
				btn.data('url')
			)
			.done(function (res) {
				//console.log(res);
				$('#ULMTitle').text(res.name);
				$('#userSearch').val('');
				// already linked
				$.each(res.linked_users, function () {
					var u = this;
					var elem = $('<div />')
										.addClass('col-md-4 removeLink')
										.append(
											$('<a />')
												.attr('href', '#')
												.append(
													$('<span />')
														.addClass('fa fa-times-circle')
														.text(' '),
													(' ' + u.name + ' (' + u.linked_users_num + ')'),
													$('<input />')
														.attr('name', 'linkedusers')
														.attr('type', 'hidden')
														.val(u.id)
												)
												
										);
					$('#ULMLinkedUsersContainer').append(elem);
				});
				// load Views and ViewedBy
				$.ajax(
					res.url_visibility
				)
				.done(function (res) {
					// Views
					if (res.views) {
						var ul = $('<ul />');
						$.each(res.views, function (){
							var u = this;
							ul.append(
								$('<li />')
									.html(this.name)
							)
						});
						$('#ULMViews').html(ul);
					}
					// ViewedBy
					if (res.viewedby) {
						var ul = $('<ul />');
						$.each(res.viewedby, function (){
							var u = this;
							ul.append(
								$('<li />')
									.html(this.name)
							)
						});
						$('#ULMViewedBy').html(ul);
					}
				});
			});
			
			return false;
		})
		
		// User Links Modal events
		$('#UserLinksModal').on('click', '.removeLink', function () {
			$(this).remove();
			return false;
		});
		
		$('#UserLinksModal').on('click', '.addLink', function () {
			var u = $(this).data('user');
			var elem = $('<div />')
								.addClass('col-md-4 removeLink')
								.css('background-color', '#e0ffe0')
								.append(
									$('<a />')
										.attr('href', '#')
										.append(
											$('<span />')
												.addClass('fa fa-times-circle')
												.text(' '),
											(' ' + u.name + ' (' + u.linked_users_num + ')'),
											$('<input />')
												.attr('name', 'linkedusers')
												.attr('type', 'hidden')
												.val(u.id)
										)
										
								);
			$('#ULMLinkedUsersContainer').append(elem);
			
			return false;
		});
		
		$('#userSearch').on('keyup', function () {
			var v = $(this).val();
			if (v.length > 2) {
				//console.log(v);
				ULMSearch.start($(this).data('url'), v);
			} else {
				$('#ULMSearchResults').empty();
			}
		});
		
		$('#UserLinksModal .saveLinksBtn').on('click', function () {
			$('#UMLForm').submit();
		});
		
		$('#userListSearch').on('keyup', function () {
			updateUserSearch($('#userListSearch').val());
			return false;
		});
		
		$('#btnUserListSearch').on('click', function () {
			updateUserSearch($('#userListSearch').val());
			return false;
		});
	});	
}

