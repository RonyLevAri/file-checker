function user_action() {
    console.log('add file');
    var file = $('#url').val();
    $('#url').val('');

    $.ajax({
        type: "POST",
        url: "/actionfile",
        data: {
            url: file,
            message: this.firstChild.nodeValue
        },
        success: function (response) {
            console.log(response['responseText']);
            var message = $('#messages-section');
            message.find('strong').html(response['responseText']);
            message.show()
        },
        error: function (response) {
            console.log(response['responseText']);
            var message = $('#messages-section');
            message.find('strong').html(response['responseText']);
            message.show()
        },
        completes: function () {

        }
    });
}

$('#add_file').click(user_action);

$('#check_file').click(user_action);

$('#add_mail').click(function () {

    var email = $('#email').val();
    $('#email').val('');
    $.ajax({
        type: "POST",
        url: "/addmail",
        data: {
            email: email,
            message: this.firstChild.nodeValue
        },
        success: function (response) {
            console.log(response['responseText']);
            var message = $('#messages-section');
            message.find('strong').html(response['responseText']);
            message.show()
        },
        error: function (response) {
            console.log(response['responseText']);
            var message = $('#messages-section');
            message.find('strong').html(response['responseText']);
            message.show()
        },
        completes: function () {

        }
    });
});

$('#get_logs').click(function () {
        var ret = 'Unfortunately this fnctionality is unavailable :('
        var message = $('#messages-section');
        message.find('strong').html(ret);
        message.show()

    // $.ajax({
    //     type: "POST",
    //     url: "/logs",
    //     data: {
    //     },
    //     success: function (response) {
    //         console.log(response['responseText']);
    //         var message = $('#messages-section');
    //         message.find('strong').html(response['responseText']);
    //         message.show()
    //     },
    //     error: function (response) {
    //         console.log(response['responseText']);
    //         var message = $('#messages-section');
    //         message.find('strong').html(response['responseText']);
    //         message.show()
    //     },
    //     completes: function () {
    //
    //     }
    // });
});

// $('#activate').click(function () {
//     var button_value = this.firstChild.nodeValue;
//
//     if (button_value === "Activate File Checker") {
//         this.firstChild.nodeValue = "Deactivate File Checker";
//         $('#main_content_section').show();
//         $.ajax({
//             type: "POST",
//             url: "/activate",
//             data: {
//                 message: "Activate",
//             },
//             success: function (response) {
//                 var res = parse_json(response);
//                 var message = $('#messages-section');
//                 message.find('strong').html(res);
//                 message.show();
//             },
//             error: function (response) {
//                 var res = parse_json(response);
//                 var message = $('#messages-section');
//                 message.find('strong').html(res);
//                 message.show();
//             },
//             completes: function () {
//
//             }
//
//         });
//         // activate server
//     } else {
//         this.firstChild.nodeValue = "Activate File Checker";
//         $('#main_content_section').hide();
//         $.ajax({
//             type: "POST",
//             url: "/activate",
//             data: {
//                 message: "Deactivated",
//             },
//             success: function (response) {
//                 var res = parse_json(response);
//                 var message = $('#messages-section');
//                 message.find('strong').html(res);
//                 message.show();
//             },
//             error: function (response) {
//                 var res = parse_json(response);
//                 var message = $('#messages-section');
//                 message.find('strong').html(res);
//                 message.show();
//             },
//             completes: function () {
//
//             }
//
//         });
//     }// deactivate server
// });

