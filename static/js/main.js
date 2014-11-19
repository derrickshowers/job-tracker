console.log('hello');

$("#newJobForm").submit(function(e){
    console.log(e);
    // e.preventDefault();

    var isValid = validateForm(this);
    return isValid;
});

function validateForm(form) {
    console.log(form);
    if(form.title.value === ""){
        alert("Error: Input is empty");
        // form.title.focus();
        console.log("no input");
        return false;
    }
    if(form.company.value === ""){
        alert("Error: Input is empty");
        // form.company.focus();
        return false;
    }
    return true;
}

