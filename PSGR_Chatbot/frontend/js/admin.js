function addFAQ() {
    const domain = document.getElementById("domain").value;
    const keywords = document.getElementById("keywords").value.split(",");
    const reply = document.getElementById("reply").value;

    fetch("http://127.0.0.1:5000/admin/add-faq", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ domain, keywords, reply })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("status").innerText =
            data.message || data.error;
    });
}
