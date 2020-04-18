function fetchCPUUtilization() {
    ajax_get("https://83e8rxa4f4.execute-api.ap-south-1.amazonaws.com/default/testCPU", function(data) {
        document.getElementById("cpuutil-id").innerHTML = data["CPUUtilization"] + "%";
    });
}

function fetchHostname() {
    ajax_get("https://df7klcan56.execute-api.ap-south-1.amazonaws.com/default/servername", function(data) {
        document.getElementById("servername-id").innerHTML = data["hostname"] + " - Server Dashboard";
    });
}

function get_MemoryUtilization() {
    ajax_get("https://hwitv71p0f.execute-api.ap-south-1.amazonaws.com/default/Get_MemoryDetails", function(data) {
        document.getElementById("physicalmemory-id").innerHTML = data["memory"] + "GB";
        document.getElementById("virtualmemory-id").innerHTML = data["memory"] + "GB";
    });
}

function ajax_get(url, callback) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            console.log('responseText:' + xmlhttp.responseText);
            try {
                var data = JSON.parse(xmlhttp.responseText);
            } catch (err) {
                console.log(err.message + " in " + xmlhttp.responseText);
                return;
            }
            callback(data);
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

function generateReport() {
    var link = document.createElement('a');
    link.href = "https://www.infoblox.com/wp-content/uploads/infoblox-datasheet-infoblox-reporting-and-analytics-sample-report.pdf";
    link.download = 'sample.pdf';
    link.dispatchEvent(new MouseEvent('click'));
}