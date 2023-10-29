function addInventory() {
    fetch("{% url 'Inventory:create_folder' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    })
    .then(function (response) {
        if (response.status === 200) {
            var myModal = new bootstrap.Modal(document.getElementById("addInventoryModal"));
            myModal.hide();
            document.getElementById("form").reset();
        }
    });
    return false;
}

document.getElementById("button_add").onclick = addInventory;