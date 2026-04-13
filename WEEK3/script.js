function callAPI() {
    const name = document.getElementById("nameInput").value;

    const apiURL = "https://apinnmlge6.execute-api.us-east-2.amazonaws.com/hello?name=" + name;

    fetch(apiURL)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = data;
        })
        .catch(error => {
            document.getElementById("result").innerText = "Error calling API";
        });
}