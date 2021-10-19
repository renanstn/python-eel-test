function send_data(event) {
    event.preventDefault();
    console.log('click');

    const tibcoUrl = document.getElementById("tibco_url").value;
    const tableName = document.getElementById("table").value;
    const query = document.getElementById("query").value;
    const fields = document.getElementById("fields").value;

    eel.send_data(tibcoUrl, tableName, query, fields)
};

document.getElementById("send").addEventListener('click', send_data)
