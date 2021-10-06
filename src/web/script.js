$(document).ready(function () {

    $("#send").click(function (event) {
        event.preventDefault();

        const tibcoUrl = $("#tibco_url").val();
        const tableName = $("#table").val();
        const query = $("#query").val();
        const fields = $("#fields").val();

        eel.send_data(tibcoUrl, tableName, query, fields)
    });

});
