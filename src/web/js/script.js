function send_data(event) {
  event.preventDefault();

  document.getElementById("content").style.display = "none";
  document.getElementById("loading-icon").style.display = "block";

  const tibcoUrl = document.getElementById("tibco_url").value;
  const tableName = document.getElementById("table").value;
  const query = document.getElementById("query").value;
  const fields = document.getElementById("fields").value;

  eel.send_data(tibcoUrl, tableName, query, fields)(function(response) {
    const string_response = JSON.stringify(response, null, 2);
    document.getElementById("response-text").value = string_response;
    change_tab_to_response();
    document.getElementById("loading-icon").style.display = "none";
    document.getElementById("content").style.display = "block";
  });
};

function change_tab_to_response() {
  document.getElementById("response-tab").click();
};

function save_data(event) {
  event.preventDefault();

  const data = {
    tibcoUrl: document.getElementById("tibco_url").value,
    tableName: document.getElementById("table").value,
    query: document.getElementById("query").value,
    fields: document.getElementById("fields").value,
  };

  eel.save_data(data);
};

function load_data() {
  eel.load_data()(function(data) {
    document.getElementById("tibco_url").value = data.tibcoUrl;
    document.getElementById("table").value = data.tableName;
    document.getElementById("query").value = data.query;
    document.getElementById("fields").value = data.fields;
  });
};

function copy_data() {
  const content = document.getElementById("response-text").value;
  navigator.clipboard.writeText(content);
}

document.getElementById("send").addEventListener("click", send_data);
document.getElementById("tibco_url").addEventListener("change", save_data);
document.getElementById("table").addEventListener("change", save_data);
document.getElementById("query").addEventListener("change", save_data);
document.getElementById("fields").addEventListener("change", save_data);
document.getElementById("copy").addEventListener("click", copy_data);

load_data();
