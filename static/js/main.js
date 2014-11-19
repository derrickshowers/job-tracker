document.ready
    console.log("hello world");


function validateForm(form) {
    if(form.title.value == ""){
        alert("Error: Input is empty");
        form.title.focus();
        console.log("no input");
        return false;
    }
    if(form.company.value == ""){
        alert("Error: Input is empty");
        form.company.focus();
        return false;
    }
    return true;
}