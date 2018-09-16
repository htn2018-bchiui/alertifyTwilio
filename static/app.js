$(function() {
	$.ajax({
            url: '/call',
            method: 'GET',
        }).done(function(data) {
            // The JSON sent back from the server will contain
            // a success message
            alert(data.message);
        }).fail(function(error) {
            alert(JSON.stringify(error));
        });
});